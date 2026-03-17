from __future__ import annotations

import json
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from .kraken_trade_client import get_kraken_balance, place_market_order
from .market_service import fetch_prices
from .telegram_notifier import send_telegram

load_dotenv()

logger = logging.getLogger(__name__)

_MIN_ORDER_USD = 5.00
_PROJECT_ROOT = Path(__file__).parent.parent.parent
_DIVERGENCE_FILE = _PROJECT_ROOT / "data" / "kraken_divergence.json"
_KRAKEN_ASSET_TO_PAIR = {
    "XXBT":  "BTC/USD",
    "XETH":  "ETH/USD",
    "XXMR":  "XMR/USD",
    "SOL":   "SOL/USD",
    "ADA":   "ADA/USD",
    "DOT":   "DOT/USD",
    "LINK":  "LINK/USD",
    "AVAX":  "AVAX/USD",
}


def mirror_tilt_to_kraken(
    sell_pair: str,
    sell_usd: float,
    buy_pair: str,
    buy_usd: float,
    sell_held_units: float | None = None,
) -> None:
    """Mirror a sim tilt trade to the live Kraken exchange.

    This is the safety layer between the tilt function and live order placement.
    All guards are enforced before any API call is made. The sim trade is assumed
    to have already executed before this function is called.

    Safety checks (enforced in this order):
    1. ``KRAKEN_LIVE_ENABLED`` env var must be ``"true"`` (case-insensitive).
    2. Total portfolio value (ZUSD + crypto holdings at live prices) must exceed
       ``KRAKEN_STOP_LOSS_USD`` (default ``4000.00``).
    3. Both scaled order sizes must be >= $5.00.

    On any Kraken failure the error is logged at ERROR level and the function
    returns silently — it never raises.

    Args:
        sell_pair: Canonical pair to sell, e.g. ``"SOL/USD"``.
        sell_usd:  Sim USD value of the sell.
        buy_pair:  Canonical pair to buy, e.g. ``"BTC/USD"``.
        buy_usd:   Sim USD value of the buy.
        sell_held_units: Actual units held on Kraken for the sell asset (optional).
                         Passed through to ``place_market_order()`` as ``held_units``
                         after scaling by ``KRAKEN_SIZING_PCT``.
    """
    # Guard 1: live trading must be explicitly enabled
    live_enabled = os.environ.get("KRAKEN_LIVE_ENABLED", "false").strip().lower()
    if live_enabled != "true":
        logger.info("Kraken mirror disabled — skipping")
        return

    try:
        # Guard 2: stop loss floor — check total portfolio value
        stop_loss_usd = float(os.environ.get("KRAKEN_STOP_LOSS_USD", "4000.00"))
        balances = get_kraken_balance()
        zusd = balances.get("ZUSD", 0.0)

        # Value crypto holdings at live prices
        crypto_value = 0.0
        pairs_to_price = []
        asset_amounts = {}
        for asset, amount in balances.items():
            if asset == "ZUSD" or amount <= 0:
                continue
            pair = _KRAKEN_ASSET_TO_PAIR.get(asset)
            if not pair:
                logger.debug("Unknown asset %s — skipping in portfolio valuation", asset)
                continue
            pairs_to_price.append(pair)
            asset_amounts[pair] = amount

        if pairs_to_price:
            live_prices = fetch_prices(pairs_to_price)
            for pair, amount in asset_amounts.items():
                price = live_prices.get(pair)
                if price is None:
                    logger.warning("No price for %s — excluding from portfolio value", pair)
                    continue
                crypto_value += amount * price

        total_portfolio_value = zusd + crypto_value
        logger.info(
            "Portfolio value: $%.2f (ZUSD: $%.2f + crypto: $%.2f)  floor: $%.2f",
            total_portfolio_value, zusd, crypto_value, stop_loss_usd,
        )
        if total_portfolio_value <= stop_loss_usd:
            logger.error(
                "STOP LOSS FLOOR HIT — halting Kraken execution  "
                "balance=%.2f  floor=%.2f",
                total_portfolio_value,
                stop_loss_usd,
            )
            return

        # Guard 3: scale order sizes by KRAKEN_SIZING_PCT
        sizing_pct = float(os.environ.get("KRAKEN_SIZING_PCT", "0.25"))
        real_sell_usd = sell_usd * sizing_pct
        real_buy_usd = buy_usd * sizing_pct
        real_held_units = round(sell_held_units * sizing_pct, 8) if sell_held_units else None

        if real_sell_usd < _MIN_ORDER_USD or real_buy_usd < _MIN_ORDER_USD:
            logger.info(
                "Order too small — skipping  "
                "sell=%.2f  buy=%.2f  min=%.2f",
                real_sell_usd,
                real_buy_usd,
                _MIN_ORDER_USD,
            )
            return

        # Execute: sell first, then buy
        sell_executed = False
        sell_result = place_market_order(sell_pair, "sell", real_sell_usd, held_units=real_held_units)
        sell_executed = True
        logger.info(
            "Kraken sell executed: pair=%s  usd=%.2f  result=%s",
            sell_pair,
            real_sell_usd,
            sell_result,
        )

        try:
            try:
                buy_result = place_market_order(buy_pair, "buy", real_buy_usd)
            except Exception as exc:
                logger.warning(
                    "Buy failed on first attempt — retrying in 5s: %s", exc
                )
                time.sleep(5)
                buy_result = place_market_order(buy_pair, "buy", real_buy_usd)
                logger.info("Buy succeeded on retry")
        except Exception as buy_exc:
            logger.critical(
                "ORPHANED SELL — sell executed but buy failed after retry: "
                "sell=%s  buy=%s  error=%s",
                sell_pair,
                buy_pair,
                buy_exc,
            )
            _DIVERGENCE_FILE.parent.mkdir(parents=True, exist_ok=True)
            _DIVERGENCE_FILE.write_text(
                json.dumps(
                    {
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "type": "orphaned_sell",
                        "sell_pair": sell_pair,
                        "sell_usd": real_sell_usd,
                        "buy_pair": buy_pair,
                        "buy_usd": real_buy_usd,
                        "error": str(buy_exc),
                        "resolved": False,
                    },
                    indent=2,
                )
            )
            send_telegram(
                f"🚨 <b>ORPHANED SELL DETECTED</b>\n"
                f"Sell executed: <b>${real_sell_usd:.2f} of {sell_pair}</b>\n"
                f"Buy FAILED after retry: <b>{buy_pair}</b>\n"
                f"Error: {buy_exc}\n\n"
                f"⚠️ Check Kraken Pro — you have orphaned USD\n"
                f"File: data/kraken_divergence.json\n"
                f"Manual action may be required"
            )
            return

        logger.info(
            "Kraken buy executed: pair=%s  usd=%.2f  result=%s",
            buy_pair,
            real_buy_usd,
            buy_result,
        )

        logger.info(
            "Kraken tilt mirror complete — sold %s $%.2f → bought %s $%.2f  (sizing=%.0f%%)",
            sell_pair,
            real_sell_usd,
            buy_pair,
            real_buy_usd,
            sizing_pct * 100,
        )

    except Exception as exc:
        logger.error(
            "Kraken execution failed — sell=%s  buy=%s  error=%s",
            sell_pair,
            buy_pair,
            exc,
        )
