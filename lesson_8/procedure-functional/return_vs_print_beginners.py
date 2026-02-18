#!/usr/bin/env python3

"""
Understanding RETURN vs PRINT for Beginners

This guide explains the difference between return and print in a way
that's easy to understand for people just learning Python.
"""

print("=" * 80)
print("RETURN vs PRINT: The Complete Beginner's Guide")
print("=" * 80)

# ============================================================================
# THE SIMPLE ANALOGY
# ============================================================================

print("""
🎯 THE RESTAURANT ANALOGY

Imagine a function is like a restaurant kitchen:

PRINT = The waiter ANNOUNCING the food to the dining room
        "Your burger is ready!" (Everyone hears it)
        But you can't eat an announcement!

RETURN = The waiter GIVING you the actual food
         You get the burger on a plate (You can eat it!)
         You can share it, save it for later, or modify it

Key insight: PRINT shows you something.
             RETURN gives you something you can use.
""")

input("Press Enter to see examples...\n")


# ============================================================================
# EXAMPLE 1: The Most Basic Difference
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 1: The Most Basic Difference")
print("=" * 80)

# Function that PRINTS
def add_and_print(a, b):
    result = a + b
    print(result)  # Shows the answer
    # Notice: No return statement!

# Function that RETURNS
def add_and_return(a, b):
    result = a + b
    return result  # Gives back the answer


print("\n--- Using the PRINT function ---")
add_and_print(3, 5)  # You see: 8
print("The function printed 8, but gave us nothing back.\n")

# Try to save the result
saved_result = add_and_print(10, 20)  # You see: 30
print(f"What did we save? {saved_result}")  # None!
print("We got None because the function didn't RETURN anything.\n")


print("\n--- Using the RETURN function ---")
result = add_and_return(3, 5)  # Nothing printed!
print(f"But we saved: {result}")  # We have the value!
print("The function gave us back the value 8.\n")

# Now we can USE the result
double = result * 2
print(f"We can use it: {result} * 2 = {double}")
print(f"We can do math with it: {result} + 100 = {result + 100}")
print(f"We can pass it to other functions: max({result}, 10) = {max(result, 10)}")

print("""
📝 KEY LESSON:
   - PRINT shows something on screen (for humans to see)
   - RETURN gives the value back to your code (for code to use)
""")

input("\nPress Enter to continue...\n")


# ============================================================================
# EXAMPLE 2: Why This Matters - Using Results
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 2: Why RETURN Matters - Using Results")
print("=" * 80)

# PRINT version - can't use the result
def calculate_tax_print(price):
    tax = price * 0.08
    print(f"Tax is: ${tax}")
    # No return!

# RETURN version - can use the result
def calculate_tax_return(price):
    tax = price * 0.08
    return tax


print("\n--- With PRINT (limited) ---")
calculate_tax_print(100)  # Shows: Tax is: $8.0

# Try to use it to calculate total
tax_amount = calculate_tax_print(100)  # Shows: Tax is: $8.0
print(f"tax_amount = {tax_amount}")  # None!

# Can't do this:
# total = 100 + tax_amount  # ERROR! Can't add number + None


print("\n--- With RETURN (flexible) ---")
tax = calculate_tax_return(100)  # Nothing shown, but we have the value!
print(f"Tax: ${tax}")

# Now we can use it!
total = 100 + tax
print(f"Total with tax: ${total}")

# We can use it in calculations
discount = tax * 0.5
print(f"Half tax discount: ${discount}")

print("""
📝 KEY LESSON:
   If you want to USE the result in your program, you MUST use RETURN.
   PRINT just shows information, but doesn't give it back to use.
""")

input("\nPress Enter to continue...\n")


# ============================================================================
# EXAMPLE 3: The Visual Difference
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 3: The Visual Difference")
print("=" * 80)

print("""
Think of functions as MACHINES:

┌─────────────────────┐
│   PRINT Machine     │
│                     │
│  Input: 5 + 3       │
│     ↓               │
│  Calculates: 8      │
│     ↓               │
│  ANNOUNCES: "8"     │  ← You see this on screen
│                     │
│  Output: Nothing    │  ← Function gives back nothing
└─────────────────────┘

┌─────────────────────┐
│   RETURN Machine    │
│                     │
│  Input: 5 + 3       │
│     ↓               │
│  Calculates: 8      │
│     ↓               │
│  Output: 8          │  ← Function gives back the value
│     ↓               │
│  (You can catch it) │
└─────────────────────┘
""")

input("Press Enter to continue...\n")


# ============================================================================
# EXAMPLE 4: Real-World Scenarios
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 4: Real-World Scenarios")
print("=" * 80)

print("\n--- Scenario 1: Checking if someone can vote ---\n")

# PRINT version
def can_vote_print(age):
    if age >= 18:
        print("Yes, you can vote!")
    else:
        print("No, you're too young.")
    # No return!

