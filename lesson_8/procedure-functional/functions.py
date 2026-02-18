#!/usr/bin/env python3

"""
Lesson 8: Functions in Python

In this lesson, we'll explore:
1. Defining and calling functions
2. Function parameters and arguments
3. Return statements
4. The break keyword in functions

Functions are reusable blocks of code that perform specific tasks.
They help in organizing code, improving readability, and reducing repetition.
"""

# 1. Defining and calling functions

def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Calling the function
print("Calling greet() function:")
greet()

# 2. Function parameters and arguments

def personalized_greeting(name):
    """A function that takes a parameter and prints a personalized greeting."""
    print(f"Hello, {name}!")

# Calling the function with an argument
print("\nCalling personalized_greeting() function:")
personalized_greeting("Alice")
personalized_greeting("Bob")

# Function with multiple parameters
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Calling the function with positional arguments
describe_pet("dog", "Buddy")

# Calling the function with keyword arguments
describe_pet(animal_type="cat", pet_name="Whiskers")

# 3. Return statements

def add_numbers(a, b):
    """A function that adds two numbers and returns the result."""
    return a + b

# Calling the function and using the returned value
result = add_numbers(5, 3)
print(f"\nThe result of 5 + 3 is: {result}")

# Function with multiple return statements
def get_number_info(number):
    """Return information about a number."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Calling the function with different inputs
print(f"\n5 is {get_number_info(5)}")
print(f"-2 is {get_number_info(-2)}")
print(f"0 is {get_number_info(0)}")

# 4. The break keyword in functions

def find_number(numbers, target):
    """Find a target number in a list and return its index."""
    for index, number in enumerate(numbers):
        if number == target:
            print(f"Found {target} at index {index}")
            break
    else:
        print(f"{target} not found in the list")

# Calling the function
print("\nSearching for numbers:")
number_list = [1, 3, 5, 7, 9, 11, 13]
find_number(number_list, 7)
find_number(number_list, 10)

"""
Practice Exercises:

1. Write a function called 'calculate_area' that takes the radius of a circle as a parameter
   and returns the area of the circle. (Hint: use 3.14 for pi)

2. Create a function called 'is_palindrome' that takes a string as an input and returns True
   if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

3. Write a function called 'print_fibonacci' that takes a number n as input and prints the
   first n numbers in the Fibonacci sequence. Use a break statement to stop the sequence
   if it exceeds 1000.

4. Create a function called 'safe_divide' that takes two parameters (a numerator and a denominator)
   and returns the result of their division. If the denominator is zero, the function should
   return None instead of raising an error.

Remember, functions are a fundamental building block in Python programming. They allow you
to write modular, reusable code that's easier to understand and maintain. Practice creating
and using functions to become more comfortable with this important concept.
"""
