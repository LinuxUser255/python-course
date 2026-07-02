#!/usr/bin/env python3
# Create a program that does the following:
#
# 1. Keeps asking for names, one at a time. Stop asking for names when user's input is "end".
# 2. When the user is done adding names, the program should show two lines for each name:
#    - A line with a greeting: "Hello, {name}!"
#    - A line with the first letter of the user's name: "Your initial is {initial}."
#
# Use at least one function. Extra points if you use two and call a function from another function.

def greet(name):  # <- what does this function need to receive?
    print(f"Hello, {name}!")
    print(f"Your initial is {name[0]}.")


def collect_names():
    """Continue asking for names until the user types 'end'.
    Returns: ???  <- fill this in before you write the body
    """
    names = [] # initialize an empty list
    while True:
        name = input("Enter a name (or 'end' to finish): ")
        if name == "end":
            break
        names.append(name)
    return names


def main():
    names = collect_names()
    for name in names:
        greet(name)


if __name__ == "__main__":
    main()






