#!/usr/bin/env python3



def multiply_wrong(a, b):
    """WRONG: Only prints, doesn't return."""
    print('multiply_wrong function')
    result = a * b
    print(result)  # Just shows it
    # Missing return!
    print()

def multiply_correct(a, b):
    print('multiply_correct function')
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
