# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []

my_list.append('Miami')
my_list.append('Florida')
my_list.append([99, 100, 98])
my_list.append('Sloth')

# Then, remove the State, without using the indexes.
my_list.remove('Florida')

print(my_list)
# Bonus: Remove the last element, using a negative index.
del my_list[-1]
print(my_list)
