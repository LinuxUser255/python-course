#!/usr/bin/env python3


def main():
    """
    Create a variable called number. Set it to any integer.
    - If the number is divisible by 3, print ‘Fizz’
    - If the number is divisible by 5, print ‘Buzz’
    - If the number is divisible by both 3 and 5, print ‘FizzBuzz’
    """
    number = 15

    if number % 3 == 0 and number % 5 == 0:
        print(f"The number is {number}, so FizzBuzz")
    elif number % 3 == 0:
        print(f"The number is {number}, so Fizz")
    elif number % 5 == 0:
        print(f"The number is {number} , so Buzz")
    else:
        print(f"{number}..nope")


if __name__ == "__main__":
    main()

