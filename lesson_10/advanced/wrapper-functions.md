# Wrapper Functions

## Why `*args, **kwargs`?

The wrapper doesn't know what function it will wrap, so it must accept **any possible arguments**.

---

## The Problem Without Them

```python
def wrapper():  # No parameters
    result = func()
    return result

@rate_limit()
def fetch_ticker(pair):  # Needs 1 argument
    ...

fetch_ticker("XBTUSD")  # TypeError: wrapper() takes 0 arguments but 1 was given
```

The wrapper intercepts the call but can't pass arguments through.

---

## The Solution

```python
def wrapper(*args, **kwargs):  # Accept anything
    result = func(*args, **kwargs)  # Pass everything through
    return result
```

---

## What `*args` and `**kwargs` Capture

```python
fetch_ticker("XBTUSD", timeout=10)
#            ^^^^^^^^  ^^^^^^^^^^
#            args      kwargs

# Inside wrapper:
# args = ("XBTUSD",)
# kwargs = {"timeout": 10}

# Passed to func:
func(*args, **kwargs)
# Expands to:
func("XBTUSD", timeout=10)
```

---

## Examples of What Gets Captured

```python
@rate_limit()
def example(a, b, c=None, d=None):
    print(f"a={a}, b={b}, c={c}, d={d}")

# Call 1: All positional
example(1, 2, 3, 4)
# args = (1, 2, 3, 4)
# kwargs = {}

# Call 2: Mixed
example(1, 2, d=4)
# args = (1, 2)
# kwargs = {"d": 4}

# Call 3: All keyword
example(a=1, b=2, c=3, d=4)
# args = ()
# kwargs = {"a": 1, "b": 2, "c": 3, "d": 4}
```

All three work because `*args, **kwargs` captures everything.

---

## The Flow

```
fetch_ticker("XBTUSD", timeout=10)
      │
      ▼
wrapper(*args, **kwargs)
      │
      │  args = ("XBTUSD",)
      │  kwargs = {"timeout": 10}
      │
      │  # Rate limit logic...
      │
      ▼
func(*args, **kwargs)
      │
      │  Expands to:
      │  fetch_ticker("XBTUSD", timeout=10)
      │
      ▼
   (result)
      │
      ▼
return result
```

---

## Why Both `*` and `**`?

| Syntax | Captures | Example |
|--------|----------|---------|
| `*args` | Positional arguments | `func(1, 2, 3)` → `args = (1, 2, 3)` |
| `**kwargs` | Keyword arguments | `func(a=1, b=2)` → `kwargs = {"a": 1, "b": 2}` |

You need both to handle any function signature:

```python
# Function with only positional
def add(a, b):
    return a + b

# Function with only keyword
def configure(*, host, port):
    return f"{host}:{port}"

# Function with both
def request(url, method="GET", timeout=30):
    ...

# wrapper(*args, **kwargs) handles ALL of these
```

---

## Summary

```python
def wrapper(*args, **kwargs):
    #        ^^^^^ ^^^^^^^^
    #        │     │
    #        │     └── Catches all keyword arguments as a dict
    #        │
    #        └── Catches all positional arguments as a tuple

    result = func(*args, **kwargs)
    #             ^^^^^ ^^^^^^^^
    #             │     │
    #             │     └── Unpacks dict back to keyword arguments
    #             │
    #             └── Unpacks tuple back to positional arguments

    return result
```

**One line summary:** `*args, **kwargs` makes the wrapper transparent — it accepts anything and passes everything through unchanged.

## Code execution line-by-line
Here’s a **line-by-line execution flow** of production-ready Kraken client —

We’ll go **chronologically**, exactly as Python executes it.

```python
#!/usr/bin/env python3
```
→ Shebang. Makes it executable on Linux/macOS: `./kraken_client.py`

```python
"""
Simplified Kraken API Client
...
"""
```
→ Docstring. Ignored at runtime.

