```python
#!/usr/bin/env python3

# Practice 6: Text replacement and letter counting
# BUGFIX

# Get user inputs
sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")

# BUG #1: The solution replaces new_word with the entire sentence
# instead of replacing it with "REPLACED"
#
# BUGGY CODE:
# print(sentence.replace(new_word, sentence))
#
# CORRECTED CODE:
replaced_sentence = sentence.replace(new_word, "REPLACED")
print(replaced_sentence)

# BUG #2: Should count letters in the REPLACED sentence, not the original
# This matters when the word being replaced contains the letter to count
#
# BUGGY CODE:
# print(sentence.count(letter))
#
# CORRECTED CODE:
print(replaced_sentence.count(letter))
```