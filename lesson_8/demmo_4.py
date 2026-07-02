#!/usr/bin/env python3

# Without functions
# If I have 6 years, how many times do I copy
# this if/else block?
# 6 times. What if it has a bug?
# Then you got a lot of code to pick through
year_1 = 2000
year_2 = 2001
#year_3 = 2002
#year_4 = 2003
#year_5 = 2004
#year_6 = 2005

# Check if year_1 is a leap year or not
if year_1 % 4 == 0:
    if year_1 % 100 != 0:
        print(f'{year_1} is a leap year_1')
    else:
        if year_1 % 400 == 0:
            print(f'{year_1} is a leap year_1')
        else:
            print(f'{year_1} is NOT a leap year_1')
else:
    print(f'{year_1} is NOT a leap year_1')

# Then rewrite the entire if statement again to check.
# Check if year_2 is a leap year or not
if year_2 % 4 == 0:
    if year_2 % 100 != 0:
        print(f'{year_2} is a leap year_1')
    else:
        if year_1 % 400 == 0:
            print(f'{year_2} is a leap year_1')
        else:
            print(f'{year_2} is NOT a leap year_1')
else:
    print(f'{year_2} is NOT a leap year_1')


# Check if year_3 is a leap year or not

# Check if year_4 is a leap year or not

# Check if year_5 is a leap year or not

# Check if year_6 is a leap year or not


