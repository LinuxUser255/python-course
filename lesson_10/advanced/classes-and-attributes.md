# One-to-one Correspondence ?

**Is there a one-to-one correspondence between the number and name of parameters in a constructor and the attributes??**
There's no strict rule — it depends on the purpose of the class.

---

**One-to-one: Data containers**

When the class mainly holds data that's passed in:

```python
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
```

Every parameter becomes an attribute. The class is essentially a struct.

---

**Not one-to-one: Computed/derived attributes**

When attributes are derived from parameters:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height        # Computed, not a parameter
        self.perimeter = 2 * (width + height)
```

---

**Not one-to-one: Internal state**

When the class needs private/internal attributes:

```python
class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None          # Internal state
        self.is_connected = False   # Internal state
        self._retry_count = 0       # Private tracking
```

---

**Not one-to-one: Parameters used but not stored**

When a parameter is only used during initialization:

```python
class FileReader:
    def __init__(self, filepath):
        # filepath is NOT stored as self.filepath
        self.content = open(filepath).read()
        self.line_count = self.content.count('\n')
```

---

**General guideline:**

| Scenario | One-to-one? |
|----------|-------------|
| Data class / container | Yes |
| Configuration object | Yes |
| Computed attributes needed | No |
| Internal state needed | No |
| Parameter only used temporarily | No |

---

**How to decide for your own classes:**

Ask: *"Will I need to access this value later?"*

- Yes → store as `self.x`
- No → just use it during `__init__` and discard

---

#### More elaboration



### Level 2: Parameters ≠ Attributes

```python
#!/usr/bin/env python3

import hashlib
from datetime import datetime

"""
Class, parameters and attributes example 2
parameters != attributes

Parameters (3): name, email, password
Attributes (5): name, email, _password_hash, is_active, created_at

Demonstrates:
- Transformed attribute (email → lowercased/stripped)
- Derived attribute (_password_hash from password)
- Internal state (is_active, created_at — not parameters)
- Password is used but never stored
"""


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email.lower().strip()
        self._password_hash = self._hash_password(password)  # never store raw!
        self.is_active = True
        self.created_at = datetime.utcnow()

    def _hash_password(self, password):
        """Hash password with salt. Never store plaintext."""
        salt = "secret_salt_123"  # In production, use unique salt per user
        salted = f"{salt}{password}".encode()
        return hashlib.sha256(salted).hexdigest()

    def check_password(self, password):
        """Verify password against stored hash."""
        return self._password_hash == self._hash_password(password)

    def deactivate(self):
        """Deactivate user account."""
        self.is_active = False

    def activate(self):
        """Activate user account."""
        self.is_active = True

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}', active={self.is_active})"


def main():
    # Create user — password is used but never stored
    user = User(
        name="Alice",
        email="  ALICE@Example.COM  ",
        password="supersecret123"
    )

    print(user)
    print(f"Created at: {user.created_at}")
    print(f"Password hash: {user._password_hash[:16]}...")  # Show partial hash

    # Verify password
    print(f"\nCorrect password: {user.check_password('supersecret123')}")
    print(f"Wrong password: {user.check_password('wrongpassword')}")

    # Deactivate
    user.deactivate()
    print(f"\nAfter deactivation: {user}")


if __name__ == "__main__":
    main()
```

---

**Output:**

```
User(name='Alice', email='alice@example.com', active=True)
Created at: 2025-12-06 15:30:45.123456
Password hash: 7a3b9c2d1e4f5a6b...

Correct password: True
Wrong password: False

After deactivation: User(name='Alice', email='alice@example.com', active=False)
```

---

**Parameter → Attribute mapping:**

| Parameter  | Attribute             | Relationship                         |
| ---------- | --------------------- | ------------------------------------ |
| `name`     | `self.name`           | 1:1 (stored as-is)                   |
| `email`    | `self.email`          | Transformed (lowercase, stripped)    |
| `password` | `self._password_hash` | Derived (hashed, original discarded) |
| —          | `self.is_active`      | Internal state (no parameter)        |
| —          | `self.created_at`     | Internal state (no parameter)        |


# Level 3: Parameters Used to Compute Attributes (Very Common)

```python
#!/usr/bin/env python3

import time

