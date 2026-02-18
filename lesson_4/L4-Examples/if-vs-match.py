#!/usr/bin/env python3

def greeting():
    print()
    print("If-elif statement vs Match statement:")
    print()

def if_elif():
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("Your grade is A")
    elif grade >= 80:
        print("Your grade is B")
    elif grade >= 70:
        print("Your grade is C")
    elif grade >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")

# match is useful, but because of using numeric ranges, match isn't the best choice here
# you can use the 'guard' clause
def switch_case():
    grade = int(input("Enter your grade: "))
    match grade:
        case g if g >= 90:
            print("Your grade is A")
        case g if g >= 80:
            print("Your grade is B")
        case g if g >= 70:
            print("Your grade is C")
        case g if g >= 60:
            print("Your grade is D")
        case _:
            print("Your grade is F")


def main():
    greeting()
    if_elif()
    switch_case()


if __name__ == "__main__":
    main()

