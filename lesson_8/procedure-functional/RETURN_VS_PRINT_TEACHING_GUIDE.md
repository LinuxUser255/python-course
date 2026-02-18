# RETURN vs PRINT - One-Page Teaching Guide

## 🎯 The Restaurant Analogy (Easiest Way to Explain)

```
PRINT = The waiter ANNOUNCING "Your burger is ready!"
        → Everyone hears it, but you can't eat an announcement

RETURN = The waiter GIVING you the actual burger on a plate
         → You can eat it, share it, or save it for later
```

---

## 📊 Quick Comparison

| | PRINT | RETURN |
|---|---|---|
| **Purpose** | Show to humans | Give to code |
| **What it does** | Displays on screen | Sends value back |
| **Can you use it?** | ❌ No | ✅ Yes |
| **Can you do math with it?** | ❌ No | ✅ Yes |
| **Default value** | None | The actual value |

---

## 💻 Side-by-Side Examples

### Example 1: The Basic Difference

```python
# PRINT version
def add_print(a, b):
    print(a + b)  # Shows: 8

result = add_print(3, 5)
print(result)  # Shows: None
# Can't use it!
```

```python
# RETURN version
def add_return(a, b):
    return a + b  # Gives back: 8

result = add_return(3, 5)
print(result)  # Shows: 8
# Can use it!
double = result * 2  # Works!
```

---

### Example 2: Real-World Scenario

```python
# PRINT - Can only show
def calculate_tax_print(price):
    tax = price * 0.08
    print(f"Tax: ${tax}")
    # No return!

tax = calculate_tax_print(100)  # Shows: Tax: $8.0
total = 100 + tax  # ERROR! tax is None
```

```python
# RETURN - Can use the value
def calculate_tax_return(price):
    tax = price * 0.08
    return tax

tax = calculate_tax_return(100)  # Nothing shown
total = 100 + tax  # Works! total = 108.0
print(f"Total: ${total}")  # Shows: Total: $108.0
```

---

### Example 3: Using Both (Very Common!)

```python
def calculate_area(length, width):
    area = length * width
    print(f"Area: {area}")  # Show message (for humans)
    return area             # Give value back (for code)

result = calculate_area(5, 10)  # Shows: Area: 50
double = result * 2             # Works! result = 50
```

---

## 🎓 Teaching Tips: How to Explain It

### 1. **The "Use It Later" Test**
Ask students: "Do you need to use this value later in your code?"
- **YES** → Must use `return`
- **NO** → Can use just `print`

### 2. **The Variable Test**
```python
result = some_function()
print(result)
```
- If `result` is `None` → function didn't return anything
- If `result` has a value → function returned something

### 3. **The Math Test**
```python
result = some_function()
answer = result + 10
```
- If this gives an error → function only printed, didn't return
- If this works → function returned a value

---

## 🚨 Common Student Mistakes

### Mistake #1: Thinking PRINT gives back the value
```python
# WRONG
def double(x):
    print(x * 2)  # Student thinks this "returns" the value

result = double(5)  # result is None, not 10!
```

**Why it's confusing:** Students SEE the number on screen and think the function gave it back.

**Fix:** Explain that seeing ≠ having. The function showed you the answer but didn't give it to you.

### Mistake #2: Forgetting return completely
```python
# WRONG
def add(a, b):
    sum = a + b
    # Forgot return!

result = add(3, 5)  # result is None
```

**Fix:** If you calculate something, you usually need to `return` it.

---

## 📝 When to Use Each

### Use PRINT when:
- ✅ Showing messages to users
- ✅ Debugging (seeing what's happening)
- ✅ Displaying formatted output
- ✅ The function's job is just to communicate

```python
def greet_user(name):
    print(f"Hello, {name}!")  # Job is to greet, not calculate

def show_menu():
    print("1. Start")
    print("2. Quit")  # Job is to display menu
```

### Use RETURN when:
- ✅ Calculating values
- ✅ Processing data
- ✅ Making decisions (True/False)
- ✅ Other code needs the result

```python
def calculate_total(price, tax):
    return price + tax  # Code needs this value

def is_adult(age):
    return age >= 18  # Code needs this True/False
```

### Use BOTH when:
- ✅ Want to show a message AND give back a value

```python
def divide(a, b):
    if b == 0:
        print("Error: Can't divide by zero!")
        return None
    
    result = a / b
    print(f"{a} ÷ {b} = {result}")  # Show calculation
    return result  # Give back value
```

---

## 🎯 The Golden Rules

### Rule 1: PRINT talks to humans
```python
print("Hello!")  # Humans see this
```

### Rule 2: RETURN talks to code
```python
return 42  # Code can use this
```

### Rule 3: No return = None
```python
def no_return():
    x = 5 + 3
    # No return means returns None automatically

result = no_return()
print(result)  # None
```

### Rule 4: Can't do math with None
```python
result = function_without_return()
answer = result + 10  # ERROR! Can't add None + 10
```

---

## 🎨 Visual Diagram

```
Function with PRINT:
┌──────────────┐
│  Input: 5    │
│      ↓       │
│  Process     │
│      ↓       │
│  PRINT "10"  │──→ Shows on screen
│      ↓       │
│  Output: ❌  │    Nothing given back
└──────────────┘

Function with RETURN:
┌──────────────┐
│  Input: 5    │
│      ↓       │
│  Process     │
│      ↓       │
│  RETURN 10   │──→ Value given back
│      ↓       │
│  Output: ✅  │    Can be used in code
└──────────────┘
```

---

## 💡 Practice Exercises for Students

### Exercise 1: Which is correct?
```python
# Scenario: Calculate a tip
def calculate_tip(bill):
    tip = bill * 0.15
    print(tip)  # Is this enough?
```
**Answer:** No! If you need to use the tip amount later, must `return tip`

### Exercise 2: Fix this function
```python
def get_full_name(first, last):
    full_name = first + " " + last
    print(full_name)

# Student wants to use it:
name = get_full_name("John", "Doe")
print(f"Name is: {name}")  # Shows: Name is: None
```
**Answer:** Add `return full_name` before the print

### Exercise 3: What will this show?
```python
def mystery(x):
    print(x * 2)
    return x * 3

result = mystery(5)
print(result)
```
**Answer:** 
- First shows: 10 (from print inside function)
- Then shows: 15 (from print of returned value)

---

## 🎤 Teaching Script (What to Say)

> "Think of a function like a factory. When you call the function, it does some work.
> 
> **PRINT** is like the factory announcing 'We made a car!' over the loudspeaker. You hear it, but you don't GET the car.
> 
> **RETURN** is like the factory actually giving you the car. Now you can drive it, sell it, or paint it a different color.
> 
> If you want to USE what the function calculated, you MUST use RETURN.
> 
> PRINT is for showing information.
> RETURN is for giving back values your code can use.
> 
> Ask yourself: Do I need to use this value later?
> - If yes → use RETURN
> - If no → PRINT is fine"

---

## 📚 Quick Reference Card

```python
# ❌ WRONG - Can't use the result
def add(a, b):
    print(a + b)

result = add(5, 3)  # result is None
total = result + 10  # ERROR!

# ✅ CORRECT - Can use the result
def add(a, b):
    return a + b

result = add(5, 3)  # result is 8
total = result + 10  # total is 18

# ✅ BEST - Show message AND return value
def add(a, b):
    result = a + b
    print(f"Adding {a} + {b} = {result}")
    return result
```

---

**Remember:** If your function calculates something, it should probably `return` it!
