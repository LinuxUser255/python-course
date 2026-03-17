#!/usr/bin/env python3

# ============================================================
#  🐍 LESSON: Dictionaries
#  Inspired by kraken_executor.py
# ============================================================
# The real kraken_executor.py is built almost entirely on
# dictionaries. Every balance, every asset, every price lookup
# is a dict. This lesson walks through that same thinking
# at a beginner-friendly pace.
# ============================================================


# ============================================================
#  PART 1 — Declaring Dictionaries
#
#  In the real executor, this dict maps Kraken's internal
#  asset codes to human-readable trading pairs:
#
#  _KRAKEN_ASSET_TO_PAIR = {
#      "XXBT":  "BTC/USD",
#      "XETH":  "ETH/USD",
#      ...
#  }
#
#  Key   → Kraken's internal code  (what the API sends back)
#  Value → The pair we recognise   (what humans use)
# ============================================================

def declare_dicts():
    # Pre-populated — data defined upfront
    asset_to_pair = {
        "XXBT": "BTC/USD",
        "XETH": "ETH/USD",
        "SOL":  "SOL/USD",
        "ADA":  "ADA/USD",
    }
    print(asset_to_pair)

    # Empty — built up over time (e.g. as balances come in)
    balances = {}
    balances["XXBT"] = 0.012
    balances["XETH"] = 1.5
    balances["ZUSD"] = 1_500.00
    print(balances)


# ============================================================
#  PART 2 — Accessing Values
#
#  The executor looks up a pair like this:
#      pair = _KRAKEN_ASSET_TO_PAIR.get(asset)
#
#  Two ways to access a value — knowing the difference matters.
# ============================================================

def accessing_values():
    asset_to_pair = {
        "XXBT": "BTC/USD",
        "XETH": "ETH/USD",
        "SOL":  "SOL/USD",
    }

    # Square bracket access — raises KeyError if key missing
    print(asset_to_pair["XXBT"])        # "BTC/USD"

    # .get() — returns None (or a default) if key missing
    # The real executor uses this because not every asset
    # is in the map — unknown assets should be skipped safely.
    print(asset_to_pair.get("SOL"))     # "SOL/USD"
    print(asset_to_pair.get("DOGE"))    # None  ← no crash!
    print(asset_to_pair.get("DOGE", "Unknown pair"))  # safe default


# ============================================================
#  PART 3 — Nested Dictionaries
#
#  The executor's balances dict is flat, but the portfolio
#  valuation builds a richer nested structure internally.
#  Here's a simplified version showing nested dicts.
# ============================================================

def nested_dicts():
    portfolio = {
        "XXBT": {
            "pair":   "BTC/USD",
            "amount": 0.012,
            "price":  62_000.00,
        },
        "XETH": {
            "pair":   "ETH/USD",
            "amount": 1.5,
            "price":  3_100.00,
        },
        "ZUSD": {
            "pair":   None,
            "amount": 1_500.00,
            "price":  1.00,
        },
    }

    # Access the BTC price — chain the keys
    print(portfolio["XXBT"]["price"])           # 62000.0

    # Access ETH amount
    print(portfolio["XETH"]["amount"])          # 1.5

    # Calculate the USD value of one asset
    btc = portfolio["XXBT"]
    btc_value = btc["amount"] * btc["price"]
    print(f"BTC value: ${btc_value:,.2f}")      # $744.00


# ============================================================
#  PART 4 — .keys(), .values(), .items()
#
#  The executor iterates over balances like this:
#      for asset, amount in balances.items():
#
#  This is the most common pattern in the entire file.
# ============================================================

def view_objects():
    balances = {
        "ZUSD": 1_500.00,
        "XXBT": 0.012,
        "XETH": 1.5,
        "SOL":  10.0,
    }

    print(balances.keys())    # all asset codes
    print(balances.values())  # all amounts
    print(balances.items())   # both together as tuples


# ============================================================
#  PART 5 — Iterating + in / not in
#
#  The real executor loops over balances and skips ZUSD,
#  skips zero amounts, and skips unknown assets:
#
#      for asset, amount in balances.items():
#          if asset == "ZUSD" or amount <= 0:
#              continue
#          pair = _KRAKEN_ASSET_TO_PAIR.get(asset)
#          if not pair:
#              continue
# ============================================================

