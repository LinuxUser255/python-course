#!/usr/bin/env python3


def drink_age():
    age = int(input("Enter your age: "))

    if age >= 21:
        print("You can drink.")
    else:
        print("You can't drink.")


def main():
    drink_age()


if __name__ == "__main__":
    main()