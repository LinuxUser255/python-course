

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

word = "hannah"

if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is NOT a palindrome")


