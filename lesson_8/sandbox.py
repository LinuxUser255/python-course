#!/usr/bin/env python3

def is_even(number):
    return number % 2 == 0

num = 10
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is not even.")
