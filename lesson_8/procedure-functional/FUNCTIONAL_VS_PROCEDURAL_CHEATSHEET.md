# Procedural vs Functional Programming - Cheat Sheet

## 🎯 Quick Comparison

| Aspect | Procedural | Functional |
|--------|-----------|-----------|
| **Style** | Do this, then that | What to compute |
| **Functions** | Perform actions | Return values |
| **State** | Mutable (changes) | Immutable (never changes) |
| **Side Effects** | Common (print, modify) | Avoided |
| **Loops** | for, while | map, filter, reduce |
| **Testing** | Harder (depends on state) | Easier (pure functions) |

---

## 📝 Same Logic, Different Styles

### Example 1: Check if Adult

```python
# PROCEDURAL
def check_age():
    age = 18
    if age >= 18:
        print("Adult")  # Side effect (prints)
    else:
        print("Minor")

check_age()


# FUNCTIONAL
def is_adult(age: int) -> str:
    return "Adult" if age >= 18 else "Minor"  # Pure function (returns)

result = is_adult(18)
print(result)  # Side effect separated from logic
```

---

### Example 2: Calculate Grades

```python
# PROCEDURAL
def calculate_grade():
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")


# FUNCTIONAL
def get_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

grade = get_grade(85)
print(grade)
```

---

### Example 3: Process List of Ages

```python
ages = [15, 18, 25, 12, 30]

# PROCEDURAL (loop)
results = []
for age in ages:
    if age >= 18:
        results.append("adult")
    else:
        results.append("minor")
print(results)


# FUNCTIONAL (map + lambda)
results = list(map(lambda age: "adult" if age >= 18 else "minor", ages))
print(results)
```

---

## 🧩 Functional Programming Tools

### 1. Lambda (Anonymous Functions)
```python
# Regular function
def add(x, y):
    return x + y

# Lambda (one-liner)
add = lambda x, y: x + y

# Usage
print(add(3, 5))  # 8
```

### 2. Map (Transform each item)
```python
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
```

### 3. Filter (Keep items that match)
```python
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

### 4. Reduce (Combine into single value)
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
# 15
```

---

## 🔑 Key Functional Concepts

### Pure Functions
```python
# IMPURE (has side effects)
total = 0
def add_to_total(x):
    global total
    total += x  # Modifies external state
    print(total)  # Side effect

# PURE (no side effects)
def add(x, y):
    return x + y  # Only returns value
```

**Pure Function Rules:**
1. Same input → always same output
2. No side effects (no print, no global variables)
3. Doesn't modify input

### Immutability
```python
# MUTABLE (procedural)
my_list = [1, 2, 3]
my_list.append(4)  # Changes original
print(my_list)  # [1, 2, 3, 4]

# IMMUTABLE (functional)
my_list = [1, 2, 3]
new_list = my_list + [4]  # Creates new list
print(my_list)   # [1, 2, 3] - original unchanged
print(new_list)  # [1, 2, 3, 4]
```

### Higher-Order Functions
```python
def apply_twice(func, value):
    """Function that takes a function as argument."""
    return func(func(value))

def double(x):
    return x * 2

result = apply_twice(double, 5)
# double(double(5)) = double(10) = 20
```

---

## 🎓 Is Functional = Lambda?

### ❌ NO!

Lambda is just **one tool** in functional programming.

### Functional Programming Includes:
- ✅ Pure functions
- ✅ Immutability
- ✅ map, filter, reduce
- ✅ Lambda
- ✅ Function composition
- ✅ Recursion
- ✅ No side effects

### You Can Be Functional Without Lambda:
```python
# Functional WITHOUT lambda
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))

# Functional WITH lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Both are functional!
```

---

## 📊 When to Use Each?

### Use Procedural When:
- ✅ Simple scripts
- ✅ Learning basics
- ✅ Team prefers it
- ✅ Performance critical
- ✅ Lots of I/O (files, network)

### Use Functional When:
- ✅ Data transformations
- ✅ Want testable code
- ✅ Processing collections
- ✅ No shared state
- ✅ Parallel processing

### Reality: Most code is **MIXED**!
```python
# Mixed: functional logic, procedural I/O
def process_scores(scores):
    # Functional: transform data
    passing = list(filter(lambda s: s >= 70, scores))
    grades = list(map(lambda s: "A" if s >= 90 else "B", passing))

    # Procedural: output
    for grade in grades:
        print(grade)
```

---

## 💡 Quick Tips

1. **Start simple:** Master procedural first
2. **Learn lambda:** Useful for simple functions
3. **Practice map/filter:** Common in real code
4. **Write pure functions:** Easier to test
5. **Don't force it:** Use what makes sense

---

## 🚀 Try This Exercise

Convert this procedural code to functional:

```python
# PROCEDURAL
def process_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num * 2)

    print(result)

process_numbers()
```

**Your turn:** Rewrite using map and filter!

<details>
<summary>Solution (click to reveal)</summary>

```python
# FUNCTIONAL
def process_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = list(
        map(lambda x: x * 2,           # Double them
            filter(lambda x: x % 2 == 0, numbers)  # Keep evens
        )
    )

    print(result)

process_numbers()
# Output: [4, 8, 12, 16, 20]
```

</details>
