#!/usr/bin/env python3

# Practice 6: Text replacement and letter counting
# Write a program that takes three user's inputs:
# A sentence
# A word to replace
# Letter to count
# Provide two outputs
# The sentence replacing all "word to
# replace" with REPLACED
# The number of occurrences of the
# given letter to count in the sentence

# Corrected Code

sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")

replaced_sentence = sentence.replace(new_word, "REPLACED")
print(replaced_sentence)
print(replaced_sentence.count(letter))

