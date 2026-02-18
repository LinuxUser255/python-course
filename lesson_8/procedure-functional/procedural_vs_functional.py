#!/usr/bin/env python3

"""
Procedural vs Functional Programming Comparison

This file demonstrates the same logic written in both:
1. Procedural style (your original approach)
2. Functional style (pure functions, immutability, composition)
"""

# ============================================================================
# PROCEDURAL STYLE (Your Original Approach)
# ============================================================================

print("=" * 60)
print("PROCEDURAL PROGRAMMING STYLE")
print("=" * 60)


def procedural_adult_or_minor() -> None:
    """
    Procedural: Has side effects (prints directly).
    Returns nothing.
    """
    age = 18
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


def procedural_grade_calculator() -> None:
    """
    Procedural: Modifies state, prints directly.
    """
    score = 85

    if score >= 90:
        print("A grade")
    elif score >= 80:
        print("B grade")
    elif score >= 70:
        print("C grade")
    else:
        print("Below C grade")


def procedural_day_type(day: str) -> None:
    """
    Procedural: Uses match but still prints (side effect).
    """
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("Weekday")
        case "saturday" | "sunday":
            print("Weekend")
        case _:
            print("Invalid day")


# Run procedural examples
print("\n--- Procedural Examples ---")
procedural_adult_or_minor()
procedural_grade_calculator()
procedural_day_type("Monday")


# ============================================================================
# FUNCTIONAL STYLE (Pure Functions)
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTIONAL PROGRAMMING STYLE")
print("=" * 60)


def functional_adult_or_minor(age: int) -> str:
    """
    Functional: Pure function.
    - Takes input
    - Returns output
    - No side effects
    - Same input always produces same output
    """
    return "You are an adult." if age >= 18 else "You are a minor."


def functional_grade_calculator(score: int) -> str:
    """
    Functional: Returns result instead of printing.
    Deterministic - same input always gives same output.
    """
    if score >= 90:
        return "A grade"
    elif score >= 80:
        return "B grade"
    elif score >= 70:
        return "C grade"
    else:
        return "Below C grade"


def functional_day_type(day: str) -> str:
    """
    Functional: Returns result, no printing.
    """
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"


# Run functional examples (notice we handle output separately)
print("\n--- Functional Examples ---")
print(functional_adult_or_minor(18))
print(functional_adult_or_minor(16))
print(functional_grade_calculator(85))
print(functional_day_type("Monday"))


# ============================================================================
# FUNCTIONAL PROGRAMMING: ADVANCED CONCEPTS
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTIONAL PROGRAMMING: ADVANCED FEATURES")
print("=" * 60)


# 1. LAMBDA FUNCTIONS (Anonymous functions)
print("\n--- Lambda Functions ---")

# Traditional function
def add(x, y):
    return x + y

# Lambda equivalent (one-liner)
add_lambda = lambda x, y: x + y

print(f"Traditional: add(3, 5) = {add(3, 5)}")
print(f"Lambda: add_lambda(3, 5) = {add_lambda(3, 5)}")

# Lambda for age check
is_adult = lambda age: age >= 18
print(f"is_adult(18) = {is_adult(18)}")
print(f"is_adult(16) = {is_adult(16)}")


# 2. HIGHER-ORDER FUNCTIONS (Functions that take functions as arguments)
print("\n--- Higher-Order Functions ---")

def apply_operation(func, value):
    """
    Higher-order function: takes a function as an argument.
    """
    return func(value)

# Pass different functions
print(f"Apply is_adult to 20: {apply_operation(is_adult, 20)}")
print(f"Apply lambda to 5: {apply_operation(lambda x: x * 2, 5)}")


# 3. MAP (Apply function to each item in a list)
print("\n--- Map (Transform data) ---")

ages = [15, 18, 25, 12, 30]

# Procedural way (loop)
procedural_results = []
for age in ages:
    procedural_results.append("adult" if age >= 18 else "minor")
print(f"Procedural: {procedural_results}")

# Functional way (map)
functional_results = list(map(lambda age: "adult" if age >= 18 else "minor", ages))
print(f"Functional (map): {functional_results}")


# 4. FILTER (Keep only items that match condition)
print("\n--- Filter (Select data) ---")

scores = [45, 78, 92, 65, 88, 55]

# Procedural way
procedural_passing = []
for score in scores:
    if score >= 70:
        procedural_passing.append(score)
print(f"Procedural passing scores: {procedural_passing}")

# Functional way (filter)
functional_passing = list(filter(lambda score: score >= 70, scores))
print(f"Functional (filter) passing scores: {functional_passing}")


# 5. REDUCE (Combine all items into single value)
print("\n--- Reduce (Aggregate data) ---")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Procedural way
procedural_sum = 0
for num in numbers:
    procedural_sum += num
print(f"Procedural sum: {procedural_sum}")

