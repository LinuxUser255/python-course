#!/usr/bin/env python3

# begin with empty list
my_list = []


# You can use "append", which adds a single item to the end of the list.
my_list.append('Raleigh')
print(f"After append: {my_list}")  # ['Raleigh']


# You can use "insert" to add an element at a specific position
my_list.insert(0, 'Durham')  # Insert at beginning
print(f"After insert at beginning: {my_list}")  # ['Durham', 'Raleigh']


my_list.insert(1, 'Chapel Hill')  # Insert in middle
print(f"After insert in middle: {my_list}")  # ['Durham', 'Chapel Hill', 'Raleigh']


# You can use "extend" to add multiple elements at once
my_list.extend(['Cary', 'Apex'])
print(f"After extend: {my_list}")  # ['Durham', 'Chapel Hill', 'Raleigh', 'Cary', 'Apex']


# To remove items from the list, you use the "del" statement with the index
del my_list[1]  # Remove 'Chapel Hill'
print(f"After del at index 1: {my_list}")  # ['Durham', 'Raleigh', 'Cary', 'Apex']


# You can also remove by value using "remove()" - removes first occurrence
my_list.remove('Raleigh')
print(f"After remove 'Raleigh': {my_list}")  # ['Durham', 'Cary', 'Apex']


# "pop()" removes an element at a specific index and returns it
popped_city = my_list.pop(1)  # Remove 'Cary'
print(f"Popped city: {popped_city}")  # 'Cary'
print(f"After pop at index 1: {my_list}")  # ['Durham', 'Apex']


# Without an index, pop() removes the last element
last_city = my_list.pop()  # Remove 'Apex'
print(f"Last city popped: {last_city}")  # 'Apex'
print(f"After pop last: {my_list}")  # ['Durham']


# Let's add more elements to demonstrate sorting
my_list.extend(['Winston-Salem', 'Charlotte', 'Asheville'])
print(f"Extended list: {my_list}")  # ['Durham', 'Winston-Salem', 'Charlotte', 'Asheville']


# "sort()" sorts the list in-place (alphabetically for strings)
my_list.sort()
print(f"After sort: {my_list}")  # ['Asheville', 'Charlotte', 'Durham', 'Winston-Salem']


# "reverse()" reverses the order of elements in-place
my_list.reverse()
print(f"After reverse: {my_list}")  # ['Winston-Salem', 'Durham', 'Charlotte', 'Asheville']


# "clear()" removes all elements from the list
my_list.clear()
print(f"After clear: {my_list}")  # []

'''
# Warning: Using "del" directly on the list itself removes the whole list from memory
# del my_list  # This would delete the list completely
# print(my_list)  # This would raise a NameError

'''
# index       0         1         2       3       4
cars = ['Honda', 'Ferrari', 'Kia', 'Toyota', 'BMW']
# to delete an item using this method, the syntax is:
# list_name[index number]
# del cars[0] # delets Honda from the list.