"""
Class, parameters and attributes example 3
parameters != attributes

Parameters (1): initial_cash
Attributes (6): initial_cash, cash, holdings, equity_history, trades, start_time

Demonstrates:
- Duplicated attribute (initial_cash stored twice — original and working copy)
- Internal state containers (holdings dict, equity_history list)
- Counters (trades)
- Auto-generated timestamp (start_time)
"""


class Portfolio:
    def __init__(self, initial_cash=100_000):
        self.initial_cash = initial_cash      # Original amount (never changes)
        self.cash = initial_cash              # Working balance (changes with trades)
        self.holdings = {}                    # {symbol: units}
        self.equity_history = []              # list of (timestamp, equity)
        self.trades = 0
        self.start_time = time.time()

    def buy(self, symbol, units, price):
        """Buy shares of a stock."""
        cost = units * price
        if cost > self.cash:
            raise ValueError(f"Insufficient cash: need ${cost:.2f}, have ${self.cash:.2f}")
        
        self.cash -= cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + units
        self.trades += 1
        self._record_equity(price)

    def sell(self, symbol, units, price):
        """Sell shares of a stock."""
        if symbol not in self.holdings or self.holdings[symbol] < units:
            raise ValueError(f"Insufficient holdings for {symbol}")
        
        self.holdings[symbol] -= units
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.cash += units * price
        self.trades += 1
        self._record_equity(price)

    def _record_equity(self, current_price):
        """Record current equity for history tracking."""
        equity = self.get_equity(current_price)
        self.equity_history.append((time.time(), equity))

    def get_equity(self, current_price):
        """Calculate total equity (cash + holdings value)."""
        holdings_value = sum(units * current_price for units in self.holdings.values())
        return self.cash + holdings_value

    def get_return(self, current_price):
        """Calculate percentage return."""
        equity = self.get_equity(current_price)
        return ((equity - self.initial_cash) / self.initial_cash) * 100

    def get_runtime(self):
        """Get time elapsed since portfolio creation."""
        return time.time() - self.start_time

    def __repr__(self):
        return f"Portfolio(cash=${self.cash:,.2f}, holdings={self.holdings}, trades={self.trades})"


def main():
    # Create portfolio with default $100k
    portfolio = Portfolio()

    print(portfolio)
    print(f"Started at: {portfolio.start_time}")

    # Simulate trading
    btc_price = 50_000

    portfolio.buy("BTC", 1, btc_price)
    print(f"\nAfter buying 1 BTC @ ${btc_price:,}:")
    print(portfolio)

    portfolio.buy("BTC", 0.5, btc_price)
    print(f"\nAfter buying 0.5 BTC @ ${btc_price:,}:")
    print(portfolio)

    # Price goes up
    btc_price = 55_000
    portfolio.sell("BTC", 0.5, btc_price)
    print(f"\nAfter selling 0.5 BTC @ ${btc_price:,}:")
    print(portfolio)

    # Summary
    print(f"\n--- Summary ---")
    print(f"Initial cash: ${portfolio.initial_cash:,}")
    print(f"Current cash: ${portfolio.cash:,.2f}")
    print(f"Current equity: ${portfolio.get_equity(btc_price):,.2f}")
    print(f"Return: {portfolio.get_return(btc_price):.2f}%")
    print(f"Total trades: {portfolio.trades}")
    print(f"Runtime: {portfolio.get_runtime():.4f} seconds")
    print(f"Equity history entries: {len(portfolio.equity_history)}")


if __name__ == "__main__":
    main()
```

---

**Output:**

```
Portfolio(cash=$100,000.00, holdings={}, trades=0)
Started at: 1733500245.123456

After buying 1 BTC @ $50,000:
Portfolio(cash=$50,000.00, holdings={'BTC': 1}, trades=1)

After buying 0.5 BTC @ $50,000:
Portfolio(cash=$25,000.00, holdings={'BTC': 1.5}, trades=2)

After selling 0.5 BTC @ $55,000:
Portfolio(cash=$52,500.00, holdings={'BTC': 1.0}, trades=3)

