# Given the string "Python programming is fun!"

# 1. Slice the string and print the substring "programming".
# 2. Slice the string and print the substring "programming is fun!"
# 3. Slice the string and print the substring “Ph rgmn sfn”
#string = "Python programming is fun!"



#string = "Python programming is fun!"

#print(len(string))  # 26 characters


# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# P  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g     i  s     f  u  n  !

# -26-25-24-23-22-21-20-19-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  P  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g     i  s     f  u  n  !

# the p in programmin is the 7th item
# extract the word 'programming' [7:18]
# The slice [7:18] extracts exactly 11 characters that spell "programming".
 # programming
#print(string[7:])    # 'programming is fun!'
#print(string[::3])

string = "Python"
print(string[5:3:-1])

text = "Python is amazing!"