def iterate_and_check():
    asset_to_pair = {
        "XXBT": "BTC/USD",
        "XETH": "ETH/USD",
        "SOL":  "SOL/USD",
    }

    balances = {
        "ZUSD": 1_500.00,
        "XXBT": 0.012,
        "XETH": 0.0,        # zero balance — skip
        "SOL":  10.0,
        "DOGE": 500.0,      # not in our asset map — skip
    }

    fake_prices = {
        "BTC/USD": 62_000.00,
        "ETH/USD":  3_100.00,
        "SOL/USD":    150.00,
    }

    crypto_value = 0.0

    # `balances.items()` - Returns a view object containing key-value pairs as tuples:
    # `for asset, amount in ...` - Unpacks each tuple into two variables:
    # asset = the dictionary key (e.g., "ZUSD", "XXBT")
    # amount = the dictionary value (e.g., 1500.00, 0.012)
    # `.items()`: You get both keys AND values simultaneously,
    for asset, amount in balances.items():
        if asset == "ZUSD" or amount <= 0:
            continue

        pair = asset_to_pair.get(asset)
        # defensive programming technique
        # using guard clause pattern, validate data before proceeding
        if not pair:
            print(f"⚠️  Unknown asset: {asset} — skipping")
            continue

        price = fake_prices.get(pair, 0.0)
        value = amount * price
        crypto_value += value
        print(f"  {asset} → {pair}:  {amount} units × ${price:,.2f} = ${value:,.2f}")

    zusd = balances.get("ZUSD", 0.0)
    total = zusd + crypto_value
    #         💰 Cash:          $1,500.00
    print(f"\n💰 Cash:          ${zusd:,.2f}")
    print(f"📈 Crypto value:  ${crypto_value:,.2f}")
    print(f"🏦 Total portfolio: ${total:,.2f}")


# ============================================================
#  PART 6 — Updating and Deleting
#
#  The executor updates balances after trades execute.
#  .update() merges a whole dict in one shot.
# ============================================================

def update_and_delete():
    balances = {
        "ZUSD": 1500.00,
        "XXBT": 0.012,
        "XETH": 1.5,
    }

    # Single update — price of BTC changed our USD balance
    balances["ZUSD"] = 1_000.00
    print(balances["ZUSD"])         # 1000.0

    # Bulk update — trade executed, multiple balances changed
    post_trade = {
        "ZUSD": 500.00,
        "XXBT": 0.020,
        "SOL":  5.0,                # new asset added
    }
    balances.update(post_trade)
    print(balances)

    # Delete — asset fully sold, remove it
    del balances["XETH"]
    print(balances)


# ============================================================
#  🏋️  CHALLENGE — Build a Mini Portfolio Valuator
#
#  Using only what you've learned above, complete this program.
#
#  You are given:
#    - asset_to_pair  (asset code → trading pair)
#    - balances       (asset code → units held)
#    - prices         (trading pair → current USD price)
#
#  Your tasks:
#  1. Loop over balances using .items()
#  2. Skip ZUSD and any asset with amount <= 0
#  3. Look up the pair using asset_to_pair.get()
#  4. Skip any asset not found in asset_to_pair
#  5. Look up the price using prices.get()
#  6. Calculate: value = amount * price
#  7. Add to a running total called crypto_value
#  8. Print each line like:
#       SOL  →  SOL/USD:  10.0 units × $150.00 = $1,500.00
#  9. After the loop print the total portfolio value
#     (ZUSD balance + crypto_value)
#
#  BONUS:
#  - Add a stop loss check: if total portfolio value drops
#    below stop_loss_floor, print a warning and return early.
#  - Add a new asset "LINK" to asset_to_pair after declaring it.
#  - Remove "ADA" from balances before the loop runs.
# ============================================================

def portfolio_challenge():
    asset_to_pair = {
        "XXBT": "BTC/USD",
        "XETH": "ETH/USD",
        "SOL":  "SOL/USD",
        "ADA":  "ADA/USD",
    }

    balances = {
        "ZUSD": 2_000.00,
        "XXBT": 0.05,
        "XETH": 2.0,
        "SOL":  10.0,
        "ADA":  250.0,
        "DOGE": 1_000.0,    # not in asset_to_pair — should be skipped
        "XETH2": 0.0,       # zero balance — should be skipped
    }

    prices = {
        "BTC/USD": 62_000.00,
        "ETH/USD":  3_100.00,
        "SOL/USD":    150.00,
        "ADA/USD":      0.45,
    }

    stop_loss_floor = 4_000.00

    # YOUR CODE HERE
#    ???


def main():
    print("=" * 50)
    print("PART 1 — Declaring Dicts")
    declare_dicts()

    print("\nPART 2 — Accessing Values")
    accessing_values()

    print("\nPART 3 — Nested Dicts")
    nested_dicts()

    print("\nPART 4 — View Objects")
    view_objects()

    print("\nPART 5 — Iterating + in / not in")
    iterate_and_check()

    print("\nPART 6 — Update and Delete")
    update_and_delete()

    print("\n🏋️  CHALLENGE")
    portfolio_challenge()


if __name__ == "__main__":
    main()
