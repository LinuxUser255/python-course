"""
Create a basic dictionary that contains the following information about
an imaginary person:

- Their name
- Their age
- Their location (city, state). Bonus points if you use a
  nested dictionary.
- Whether they’re married or not.
"""
print("Basic Dictionary")

person = {
    'name': 'John',
    'age': 23,
    'location': {
        'city': 'New York',
       'state': 'NY'
    },
    'married': False
}

print(person['location']['city'])
print()
print(person['married'])