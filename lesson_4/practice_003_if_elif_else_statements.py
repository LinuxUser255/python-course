# You're creating a program to determine eligibility for a discount. Here's what you need to do:
# Take user's age and income as input:


# Now, apply the following conditions and print messages accordingly:
# If the person is both 18 years or older and has an income of $1000 or less, print 'You qualify for the discount!'
# If the person is less than 18 years or has an income of $0, print 'You get a special discount!'
# If the person is neither qualified for the first nor the second discount, print 'Sorry, you are not eligible for any discount.'

# Remember to use the and, or operators to combine conditions as needed.
age = int(input('Enter your age: '))
income = int(input('Enter your monthly income: '))

# wer're dealing with age and income
if age >= 18 and income <= 1000:
    print('You qualify for the discount!')
elif age < 18 or income == 0:
    print('You get a special discount!')
else:
    print('Sorry, you are not eligible for any discount.')