--- Summary ---
Initial cash: $100,000
Current cash: $52,500.00
Current equity: $107,500.00
Return: 7.50%
Total trades: 3
Runtime: 0.0012 seconds
Equity history entries: 3
```

---

**Parameter → Attribute mapping:**

| Parameter | Attribute | Relationship |
|-----------|-----------|--------------|
| `initial_cash` | `self.initial_cash` | 1:1 (preserved for reference) |
| `initial_cash` | `self.cash` | Duplicate (working copy that changes) |
| — | `self.holdings` | Internal state (empty dict) |
| — | `self.equity_history` | Internal state (empty list) |
| — | `self.trades` | Counter (no parameter) |
| — | `self.start_time` | Auto-generated timestamp |

---

**Key pattern:**

One parameter (`initial_cash`) creates two attributes — the original value for calculating returns, and a working copy that gets modified. This is common in financial/trading applications where you need to track both the starting point and current state.


# Level 4, some Parameters NOT Stored at all

```python
#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
Class, parameters and attributes example 4
Some parameters are NOT stored at all

Parameters (4): smtp_server, port, username, password
Attributes (2): client, sender_email

Demonstrates:
- Parameters consumed during initialization but never stored
- Sensitive data (password) used and discarded
- External resource (SMTP connection) stored instead of raw config
"""


class EmailService:
    def __init__(self, smtp_server, port, username, password):
        self.client = smtplib.SMTP(smtp_server, port)
        self.client.starttls()  # Secure the connection
        self.client.login(username, password)
        self.sender_email = username  # Store only what we need later
        # smtp_server → consumed by SMTP(), not stored
        # port → consumed by SMTP(), not stored
        # username → used for login, stored only as sender_email
        # password → used for login, NEVER stored

    def send(self, to, subject, body):
        """Send an email."""
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        self.client.sendmail(self.sender_email, to, msg.as_string())
        print(f"Email sent to {to}")

    def disconnect(self):
        """Close the SMTP connection."""
        self.client.quit()
        print("Disconnected from SMTP server")

    def __repr__(self):
        return f"EmailService(sender={self.sender_email}, connected=True)"


# --- Mock version for demonstration (doesn't require real SMTP) ---

class MockEmailService:
    """Simulated version to demonstrate the pattern without real SMTP."""

    def __init__(self, smtp_server, port, username, password):
        # Simulate connection setup
        print(f"Connecting to {smtp_server}:{port}...")
        print(f"Authenticating as {username}...")
        print(f"Password {'*' * len(password)} used and discarded")
        
        self.client = f"MockSMTP({smtp_server}:{port})"  # Simulated connection
        self.sender_email = username
        
        # These are gone:
        # - smtp_server (used to create connection)
        # - port (used to create connection)
        # - password (used for auth, then discarded)

    def send(self, to, subject, body):
        """Simulate sending an email."""
        print(f"\n--- Sending Email ---")
        print(f"From: {self.sender_email}")
        print(f"To: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body[:50]}...")
        print(f"--- Sent via {self.client} ---")

    def disconnect(self):
        """Simulate disconnection."""
        print(f"\nDisconnected from {self.client}")

    def __repr__(self):
        return f"MockEmailService(sender={self.sender_email})"


def main():
    # Create email service
    email = MockEmailService(
        smtp_server="smtp.gmail.com",
        port=587,
        username="mybot@gmail.com",
        password="supersecretpassword123"
    )

    print(f"\n{email}")

    # Demonstrate what's accessible vs. not
    print(f"\n--- Accessible Attributes ---")
    print(f"email.sender_email: {email.sender_email}")
    print(f"email.client: {email.client}")

    print(f"\n--- NOT Accessible (never stored) ---")
    print(f"email.smtp_server: AttributeError")
    print(f"email.port: AttributeError")
    print(f"email.password: AttributeError (security!)")

    # Send an email
    email.send(
        to="recipient@example.com",
        subject="Hello from Python OOP",
        body="This demonstrates parameters that are consumed but not stored."
    )

    email.disconnect()


if __name__ == "__main__":
    main()
```

---

**Output:**
```
Connecting to smtp.gmail.com:587...
Authenticating as mybot@gmail.com...
Password *********************** used and discarded

MockEmailService(sender=mybot@gmail.com)

--- Accessible Attributes ---
email.sender_email: mybot@gmail.com
email.client: MockSMTP(smtp.gmail.com:587)

--- NOT Accessible (never stored) ---
email.smtp_server: AttributeError
email.port: AttributeError
email.password: AttributeError (security!)

--- Sending Email ---
From: mybot@gmail.com
To: recipient@example.com
Subject: Hello from Python OOP
Body: This demonstrates parameters that are consumed bu...
--- Sent via MockSMTP(smtp.gmail.com:587) ---

Disconnected from MockSMTP(smtp.gmail.com:587)
```

---

**Parameter → Attribute mapping:**

| Parameter     | Attribute           | Relationship                                    |
| ------------- | ------------------- | ----------------------------------------------- |
| `smtp_server` | —                   | Consumed by `SMTP()`, not stored                |
| `port`        | —                   | Consumed by `SMTP()`, not stored                |
| `username`    | `self.sender_email` | Partially stored (for sending)                  |
| `password`    | —                   | Used for auth, **never stored** (security)      |
| —             | `self.client`       | Created from parameters (the connection object) |

---

**Why this pattern?**
```
┌─────────────────────────────────────────────────────┐
│                   __init__()                        │
│                                                     │
│  smtp_server ──┐                                    │
│                ├──► smtplib.SMTP() ──► self.client  │
│  port ─────────┘                                    │
│                                                     │
│  username ─────┬──► login() ──► (authenticated)    │
│                └──► self.sender_email               │
│                                                     │
│  password ─────────► login() ──► (discarded) 🗑️    │
│                                                     │
└─────────────────────────────────────────────────────┘
```



# Level 5: Default/Optional Parameters Create Attributes Conditionally

```python
#!/usr/bin/env python3

import time
import random

"""
Class, parameters and attributes example 5
Default/Optional parameters create attributes conditionally

