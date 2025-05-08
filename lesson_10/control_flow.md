# Control Flow vs. Conditionals in Python

## Key Differences

**Control Flow** is the broader concept that determines the order in which statements are executed in a program. It includes:
- Conditionals (if/elif/else)
- Loops (for/while)
- Function calls
- Exception handling (try/except)
- Jump statements (break, continue, return)

**Conditionals** are specifically a type of control flow structure that executes different code blocks based on whether certain conditions evaluate to True or False.

## Examples of Conditionals

```python
# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
temperature = 75
if temperature > 85:
    print("Hot day ahead!")
else:
    print("The temperature is moderate")

# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Nested conditionals
income = 50000
years_employed = 3
if income > 40000:
    if years_employed >= 2:
        print("Loan approved")
    else:
        print("Employment history too short")
else:
    print("Income too low")
```

## Examples of Other Control Flow Structures

```python
# For loop
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Try-except (exception handling)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Function calls with return
def calculate_tax(income):
    if income < 40000:
        return income * 0.1
    else:
        return income * 0.2
        
tax = calculate_tax(50000)
print(f"Tax amount: ${tax}")

# Break statement
for name in ["Alice", "Bob", "Charlie", "David"]:
    if "d" in name.lower():
        print(f"{name} has the letter D in its name.")
        continue
    
    if name == "Charlie":
        print("Found Charlie, stopping the loop")
        break
```

In summary, conditionals are a specific type of control flow mechanism that allows for decision-making in code, while control flow encompasses all structures that determine the execution path of a program.
