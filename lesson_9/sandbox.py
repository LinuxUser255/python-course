#!/usr/bin/env python3

# Create a program, that takes a word input from the user, and prints out a
# dictionary showing the letter count for each letter in the word.
# Examples:
# cat -> {"c" : 1, "a" : 1, "t" : 1}
# call -> {"c" : 1, "a" : 1, "l" : 2}
# Use as many of the following concepts as you can:
# - Functions
# - Dictionaries
# - Asking for user input
# - Loops
# Bonus: Keep asking for words until the user types "end" OR an empty word.

def process_word(word):
    letters = {}      # input the word "call"
    for character in word:
        if character not in letters.keys():
            letters[character] = 1
        else:
            letters[character] += 1   # after "call" -> letters["c"] = 2, letters["a"] = 1, letters["l"] = 2
    print(letters)

def word_processor():
    while True:
        word = input("Enter a word: ")
        if word == "end" or word == "":
            break

        # calling the first function to process the word
        process_word(word)


def main():
    word_processor()


if __name__ == "__main__":
    main()