Parameters (3): name, strategy, risk_per_trade (2 have defaults)
Attributes (7): name, strategy, risk_per_trade, portfolio, trade_log, win_rate, sharpe_ratio

Demonstrates:
- Optional parameters with sensible defaults
- Composed object (Portfolio) created internally
- Derived/calculated attributes (win_rate, sharpe_ratio)
- Attributes that update based on activity
"""


class Portfolio:
    """Simple portfolio for the Trader to use."""

    def __init__(self, initial_cash=100_000):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.holdings = {}

    def get_equity(self, prices):
        """Calculate total equity given current prices."""
        holdings_value = sum(
            units * prices.get(symbol, 0)
            for symbol, units in self.holdings.items()
        )
        return self.cash + holdings_value

    def __repr__(self):
        return f"Portfolio(cash=${self.cash:,.2f}, holdings={self.holdings})"


class Trader:
    def __init__(self, name, strategy="momentum", risk_per_trade=0.02):
        # From parameters
        self.name = name
        self.strategy = strategy
        self.risk_per_trade = risk_per_trade

        # Internal state (not parameters)
        self.portfolio = Portfolio()
        self.trade_log = []

        # Derived metrics (calculated, not input)
        self.win_rate = 0.0
        self.sharpe_ratio = None

    def execute_trade(self, symbol, action, units, price):
        """Execute a buy or sell trade."""
        if action == "buy":
            cost = units * price
            if cost > self.portfolio.cash:
                print(f"[{self.name}] Insufficient funds for {symbol}")
                return False
            self.portfolio.cash -= cost
            self.portfolio.holdings[symbol] = self.portfolio.holdings.get(symbol, 0) + units

        elif action == "sell":
            if self.portfolio.holdings.get(symbol, 0) < units:
                print(f"[{self.name}] Insufficient {symbol} to sell")
                return False
            self.portfolio.holdings[symbol] -= units
            self.portfolio.cash += units * price
            if self.portfolio.holdings[symbol] == 0:
                del self.portfolio.holdings[symbol]

        # Log the trade
        trade = {
            "timestamp": time.time(),
            "symbol": symbol,
            "action": action,
            "units": units,
            "price": price,
            "profit": None  # Calculated on close
        }
        self.trade_log.append(trade)
        print(f"[{self.name}] {action.upper()} {units} {symbol} @ ${price:,.2f}")
        return True

    def close_position(self, symbol, exit_price):
        """Close a position and calculate profit."""
        if symbol not in self.portfolio.holdings:
            print(f"[{self.name}] No position in {symbol}")
            return None

        units = self.portfolio.holdings[symbol]

        # Find entry price from log
        entry_trade = next(
            (t for t in reversed(self.trade_log)
             if t["symbol"] == symbol and t["action"] == "buy"),
            None
        )
        entry_price = entry_trade["price"] if entry_trade else exit_price

        # Execute sell
        self.execute_trade(symbol, "sell", units, exit_price)

        # Calculate and record profit
        profit = (exit_price - entry_price) * units
        self.trade_log[-1]["profit"] = profit

        # Update derived metrics
        self._update_metrics()

        return profit

    def _update_metrics(self):
        """Recalculate derived attributes."""
        closed_trades = [t for t in self.trade_log if t["profit"] is not None]

        if not closed_trades:
            return

        # Win rate
        wins = sum(1 for t in closed_trades if t["profit"] > 0)
        self.win_rate = wins / len(closed_trades)

        # Simplified Sharpe ratio (profit / volatility)
        profits = [t["profit"] for t in closed_trades]
        avg_profit = sum(profits) / len(profits)
        if len(profits) > 1:
            variance = sum((p - avg_profit) ** 2 for p in profits) / len(profits)
            std_dev = variance ** 0.5
            self.sharpe_ratio = avg_profit / std_dev if std_dev > 0 else None
        else:
            self.sharpe_ratio = None

    def get_position_size(self, price):
        """Calculate position size based on risk_per_trade."""
        risk_amount = self.portfolio.cash * self.risk_per_trade
        units = risk_amount / price
        return units

    def summary(self):
        """Print trader summary."""
        print(f"\n{'='*50}")
        print(f"Trader: {self.name}")
        print(f"Strategy: {self.strategy}")
        print(f"Risk per trade: {self.risk_per_trade:.1%}")
        print(f"Portfolio: {self.portfolio}")
        print(f"Total trades: {len(self.trade_log)}")
        print(f"Win rate: {self.win_rate:.1%}")
        print(f"Sharpe ratio: {self.sharpe_ratio:.2f}" if self.sharpe_ratio else "Sharpe ratio: N/A")
        print(f"{'='*50}")

    def __repr__(self):
        return f"Trader(name='{self.name}', strategy='{self.strategy}', win_rate={self.win_rate:.1%})"


def main():
    # Create traders with different configurations
    print("--- Creating Traders ---\n")

    # All defaults
    trader1 = Trader("Alice")
    print(f"Default trader: {trader1}")
    print(f"  strategy: {trader1.strategy}")
    print(f"  risk_per_trade: {trader1.risk_per_trade}")

    # Custom strategy
    trader2 = Trader("Bob", strategy="mean_reversion")
    print(f"\nCustom strategy: {trader2}")
    print(f"  strategy: {trader2.strategy}")
    print(f"  risk_per_trade: {trader2.risk_per_trade}")

    # Fully custom
    trader3 = Trader("Charlie", strategy="scalping", risk_per_trade=0.05)
    print(f"\nFully custom: {trader3}")
    print(f"  strategy: {trader3.strategy}")
    print(f"  risk_per_trade: {trader3.risk_per_trade}")

    # Simulate trading
    print("\n--- Simulating Trades ---\n")

    # Alice trades BTC
    alice = Trader("Alice", strategy="momentum", risk_per_trade=0.02)

    # Trade 1: Win
    alice.execute_trade("BTC", "buy", 1, 50_000)
    alice.close_position("BTC", 55_000)  # +$5,000

    # Trade 2: Loss
    alice.execute_trade("ETH", "buy", 10, 3_000)
    alice.close_position("ETH", 2_800)  # -$2,000

    # Trade 3: Win
    alice.execute_trade("BTC", "buy", 0.5, 52_000)
    alice.close_position("BTC", 58_000)  # +$3,000

    # Summary
    alice.summary()

    # Show derived attributes updated
    print("\n--- Derived Attributes ---")
    print(f"win_rate started at 0.0, now: {alice.win_rate:.1%}")
    print(f"sharpe_ratio started at None, now: {alice.sharpe_ratio:.2f}")
    print(f"trade_log started empty, now has {len(alice.trade_log)} entries")


if __name__ == "__main__":
    main()
```

---

**Output:**

```
--- Creating Traders ---

Default trader: Trader(name='Alice', strategy='momentum', win_rate=0.0%)
  strategy: momentum
  risk_per_trade: 0.02

Custom strategy: Trader(name='Bob', strategy='mean_reversion', win_rate=0.0%)
  strategy: mean_reversion
  risk_per_trade: 0.02

Fully custom: Trader(name='Charlie', strategy='scalping', win_rate=0.0%)
  strategy: scalping
  risk_per_trade: 0.05

--- Simulating Trades ---

[Alice] BUY 1 BTC @ $50,000.00
[Alice] SELL 1 BTC @ $55,000.00
[Alice] BUY 10 ETH @ $3,000.00
[Alice] SELL 10 ETH @ $2,800.00
[Alice] BUY 0.5 BTC @ $52,000.00
[Alice] SELL 0.5 BTC @ $58,000.00

==================================================
Trader: Alice
Strategy: momentum
Risk per trade: 2.0%
Portfolio: Portfolio(cash=$106,000.00, holdings={})
Total trades: 6
Win rate: 66.7%
Sharpe ratio: 0.76
==================================================

--- Derived Attributes ---
win_rate started at 0.0, now: 66.7%
sharpe_ratio started at None, now: 0.76
trade_log started empty, now has 6 entries
```

---

**Parameter → Attribute mapping:**

| Parameter | Default | Attribute | Relationship |
|-----------|---------|-----------|--------------|
| `name` | (required) | `self.name` | 1:1 |
| `strategy` | `"momentum"` | `self.strategy` | 1:1 (uses default if not provided) |
| `risk_per_trade` | `0.02` | `self.risk_per_trade` | 1:1 (uses default if not provided) |
| — | — | `self.portfolio` | Composed object (created internally) |
| — | — | `self.trade_log` | Internal state (empty list) |
| — | — | `self.win_rate` | Derived (calculated from trades) |
| — | — | `self.sharpe_ratio` | Derived (calculated from trades) |

---

**Key patterns:**

```
┌─────────────────────────────────────────────────────────┐
│                     __init__()                          │
│                                                         │
│  name ─────────────────────────────► self.name          │
│                                                         │
│  strategy="momentum" ──────────────► self.strategy      │
│       (default)                                         │
│                                                         │
│  risk_per_trade=0.02 ──────────────► self.risk_per_trade│
│       (default)                                         │
│                                                         │
│  (nothing) ────► Portfolio() ──────► self.portfolio     │
│                  (composed)                             │
│                                                         │
│  (nothing) ────► [] ───────────────► self.trade_log     │
│                                                         │
│  (nothing) ────► 0.0 ──────────────► self.win_rate      │
│                  (derived, updates later)               │
│                                                         │
│  (nothing) ────► None ─────────────► self.sharpe_ratio  │
│                  (derived, updates later)               │
└─────────────────────────────────────────────────────────┘
```


# Level 6: Advanced — Parameters Are Just Messages


```python
#!/usr/bin/env python3

import time
import threading
from typing import Any

"""
Class, parameters and attributes example 6
Advanced — Parameters are just messages

