#!/usr/bin/env python3

def process_word(word):
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
        process_word(word)

word_processor()