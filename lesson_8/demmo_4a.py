#!/usr/bin/env python3

# DEMO 4: USING A FUNCTION
# define the function to check if a leap year or not.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            print(f'{year} is a leap year')
        else:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                print(f'{year} is NOT a leap year')
    else:
        print(f'{year} is NOT a leap year')

# Call the function once and have it iterate over a list of the years
for year in [2000, 2001, 2002, 2003, 2004, 2005]:
    is_leap_year(year)

# this is what it's meant when someone says that
# "Functions create re-usable code"
for year in [2020, 2021, 2022, 2023, 2024, 2025]:
    is_leap_year(year)
