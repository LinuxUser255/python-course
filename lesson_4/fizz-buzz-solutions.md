# Fizz Buzz, incorrect, correct, and optimal

**Example Two is correct and more Pythonic!** 

Example One has a **critical logic bug**. Let me explain:

---

## 🐛 **Example One - BROKEN**

```python
def fizz_buzz_example_one():
    number = 9

    if number % 3 == 0:           # ← Checks first
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:  # ← NEVER REACHED!
        print("FizzBuzz")
    else:
        print(f"The {number} is not divisible by 3 or 5.")
```

**The Problem:**
- When `number = 15`, it checks if `15 % 3 == 0` first
- This is `True`, so it prints `"Fizz"` and exits
- The `FizzBuzz` condition **never gets checked** because of the `elif`!

**Test it:**
```python
fizz_buzz_example_one()  # With number = 15
# Output: Fizz  ❌ WRONG! Should be "FizzBuzz"
```

---

## ✅ **Example Two - CORRECT**

```python
def fizz_buzz_example_two():
    number = 15

    if number % 3 == 0 and number % 5 == 0:  # ← Checks MOST SPECIFIC first
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

**Why it works:**
- Checks the **most specific condition first** (divisible by both)
- Then checks individual conditions
- This is the correct order!

**Test it:**
```python
fizz_buzz_example_two()  # With number = 15
# Output: FizzBuzz  ✅ CORRECT!
```

---

##  **The Rule: Most Specific First**

When using `if/elif/else`, **check the most specific conditions first**:

```
1. Most specific:    divisible by BOTH 3 AND 5
2. Less specific:    divisible by 3
3. Less specific:    divisible by 5
4. Default:          everything else
```

---

## 📊 **Side-by-Side Testing**

```python
# Testing both functions with number = 15

# Example One (WRONG ORDER)
if 15 % 3 == 0:              # True! Prints "Fizz" and stops
    print("Fizz")
elif 15 % 5 == 0:            # Never checked
    print("Buzz")
elif 15 % 3 == 0 and 15 % 5 == 0:  # Never reached!
    print("FizzBuzz")

# Output: Fizz ❌


# Example Two (CORRECT ORDER)
if 15 % 3 == 0 and 15 % 5 == 0:    # True! Prints "FizzBuzz" and stops
    print("FizzBuzz")
elif 15 % 3 == 0:            # Never checked (already handled above)
    print("Fizz")
elif 15 % 5 == 0:            # Never checked
    print("Buzz")

# Output: FizzBuzz ✅
```

---

##  **Most Pythonic FizzBuzz (Even Better!)**

Here's an even cleaner version using string concatenation:

```python
def fizz_buzz(number):
    """Most Pythonic FizzBuzz."""
    result = ""

    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"

    print(result or number)  # Print result if not empty, else number


# Test it
fizz_buzz(9)   # Fizz
fizz_buzz(10)  # Buzz
fizz_buzz(15)  # FizzBuzz
fizz_buzz(7)   # 7
```

**Why this is best:**
- No need to check "both" separately
- Naturally handles the FizzBuzz case
- More extensible (easy to add "Jazz" for divisible by 7, etc.)
- Uses `or` for elegant default

---

##  **Summary**

| | Example One | Example Two |
|---|---|---|
| **Correctness** | ❌ Broken | ✅ Correct |
| **Logic** | Wrong order | Right order |
| **FizzBuzz (15)** | Prints "Fizz" ❌ | Prints "FizzBuzz" ✅ |
| **Pythonic** | No | Yes |

**Answer:** **Example Two is preferred!** It checks the most specific condition first, which is the correct approach for FizzBuzz.

---

##  **Key Takeaway**

**Always check the MOST SPECIFIC condition first in if/elif chains.**

Otherwise, the more general conditions will "catch" cases that should go to more specific ones, and your later conditions will never be reached!
