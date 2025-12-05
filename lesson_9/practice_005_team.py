#!/usr/bin/env python3

"""
  Create a program, that
  takes a word input from the user,
  and prints out a dictionary
  show the letter count for each letter in the word.
  This version breaks the problem into smaller functions
  And calls these functions in the main function, using name guarding

   # Each function has ONE responsibility:
  count_letters()    # Only counts letters
  get_user_input()   # Only gets input
  display_result()   # Only handles output
  word_processor()   # Only coordinates flow
"""

def count_letters(word):
    """Count the occurrence  of each letter in a word and return as dictionary."""
    letter_count = {}
    for character in word:
        letter_count[character] = letter_count.get(character, 0) + 1
    return letter_count


def get_user_input():
    """Get user input for a word."""
    return input("Enter a word (or 'end' to quit): ")


def display_result(word, letter_dict):
    """Display the result of letter count for a word."""
    print(f"{word} -> {letter_dict}")


def word_processor():
    """function that processes user input and displays letter count."""
    print("Enter words to count letters, type 'end' or press Enter to quit.\n")
    while True:
        word = get_user_input()
        if word == "end" or word == "":
            break

        letter_dict = count_letters(word)
        display_result(word, letter_dict)


def main():
    """Call the main function to start the program."""
    word_processor()


# name guard to ensure this script is not run as a module.
if __name__ == "__main__":
    main()
