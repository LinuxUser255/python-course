# Create a program, that
# takes a word input from the user,
# and prints out a dictionary
# show the letter count for each letter in the word.

def count_letters(word):
    """Count the occurrence  of each letter in a word and return as dictionary."""
    letter_count = {}
    for character in word:
        letter_count[character] = letter_count.get(character, 0) + 1
    return letter_count


def get_user_input():
    return input("Enter a word (or 'end' to quit): ")


def display_result(word, letter_dict):
    print(f"{word} -> {letter_dict}")


def word_processor():
    print("Enter words to count letters, type 'end' or press Enter to quit.\n")
    while True:
        word = get_user_input()
        if word == "end" or word == "":
            break

        letter_dict = count_letters(word)
        display_result(word, letter_dict)

def main():
    word_processor()


if __name__ == "__main__":
    main()
