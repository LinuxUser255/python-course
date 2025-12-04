string = "Python"
sliced_text = string[2:5]
print(sliced_text)  # Output: tho

text = "Python"
sliced_text = text[0:6:2]
print(sliced_text)  # Output: Pto

string = "Python is amazing!"
reversed_string = string[::-1]
print(reversed_string)  # Output: !gnizama si nohtyP # <-- Python is amazing! (in reverse)

string = "Python programming is fun!"
substring = string[7:18]
print(substring)  # Output: programming

string = "Python"

# Omitting start (defaults to 0)
print(string[:3])  # Output: Pyt

# Omitting end (defaults to length of string)
print(string[3:])  # Output: hon

# Omitting both (creates a copy of the string)
print(string[:])  # Output: Python

# Using negative indices
string = "Python"
print(string[-3:-1])  # Output: ho   (Pyt  ho  n)  #
                                                  #


string = "Python programming"
# Get every 3rd character
print(string[::3])  # Output: Ph oa

# output: mropn

string = "Python programming"
print(string[-5:-15:-2]) # mropn