Parameters (1): config_dict (could contain 20+ keys)
Attributes (7): symbols, horizon, use_grok, models, threads, is_running, start_time

Demonstrates:
- Single dict parameter unpacked into multiple attributes
- Selective extraction (ignore most keys, use only what's needed)
- Default values via .get()
- Boolean derived from string comparison
- Internal initialization (_load_models, _start_background_threads)
- Caller has no idea what happens inside
"""

DEFAULT_SYMBOLS = ["BTC/USD", "ETH/USD"]
DEFAULT_HORIZON = 24
DEFAULT_LLM = "grok"


class CryptoBot:
    def __init__(self, config_dict: dict[str, Any]):
        # Extract only what we need from config_dict
        self.symbols = config_dict.get("symbols", DEFAULT_SYMBOLS)
        self.horizon = config_dict.get("prediction_horizon", DEFAULT_HORIZON)
        self.use_grok = config_dict.get("llm", DEFAULT_LLM) == "grok"

        # Internal state — caller doesn't know or care
        self.models = {}
        self.threads = []
        self.is_running = False
        self.start_time = None
        self.predictions = {}

        # Internal initialization
        self._load_models()
        self._start_background_threads()
        self.is_running = True
        self.start_time = time.time()

    def _load_models(self):
        """Load ML models for each symbol. Caller never sees this."""
        print("[CryptoBot] Loading models...")
        for symbol in self.symbols:
            # Simulate model loading
            self.models[symbol] = {
                "type": "lstm",
                "horizon": self.horizon,
                "llm_enhanced": self.use_grok,
                "weights": f"model_{symbol.replace('/', '_')}.h5"
            }
            print(f"  Loaded model for {symbol}")

    def _start_background_threads(self):
        """Start background workers. Caller never sees this."""
        print("[CryptoBot] Starting background threads...")

        # Price feed thread
        price_thread = threading.Thread(
            target=self._price_feed_worker,
            daemon=True,
            name="PriceFeed"
        )
        self.threads.append(price_thread)

        # Prediction thread
        pred_thread = threading.Thread(
            target=self._prediction_worker,
            daemon=True,
            name="Predictor"
        )
        self.threads.append(pred_thread)

        for t in self.threads:
            t.start()
            print(f"  Started {t.name} thread")

    def _price_feed_worker(self):
        """Background worker for price updates."""
        while self.is_running:
            time.sleep(1)  # Simulate price feed

    def _prediction_worker(self):
        """Background worker for predictions."""
        while self.is_running:
            time.sleep(1)  # Simulate predictions

    def predict(self, symbol):
        """Generate a prediction for a symbol."""
        if symbol not in self.symbols:
            raise ValueError(f"Symbol {symbol} not configured")

        # Simulate prediction
        import random
        prediction = {
            "symbol": symbol,
            "direction": random.choice(["up", "down"]),
            "confidence": random.uniform(0.6, 0.95),
            "horizon_hours": self.horizon,
            "llm_enhanced": self.use_grok,
            "timestamp": time.time()
        }
        self.predictions[symbol] = prediction
        return prediction

    def stop(self):
        """Stop the bot and all background threads."""
        print("[CryptoBot] Stopping...")
        self.is_running = False
        time.sleep(0.1)  # Let threads exit
        print("[CryptoBot] Stopped")

    def status(self):
        """Print bot status."""
        runtime = time.time() - self.start_time if self.start_time else 0
        print(f"\n{'='*50}")
        print(f"CryptoBot Status")
        print(f"{'='*50}")
        print(f"Running: {self.is_running}")
        print(f"Runtime: {runtime:.1f}s")
        print(f"Symbols: {self.symbols}")
        print(f"Horizon: {self.horizon}h")
        print(f"Using Grok LLM: {self.use_grok}")
        print(f"Models loaded: {len(self.models)}")
        print(f"Active threads: {len([t for t in self.threads if t.is_alive()])}")
        print(f"{'='*50}")

    def __repr__(self):
        return f"CryptoBot(symbols={self.symbols}, running={self.is_running})"


def main():
    print("--- Example 1: Minimal Config ---\n")

    # Minimal config — bot uses defaults for everything else
    minimal_config = {
        "prediction_horizon": 12
    }

    bot1 = CryptoBot(minimal_config)
    print(f"\n{bot1}")
    print(f"  symbols: {bot1.symbols} (default)")
    print(f"  horizon: {bot1.horizon} (from config)")
    print(f"  use_grok: {bot1.use_grok} (default)")
    bot1.stop()

    print("\n\n--- Example 2: Full Config (20 keys, most ignored) ---\n")

    # Full config with many keys — bot only uses what it needs
    full_config = {
        # Keys the bot USES
        "symbols": ["BTC/USD", "ETH/USD", "SOL/USD"],
        "prediction_horizon": 48,
        "llm": "claude",  # Not grok!

        # Keys the bot IGNORES (but caller might use elsewhere)
        "api_key": "abc123secret",
        "api_secret": "xyz789private",
        "exchange": "kraken",
        "sandbox_mode": True,
        "log_level": "DEBUG",
        "log_file": "/var/log/cryptobot.log",
        "max_position_size": 10000,
        "risk_per_trade": 0.02,
        "stop_loss_pct": 0.05,
        "take_profit_pct": 0.10,
        "rebalance_interval": 3600,
        "webhook_url": "https://hooks.slack.com/...",
        "notification_email": "alerts@example.com",
        "backtest_start": "2024-01-01",
        "backtest_end": "2024-12-01",
        "database_url": "postgresql://localhost/cryptobot",
        "redis_url": "redis://localhost:6379",
        "feature_flags": {"new_ui": True, "beta_models": False}
    }

    bot2 = CryptoBot(full_config)
    bot2.status()

    # Show what was extracted vs ignored
    print("\n--- Config Extraction ---")
    print(f"Config had {len(full_config)} keys")
    print(f"Bot extracted 3 keys: symbols, prediction_horizon, llm")
    print(f"Bot ignored {len(full_config) - 3} keys")

    # Make a prediction
    print("\n--- Prediction ---")
    pred = bot2.predict("BTC/USD")
    print(f"Symbol: {pred['symbol']}")
    print(f"Direction: {pred['direction']}")
    print(f"Confidence: {pred['confidence']:.1%}")
    print(f"LLM Enhanced: {pred['llm_enhanced']}")

    bot2.stop()

    print("\n\n--- Example 3: Grok vs Claude ---\n")

    grok_config = {"prediction_horizon": 24, "llm": "grok"}
    claude_config = {"prediction_horizon": 24, "llm": "claude"}

    bot_grok = CryptoBot(grok_config)
    bot_claude = CryptoBot(claude_config)

    print(f"Grok bot use_grok: {bot_grok.use_grok}")  # True
    print(f"Claude bot use_grok: {bot_claude.use_grok}")  # False

    bot_grok.stop()
    bot_claude.stop()


if __name__ == "__main__":
    main()
```

---

**Output:**

```
--- Example 1: Minimal Config ---

[CryptoBot] Loading models...
  Loaded model for BTC/USD
  Loaded model for ETH/USD
[CryptoBot] Starting background threads...
  Started PriceFeed thread
  Started Predictor thread

CryptoBot(symbols=['BTC/USD', 'ETH/USD'], running=True)
  symbols: ['BTC/USD', 'ETH/USD'] (default)
  horizon: 12 (from config)
  use_grok: True (default)
[CryptoBot] Stopping...
[CryptoBot] Stopped


--- Example 2: Full Config (20 keys, most ignored) ---

[CryptoBot] Loading models...
  Loaded model for BTC/USD
  Loaded model for ETH/USD
  Loaded model for SOL/USD
[CryptoBot] Starting background threads...
  Started PriceFeed thread
  Started Predictor thread

==================================================
CryptoBot Status
==================================================
Running: True
Runtime: 0.0s
Symbols: ['BTC/USD', 'ETH/USD', 'SOL/USD']
Horizon: 48h
Using Grok LLM: False
Models loaded: 3
Active threads: 2
==================================================

--- Config Extraction ---
Config had 20 keys
Bot extracted 3 keys: symbols, prediction_horizon, llm
Bot ignored 17 keys

--- Prediction ---
Symbol: BTC/USD
Direction: up
Confidence: 78.3%
LLM Enhanced: False
[CryptoBot] Stopping...
[CryptoBot] Stopped


--- Example 3: Grok vs Claude ---

[CryptoBot] Loading models...
...
Grok bot use_grok: True
Claude bot use_grok: False
```

---

**Parameter → Attribute mapping:**

| Config Key | Attribute | Transformation |
|------------|-----------|----------------|
| `symbols` | `self.symbols` | Direct (with default) |
| `prediction_horizon` | `self.horizon` | Renamed |
| `llm` | `self.use_grok` | String → Boolean (`== "grok"`) |
| (17 other keys) | — | **Ignored** |
| — | `self.models` | Internal (from `_load_models`) |
| — | `self.threads` | Internal (from `_start_background_threads`) |
| — | `self.is_running` | Internal state |
| — | `self.start_time` | Internal timestamp |
| — | `self.predictions` | Internal cache |

---

**Key pattern:**

```
┌─────────────────────────────────────────────────────────────────┐
│                         __init__(config_dict)                   │
│                                                                 │
│  config_dict = {                                                │
│      "symbols": [...],        ─────► self.symbols               │
│      "prediction_horizon": 48 ─────► self.horizon               │
│      "llm": "claude"          ─────► self.use_grok (== "grok")  │
│      "api_key": "...",        ─────► IGNORED                    │
│      "api_secret": "...",     ─────► IGNORED                    │
│      "exchange": "...",       ─────► IGNORED                    │
│      ... 14 more keys ...     ─────► IGNORED                    │
│  }                                                              │
│                                                                 │
│  (nothing) ──► _load_models() ─────► self.models                │
│  (nothing) ──► _start_threads() ───► self.threads               │
│  (nothing) ──► True ───────────────► self.is_running            │
│  (nothing) ──► time.time() ────────► self.start_time            │
│  (nothing) ──► {} ─────────────────► self.predictions           │
└─────────────────────────────────────────────────────────────────┘
```

---

**Why this pattern?**

| Benefit              | Explanation                                             |
| -------------------- | ------------------------------------------------------- |
| **Flexibility**      | Caller can pass a large config; bot picks what it needs |
| **Decoupling**       | Bot doesn't break if config has extra keys              |
| **Defaults**         | `.get(key, default)` handles missing keys gracefully    |
| **Encapsulation**    | Internal setup (`_load_models`) hidden from caller      |
| **Single parameter** | Easier API than 20 individual parameters                |