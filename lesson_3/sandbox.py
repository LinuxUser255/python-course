#!/usr/bin/env python3
"""
PRACTICE 6 PAGE 24
Bug in the code
    Write a program that takes three user's inputs:
    You need to provide two outputs:

    sentence = input("enter a sentence: ")
    new_word = input("enter the word to replace: ")
    letter = input("enter the letter to count: ")

Example:
    Enter a sentence: I love cats and dogs, but cats are my favorite.
    Enter the word to replace: cats
    Enter the letter to count: o
    Expected output:
    I love REPLACED and dogs, but REPLACED are my favorite.

    ● The sentence replacing all "word to
      replace" with REPLACED
    ● The number of occurrences of the
      given letter to count in the sentence
    ● A sentence
    ● A word to replace
    ● Letter to count

"""



sentence = input("enter a sentence: ")
new_word = input("enter the word to replace: ")
letter = input("enter the letter to count: ")

#NO
# print(sentence.replace(new_word, sentence))
print(sentence.replace(new_word, "REPLACED"))
print(sentence.count(letter))


#print(sentence.replace(new_word, sentence))
#print(sentence.count(letter))

