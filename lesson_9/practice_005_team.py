#!/usr/bin/env python3

# Practice 5, basic solution

def process_character(word):
    letters = {}
    for character in word:
        if character not in letters.keys():
            letters[character] = 1
        else:
            letters[character] += 1
    print(letters)


def word_processor():
    while True:
        word = input('Word: ')
        if word == "end" or word == "":
            break
        process_character(word)