# RETURN version
def can_vote_return(age):
    if age >= 18:
        return True
    else:
        return False


# With PRINT - can only show the answer
print("Using PRINT version:")
can_vote_print(20)  # Shows: Yes, you can vote!
can_vote_print(16)  # Shows: No, you're too young.

# But we can't use it in decisions
result = can_vote_print(20)  # Shows: Yes, you can vote!
print(f"Result stored: {result}\n")  # None!

# Can't do this:
# if result:  # Won't work - result is None!
#     print("Let's go to the polls!")


# With RETURN - can use the answer in our program
print("\nUsing RETURN version:")
can_vote = can_vote_return(20)  # Nothing shown, but we have True
print(f"Result stored: {can_vote}")

# Now we can use it!
if can_vote:
    print("Great! Let's go to the polls!")
    print("Don't forget your ID!")

# We can use it in calculations
voters = [can_vote_return(20), can_vote_return(16), can_vote_return(25)]
total_voters = sum(voters)
print(f"\nOut of 3 people, {total_voters} can vote")

print("""
📝 KEY LESSON:
   Use RETURN when you need to make decisions or do calculations
   with the result. Use PRINT when you just want to show information.
""")

input("\nPress Enter to continue...\n")


# ============================================================================
# EXAMPLE 5: Combining PRINT and RETURN
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 5: You Can Use BOTH!")
print("=" * 80)

def calculate_area(length, width):
    """
    A function can both PRINT (for humans) and RETURN (for code).
    """
    area = length * width
    
    # PRINT for human-readable message
    print(f"Calculating area of {length} x {width}...")
    
    # RETURN so the code can use it
    return area


print("\nExample: Calculating areas of multiple rooms\n")

# Get areas (see messages AND can use the values)
living_room = calculate_area(15, 20)
bedroom = calculate_area(12, 14)
kitchen = calculate_area(10, 12)

# Now we can use the returned values
total_area = living_room + bedroom + kitchen
print(f"\nTotal house area: {total_area} square feet")

print("""
📝 KEY LESSON:
   Functions can BOTH print (for information) AND return (for code to use).
   This is actually very common in real programs!
""")

input("\nPress Enter to continue...\n")


# ============================================================================
# EXAMPLE 6: What Happens Without RETURN?
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 6: What Happens Without RETURN?")
print("=" * 80)

def no_return_function():
    """This function doesn't have a return statement."""
    x = 5 + 3
    # No return!

def has_return_function():
    """This function returns a value."""
    x = 5 + 3
    return x


print("\n--- Function without return ---")
result1 = no_return_function()
print(f"Result: {result1}")  # None
print(f"Type: {type(result1)}")  # <class 'NoneType'>

print("\n--- Function with return ---")
result2 = has_return_function()
print(f"Result: {result2}")  # 8
print(f"Type: {type(result2)}")  # <class 'int'>

print("""
📝 KEY LESSON:
   If a function doesn't have RETURN, it automatically returns None.
   None means "nothing" or "no value".
""")

input("\nPress Enter to continue...\n")


# ============================================================================
# EXAMPLE 7: Common Beginner Mistake
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 7: Common Beginner Mistake")
print("=" * 80)

print("""
MISTAKE: Students often think PRINT gives back the value because they
         can see it on the screen!
""")

def multiply_wrong(a, b):
    """WRONG: Only prints, doesn't return."""
    result = a * b
    print(result)  # Just shows it
    # Missing return!

def multiply_correct(a, b):
    """CORRECT: Returns the value."""
    result = a * b
    return result  # Gives it back


print("\n--- The Problem ---")
# This looks like it works...
print("Calling multiply_wrong(5, 3):")
multiply_wrong(5, 3)  # Shows: 15

# But watch what happens when we try to use it:
print("\nTrying to use the result:")
answer = multiply_wrong(5, 3)  # Shows: 15
print(f"Saved value: {answer}")  # None!

print("\nTrying to do math with it:")
# total = answer + 10  # ERROR! Can't add None + 10


print("\n--- The Fix ---")
print("Calling multiply_correct(5, 3):")
answer = multiply_correct(5, 3)  # Nothing shown, but we have it
print(f"Saved value: {answer}")  # 15

print("\nNow we can use it:")
total = answer + 10
print(f"Can do math: {answer} + 10 = {total}")

print("""
📝 KEY LESSON:
   Just because you SEE a value printed doesn't mean the function
   RETURNED it. If you want to use the value, you MUST return it!
""")

input("\nPress Enter to continue...\n")


# ============================================================================
# EXAMPLE 8: When to Use Each
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 8: When to Use PRINT vs RETURN")
print("=" * 80)