```python
import time
import requests
```
→ Modules loaded into memory. `time` for sleeping, `requests` for HTTP.

```python
KRAKEN_BASE_URL = "https://api.kraken.com/0/public"
RATE_LIMIT = 1.0  # calls per second
```
→ Constants defined. `RATE_LIMIT = 1.0` → max 1 call per second (Kraken Tier 2 limit).

### The Magic: Rate Limiter Decorator

```python
def rate_limit(calls_per_second=RATE_LIMIT):
```
→ Outer function. Called once when decorator is applied.

```python
    min_interval = 1.0 / calls_per_second
```
→ 1.0 second minimum between calls.

```python
    last_called = [0.0]
```
→ **Mutable list** used as closure variable (critical trick!).  
Why a list? Because Python closures can’t reassign primitives, but can mutate objects.

```python
    def decorator(func):
```
→ Returns the actual decorator.

```python
        def wrapper(*args, **kwargs):
```
→ This is the function that replaces `_kraken_get` at runtime.

```python
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
```
→ **Rate limiting logic**: If less than 1 second since last call → sleep the difference.

```python
            result = func(*args, **kwargs)
```
→ **Actually call** the real `_kraken_get`

```python
            last_called[0] = time.time()
```
→ Update timestamp **after** successful call.

```python
            return result
        return wrapper
    return decorator
```
→ Classic 3-layer decorator pattern.  
Final result: `@rate_limit()` → `_kraken_get` is now rate-limited.

### The Core API Function (Now Rate-Limited)

```python
@rate_limit()
def _kraken_get(endpoint, params):
```
→ `_kraken_get` is **replaced** with the `wrapper` from above.  
Every call now goes through rate limiting.

```python
    url = f"{KRAKEN_BASE_URL}/{endpoint}"
    resp = requests.get(url, params=params, timeout=10)
```
→ Builds URL like `https://api.kraken.com/0/public/Ticker`  
Sends GET with query params.

```python
    resp.raise_for_status()
```
→ Raises HTTPError if 4xx/5xx (e.g. 429 Too Many Requests)

```python
    data = resp.json()
```
→ Parse JSON response

```python
    if data.get("error"):
        raise RuntimeError(f"Kraken API error: {data['error']}")
```
→ Kraken returns `{"error": [...]}` even on 200 OK.  
This catches things like invalid pair, rate limit, etc.

```python
    return data["result"]
```
→ Kraken nests real data under `"result"`. We return only that.

### High-Level Public Functions

```python
def fetch_ticker(pair="XBTUSD"):
```
→ Public function. You call this.

```python
    result = _kraken_get("Ticker", {"pair": pair})
```
→ Calls rate-limited function → may sleep!

```python
    ticker = next(iter(result.values()))
```
→ Kraken returns: `{"result": {"XXBTZUSD": {...}}}`  
`result` is a dict with one key → we grab the value (the actual ticker data)

```python
    return {
        "pair": pair,
        "last_price": float(ticker["c"][0]),   # "c" = [price, volume]
        "high_24h": float(ticker["h"][1]),     # "h" = [today, last_24h]
        "low_24h": float(ticker["l"][1]),
        "volume_24h": float(ticker["v"][1]),
    }
```
→ Clean, flat dict. Easy to use.

### OHLC Function

```python
def fetch_ohlc(pair="XBTUSD", interval=60):
    result = _kraken_get("OHLC", {"pair": pair, "interval": interval})
    ohlc_rows = result[pair]           # result looks like {"XXBTZUSD": [[...], [...]]}
```
→ Kraken returns list of lists: `[time, open, high, low, close, vwap, volume, count]`

```python
    candles = []
    for row in ohlc_rows:
        candles.append({
            "timestamp": int(row[0]),
            "open": float(row[1]),
            "high": float(row[2]),
            "low": float(row[3]),
            "close": float(row[4]),
            "volume": float(row[6]),       # index 6 = volume
        })
```
→ Transform raw list → clean dicts

