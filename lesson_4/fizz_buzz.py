"""
Most Pythonic FizzBuzz
  No need to check "both" separately
  Naturally handles the FizzBuzz case
  More extensible (easy to add "Jazz" for divisible by 7, etc.)
  Uses or for elegant default
"""


def fizz_buzz(number):
    result = ""

    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"

    print(result or number)  # Print result if not empty, else number


# Test it
fizz_buzz(9)  # Fizz
fizz_buzz(10)  # Buzz
fizz_buzz(15)  # FizzBuzz divisible by both 3 and 5
fizz_buzz(7)  # 7
