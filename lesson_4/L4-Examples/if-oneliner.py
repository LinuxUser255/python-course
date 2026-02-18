#!/usr/bin/env python3

# is this like a ternerary operation in C?
# yes..
# The pattern is: value_if_true if condition else value_if_false
def main():
    age = int(input("Enter your age: "))
    eligible = 'can vote' if age >= 18 else 'cannot vote'
    print(eligible)


if __name__ == "__main__":
    main()

