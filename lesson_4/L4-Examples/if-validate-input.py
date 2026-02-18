#!/usr/bin/env python3

# Code execution flow chart
# ┌─────────────────────────────────────────────────────────────┐
# │ main()                                                      │
# │   └─> check_if_number()                                    │
# │         └─> grade = "85" (local variable, string)          │
# │             └─> check_grade(int(grade))                    │
# │                      │                                      │
# │                      │ Passes: 85 (integer)                │
# │                      ▼                                      │
# │                 check_grade(grade)  ← Parameter receives 85│
# │                      │                                      │
# │                      └─> Uses grade in comparisons         │
# └─────────────────────────────────────────────────────────────┘
# The interface / Connection between the two funtions is the function call with an arg
# check_grade(int(grade))
#     ▲          ▲
#     │          │
#  Function   Argument (value being passed)
#   name
#
# - Argument: The actual value passed when calling the function
# - Parameter: The variable name in the function definition that receives the value

def check_if_number():
    """validate numerical input"""
    grade = input("Enter your grade (0-100): ")
    if grade.isdigit() and 0 <= int(grade) <= 100:
        # convert to integer for grade comparison)
        check_grade(int(grade)) # <- CRITICAL LINE: Passes the int as an ARGUMENT to the grade Parameter
    else:
        print("Enter a numerical digit between 0 and 100.")

def check_grade(grade): # The Prameter `grade` receives the validated user input
    """check if the student got an A, B, C, D, or F"""
    if grade >= 90:
        print("Your grade is an A!")
    elif grade >= 80:
        print("Your grade is a B!")
    elif grade >= 70:
        print("Your grade is a C!")
    elif grade >= 60:
        print("Your grade is a D!")
    else:
        print("Your grade is an F!")


def main():
    check_if_number()
    # check_grade() no need to call it here, it's called inside check_if_number()


if __name__ == "__main__":
    main()