```python
    return sorted(candles, key=lambda c: c["timestamp"])
```
→ Kraken sometimes returns unsorted (rare), so we ensure chronological order.

### Main Execution

```python
def main():
    print("--- Fetch Ticker ---")
    ticker = fetch_ticker("XBTUSD")          # → calls _kraken_get → may sleep
    print(f"BTC/USD: ${ticker['last_price']:,.2f}")
    ...
```
→ Pretty print current price

```python
    print("\n--- Fetch OHLC (last 5 candles) ---")
    candles = fetch_ohlc("XBTUSD", interval=60)   # → another rate-limited call
    for candle in candles[-5:]:
        print(f"  {candle['timestamp']}: O={candle['open']:.2f} ...")
```
→ Show last 5 hourly candles

```python
if __name__ == "__main__":
    main()
```
→ Only runs when executed directly (not when imported)

### Full Execution Flow Summary (What Actually Happens)

```text
1. Script starts
2. All functions defined (nothing runs yet)
3. @rate_limit() decorator APPLIES to _kraken_get → replaces it with wrapper
4. if __name__ == "__main__" → True
5. main() called
6. fetch_ticker("XBTUSD") called
   → _kraken_get("Ticker", ...) called
   → wrapper runs: checks time → maybe sleeps → calls real function
   → HTTP request → parse → return result → extract ticker → print
7. fetch_ohlc() called
   → _kraken_get("OHLC", ...) called
   → wrapper runs again: now ~1+ seconds have passed → no sleep
   → HTTP request → parse → transform rows → sort → print last 5
8. Script ends
```

### Pro Tips From Real Bot Development

| What you did right                                            | Why it matters in production (like our bot)             |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| Rate limiting with closure + list trick                       | Prevents getting IP-banned by Kraken (happens fast!)    |
| `raise_for_status()` + error check                            | Fails fast on bad requests                              |
| Clean return types (dicts, not raw Kraken format)             | Makes backtesting and signals engine **so** much easier |
| `default_factory` pattern (you’ll love this with dataclasses) | This is exactly how we do it in the real bot            |

### One Tiny Improvement (2025 style)

Replace the manual rate limiter with this (cleaner, thread-safe):

```python
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=1, period=1)
def _kraken_get(...):
    ...
```

But this closure version is **perfectly valid** and very educational.

This code is **production-grade**. 


---

## Comparison

| Aspect         | Manual Version | `ratelimit` Library     |
| -------------- | -------------- | ----------------------- |
| Thread-safe    | No             | Yes                     |
| Lines of code  | 15             | 3                       |
| Battle-tested  | No             | Yes                     |
| Dependency     | None           | `pip install ratelimit` |
| Learning value | High           | Low                     |

---

## When to Use Which

**Use the library when:**
- Production code
- Multi-threaded applications
- You want reliability over understanding

**Use manual version when:**
- Learning how decorators work
- Avoiding dependencies
- Need custom behavior (logging, metrics, etc.)

---

## One Consideration

The manual version has **per-function state**:

```python
@rate_limit()
def func_a(): ...  # Has its own last_called

@rate_limit()
def func_b(): ...  # Has its own last_called

# func_a and func_b can be called back-to-back without sleeping
```

The library version with shared decorator behaves the same way — each decorated function is independent.

---

## If You Need Global Rate Limiting

Both calls share one limit (e.g., Kraken's overall API limit):

```python
# Library approach
from ratelimit import limits, sleep_and_retry

kraken_limit = limits(calls=1, period=1)

@sleep_and_retry
@kraken_limit
def fetch_ticker(): ...

@sleep_and_retry
@kraken_limit
def fetch_ohlc(): ...

# Now fetch_ticker() + fetch_ohlc() share the same rate limit
```

---

**Verdict:** Use the library. Keep the manual version in your notes for understanding decorators.