print("""
USE PRINT WHEN:
  ✓ You want to show a message to the user
  ✓ You're debugging (checking what's happening)
  ✓ You want to display results in a nice format
  ✓ The function's purpose is to communicate, not calculate

EXAMPLES:
""")

def greet_user(name):
    """Purpose: Say hello (not calculate anything)."""
    print(f"Hello, {name}! Welcome!")
    # No return needed - this function's job is just to greet

def show_menu():
    """Purpose: Display options (not return a value)."""
    print("1. Start Game")
    print("2. Load Game")
    print("3. Quit")
    # No return needed - just showing information

greet_user("Alice")
show_menu()


print("""
USE RETURN WHEN:
  ✓ You need to use the result in your code
  ✓ You're calculating something
  ✓ You're processing data
  ✓ Other functions need this value

EXAMPLES:
""")

def get_user_age():
    """Calculate age - other code needs this value."""
    birth_year = 2000
    current_year = 2025
    return current_year - birth_year  # Other code will use this

def is_valid_email(email):
    """Check email - code needs to know true/false."""
    return "@" in email and "." in email  # Code needs this answer

age = get_user_age()
print(f"User's age: {age}")

valid = is_valid_email("test@example.com")
print(f"Email is valid: {valid}")


print("""
USE BOTH WHEN:
  ✓ You want to show a message AND give back a value

EXAMPLE:
""")

def divide_with_feedback(a, b):
    """Show message AND return value."""
    if b == 0:
        print("Error: Can't divide by zero!")
        return None
    
    result = a / b
    print(f"{a} ÷ {b} = {result}")  # Show the calculation
    return result  # Give back the value

answer = divide_with_feedback(10, 2)
if answer:
    double = answer * 2
    print(f"Double the result: {double}")

input("\nPress Enter to continue...\n")


# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("FINAL SUMMARY: The Golden Rules")
print("=" * 80)

print("""
🎯 THINK OF IT THIS WAY:

PRINT = Talking to HUMANS
        - Shows messages on screen
        - Makes output readable
        - For display purposes

RETURN = Talking to CODE
         - Gives values back to your program
         - Allows calculations and decisions
         - For program logic


📋 QUICK REFERENCE:

┌────────────────────────────────────────────────────────────┐
│                    PRINT vs RETURN                         │
├────────────────────────────────────────────────────────────┤
│ PRINT                   │  RETURN                          │
├─────────────────────────┼──────────────────────────────────┤
│ Shows on screen         │  Gives back to code              │
│ For humans to read      │  For code to use                 │
│ Can't use in math       │  Can use in calculations         │
│ Result is None          │  Result is the actual value      │
│ Good for messages       │  Good for calculations           │
│ Good for debugging      │  Good for functions              │
└─────────────────────────┴──────────────────────────────────┘


🎓 REMEMBER:

1. If you want to SEE something → use PRINT
2. If you want to USE something → use RETURN
3. You can use BOTH in the same function!
4. Without RETURN, the function gives back None


💡 THE TEST:

Ask yourself: "Do I need to use this value later in my code?"

   YES → Use RETURN
   NO  → Use PRINT (or both!)


🔥 COMMON MISTAKES TO AVOID:

❌ def add(a, b):
       print(a + b)  # Wrong if you need to use the result!
   
✅ def add(a, b):
       return a + b  # Correct - can use the result
   
✅ def add(a, b):
       result = a + b
       print(f"Adding {a} + {b} = {result}")  # Show message
       return result  # AND give back value


🎉 YOU'VE GOT THIS!

RETURN is about giving data back to your program.
PRINT is about showing information to humans.

Most functions should RETURN something unless their only job
is to display information.
""")


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "=" * 80)
print("PRACTICE EXERCISES")
print("=" * 80)

print("""
Try to predict: Will these work? Why or why not?

EXERCISE 1:
def double(x):
    print(x * 2)

result = double(5)
answer = result + 10  # Will this work?

ANSWER: No! result is None (function didn't return anything).


EXERCISE 2:
def double(x):
    return x * 2

result = double(5)
answer = result + 10  # Will this work?

ANSWER: Yes! result is 10, so answer will be 20.


EXERCISE 3:
def greet(name):
    print(f"Hello, {name}!")
    return name.upper()

message = greet("Alice")
print(message)  # What will this show?

ANSWER: First shows "Hello, Alice!" (from print inside function)
        Then shows "ALICE" (from print of returned value)


EXERCISE 4: Fix this function
def calculate_discount(price, percent):
    discount = price * (percent / 100)
    print(f"Discount: ${discount}")
    # What's missing?

ANSWER: Add "return discount" so code can use the value!
""")

print("\n" + "=" * 80)
print("END OF GUIDE")
print("=" * 80)
print("""
Remember: 
  🖨️  PRINT = Show to humans
  ↩️  RETURN = Give to code

Now go practice writing functions with return!
""")
