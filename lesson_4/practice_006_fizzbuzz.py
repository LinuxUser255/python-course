# Create a variable called number. Set it to any integer.
# If the number is divisible by 3, print 'Fizz'
# If the number is divisible by 5, print 'Buzz'
# If the number is divisible by both 3 and 5, print 'FizzBuzz'

number = 0

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