# Functional way (reduce)
functional_sum = reduce(lambda acc, num: acc + num, numbers)
print(f"Functional (reduce) sum: {functional_sum}")


# 6. FUNCTION COMPOSITION (Chaining functions)
print("\n--- Function Composition ---")

def double(x):
    return x * 2

def add_ten(x):
    return x + 10

def square(x):
    return x ** 2

# Procedural way (step by step)
value = 5
value = double(value)    # 10
value = add_ten(value)   # 20
value = square(value)    # 400
print(f"Procedural composition: {value}")

# Functional way (nested calls)
result = square(add_ten(double(5)))
print(f"Functional composition: {result}")

# Functional way (using reduce for composition)
def compose(*functions):
    """Compose multiple functions together."""
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

pipeline = compose(double, add_ten, square)
print(f"Functional pipeline: {pipeline(5)}")


# 7. IMMUTABILITY (Don't modify data, create new data)
print("\n--- Immutability ---")

# Procedural (mutable)
procedural_list = [1, 2, 3]
procedural_list.append(4)  # Modifies original
print(f"Procedural (mutated): {procedural_list}")

# Functional (immutable)
functional_list = [1, 2, 3]
new_list = functional_list + [4]  # Creates new list
print(f"Functional (original): {functional_list}")
print(f"Functional (new): {new_list}")


# 8. RECURSION (Functional alternative to loops)
print("\n--- Recursion ---")

# Procedural (loop)
def factorial_procedural(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Functional (recursion)
def factorial_functional(n):
    return 1 if n <= 1 else n * factorial_functional(n - 1)

print(f"Procedural factorial(5): {factorial_procedural(5)}")
print(f"Functional factorial(5): {factorial_functional(5)}")


# ============================================================================
# PRACTICAL EXAMPLE: Grading System
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Student Grading System")
print("=" * 60)

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": 65},
    {"name": "Diana", "score": 88},
    {"name": "Eve", "score": 55},
]

# PROCEDURAL APPROACH
print("\n--- Procedural Approach ---")

def procedural_grading_system():
    passing_students = []

    for student in students:
        if student["score"] >= 70:
            grade = "A" if student["score"] >= 90 else "B" if student["score"] >= 80 else "C"
            passing_students.append({
                "name": student["name"],
                "score": student["score"],
                "grade": grade
            })

    # Print results
    for student in passing_students:
        print(f"{student['name']}: {student['score']} ({student['grade']})")

procedural_grading_system()


# FUNCTIONAL APPROACH
print("\n--- Functional Approach ---")

def assign_grade(score: int) -> str:
    """Pure function to assign grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

def is_passing(student: dict) -> bool:
    """Pure function to check if passing."""
    return student["score"] >= 70

def add_grade(student: dict) -> dict:
    """Pure function to add grade (returns new dict)."""
    return {**student, "grade": assign_grade(student["score"])}

# Functional pipeline
passing_with_grades = list(
    map(add_grade,                    # Add grades
        filter(is_passing, students)  # Filter passing students
    )
)

# Output (side effect separated from logic)
for student in passing_with_grades:
    print(f"{student['name']}: {student['score']} ({student['grade']})")


# ============================================================================
# KEY DIFFERENCES SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY DIFFERENCES SUMMARY")
print("=" * 60)

print("""
PROCEDURAL:
  ✓ Functions perform actions (print, modify state)
  ✓ Use loops (for, while)
  ✓ Mutate data (change variables)
  ✓ Step-by-step instructions
  ✓ Easier for beginners

FUNCTIONAL:
  ✓ Functions return values (pure)
  ✓ Use map, filter, reduce (no explicit loops)
  ✓ Immutable data (create new instead of modifying)
  ✓ Declarative (what, not how)
  ✓ Easier to test and reason about
  ✓ Better for parallel processing

WHEN TO USE FUNCTIONAL:
  • Data transformations
  • No shared state needed
  • Want predictable, testable code
  • Working with collections

WHEN TO USE PROCEDURAL:
  • Simple scripts
  • Performance-critical code
  • Interacting with external systems (files, APIs)
  • Easier for team to understand
""")


# ============================================================================
# LAMBDA: YES OR NO?
# ============================================================================

print("\n" + "=" * 60)
print("IS FUNCTIONAL = LAMBDA?")
print("=" * 60)

print("""
NO! Lambda is just ONE tool in functional programming.

Functional Programming Includes:
  • Pure functions (no side effects)
  • Immutability
  • First-class functions
  • Higher-order functions (map, filter, reduce)
  • Lambda (anonymous functions)
  • Function composition
  • Recursion

Lambda is useful but NOT required for functional programming!

Example without lambda:
""")

# Functional without lambda
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(f"Without lambda: {evens}")

# Functional with lambda
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"With lambda: {evens_lambda}")

print("\nBoth are functional! Lambda just makes it shorter for simple functions.")
