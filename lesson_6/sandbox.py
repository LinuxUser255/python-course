#!/usr/bin/env python3

# LISTS

# Table of Contents
# 1.  Properties of Lists: Zero-Based Indexing
# 2.  Properties of Lists: Mutability
# 3.  Properties of Lists: Ordered
# 4.  Properties of Lists: Heterogeneity
# 5.  Creating lists
# 6.  Retrieving individual elements
# 7.  Practice! & Solution
# 8.  Add and Remove Elements
# 9.  Practice!
# 10. Check if an element exists
# 11. Sort a list
# 12. Reverse a list
# 13. Practice! & Solution
# 14. Concatenation
# 15. List slicing
# 16. Practice! & Solution
# 17. Aggregators
# 18. Helpers
# 19. Practice! & Solution
# Congratulations!
# Extra [self-study]: Tuples


# 1.  PROPERTIES OF LISTS: ZERO-BASED INDEXING
# Indexes     0        1        2       3
my_list = ['Joseph', 'Kelly', 'Eric', 'Tom']

# delete an indexed element
# print()
















# 2.  PROPERTIES OF LISTS: MUTABILITY
# create a list
mutable_list = [1, 'Joe', True]

# Remove Index 1 of the list  del-->  del list_name[]


# Change the value of an element.
# mutable_list[1] = 'Kelly'


# Add more elements at the end, use the append() method.
# these methods and functions can be too
# .append() .insert() .remove() .pop() .sort() .sorted() .reverse() del[] an indexed element

















# 3.  PROPERTIES OF LISTS: ORDERED
# Create an empty list.
append_list = []

# use the .append() sting method to Add a few items in a particular order.


# print the items






















# 4.  PROPERTIES OF LISTS: HETEROGENEITY
het_list = [1, 2, 3, 4, 5]
#het_list = ["Joseph", "Kelly", "Eric"]
#het_list = [True, True, False]
#het_list = [None, None, None]

# Store different data types at the same time, even other lists and other collection types.
het_list_vert = [
     1, # Integers
     2.00, # Floats
     True, # Booleans
     "Joseph", # Strings
     None, # None (Python's NULL)
     [100, 200, 300], # Other lists
     {'Cars', 'Motorcycles'},
]
print(het_list_vert)














# 5.  CREATING LISTS
# You can create an empty list by using empty square brackets []
some_empty_list = []

# You can create a pre-populated list by declaring the elements inside the brackets.
pre_pop_list = [1, 2, 3]

# You can also use variables.
employee_1 = 'Joseph'
employee_2 = 'Mike'

employee_list = [employee_1, employee_2]

# REMEMBER: You can mix and match data types. Even other lists!
mixed_list = [1, 1.00, False, None, ['Joseph', 'Kelly']]
















# 6.  RETRIEVING INDIVIDUAL ELEMENTS
# Indexes 0 1 2 3 4
some_elements = ["Joseph", "Kelly", "Eric", "Tom", [100, 200]]

# Access individual elements directly using "positive indexing".

# Access elements from the end of the list using "negative indexing".

# Access a list element inside another list




















# 7.  PRACTICE! & SOLUTION
# Create a list that holds the following information about your location.
# - The first element should be the city name.
# - The second element should be the state or province.
# - The third element should be a list containing the maximum temperatures
# of the last three days.
location = ['Raleigh', 'North Carolina', [85, 90, 78]]





















# 8.  ADD AND REMOVE ELEMENTS
# String methods to add and remove elements:
# .append()
# .insert()
# .remove()
# .pop()
# .sort()
# .sorted()
# .reverse()

# del[] an indexed element




# We will start with an empty list, but you could also start with a pre-populated list.
add_and_remove_elements = []

# You can use "append", which adds a single item to the end of the list.
add_and_remove_elements.append('Raleigh')
add_and_remove_elements.append('Miami')
add_and_remove_elements.append('Las Vegas')


# To remove items from the list, you use the "del" statement, with the index.
# Warning: Using "del" directly on the list itself removes the whole list from memory.

# You can also remove by value .remove() .pop()
add_and_remove_elements.remove('Raleigh')

pop_this_element = add_and_remove_elements.pop(1) # Miami



# AND YES, YOU CAN PRE-PEND ELEMENTS TO THE LIST USING THE .INSERT() METHOD
languages = ['Python', 'JavaScript', 'Rust', 'Go', 'C++']

# listname.insert(index number, the element)
languages.insert(0, 'Haskell')
#print(languages)

# This formula can be used to insert an Element anywhere in the list
# listname.insert(index number, the element)
languages.insert(1, 'TypeScript')
#print(languages)




















# 9.  PRACTICE!
# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal
# use the .append() method
work_location = []

# - City
work_location.append('Raleigh')

# - State or Province

# - A list with the temperatures the last three days

# - Your favorite animal


# Then, remove the State, without using the indexes.

# Bonus: Remove the last element, using a negative index.
#print(work_location)























# 10. CHECK IF AN ELEMENT EXISTS
# An easy way to check if an element exists in a list, is to use the “in” or “not in” statements
#work_location = []
#
#print('Raleigh' in work_location) # city
#print('North Carolina') # State
#
## This one prints FALSE, why?
#print(101 in work_location)
#
#print(101 in my_list[2]) # Prints True
#
## using it as part of an 'if' statement.
#if 'Raleigh' in work_location:
#    print('Raleigh was found in the list')
#
#if 'Chapel Hill' not in work_location:
#    print('Chapel Hill was found in the list')





















# 11. SORT A LIST
# .sort()
# .sorted()

# Sorting in place: Use this when the original order is not important. Saves memory.
sort_list = [5, 4, 7, 2, 1]

# Sorting to a new copy:
# Use this when the original order is important.
# this one uses the .sorted() and the syntax is a bit different

sort_list = [5, 4, 7, 2, 1]
# LIST_NAME = SORTED(LIST_NAME)






















# 12. REVERSE A LIST
# Reversing in place using the .reverse() method, which reverses the original list.
reverse_list = [5, 4, 7, 2, 1]

# Reversing to a new copy of the list using the "reversed" function,
# which leaves the original list unchanged, but needs to be cast to a list.
# my_list = [5, 4, 7, 2, 1]































# 13. PRACTICE! & SOLUTION
# Create a list that contains the ingredients for a sandwich. Yum.🥪
# If you want to use an empty list and add stuff to it, or start
# with a pre-populated list is up to you.

# Some people like cheese, some people don't. ONLY add cheese to your
# list of ingredients if you really like cheese.🧀
# my_list = []

# Then, use an if/else statement to print a message that will tell us
# whether you like cheese, based on its presence in the list.




# Then, to make it look pretty, sort the list in alphabetical order and print it out.
# Our computer is very old and it doesn't have a lot of memory. Also, we don't care
# about the original order of the ingredients.


#print(my_list)






















# 14. CONCATENATION
# Concatenation means stitching stuff together using the + operator
# When you concatenate lists, the order of the elements is preserved
my_list_1 = ["Joseph", "Kelly"]
my_list_2 = ["Tom", "Bernard"]

# my_catted_list = first_list

# Another way to stitch lists together is to multiply them with
# the * operator, which repeats them.
# my_list = [1, 2, 3]
# my_repeated_list = my_list * 3
# print(my_repeated_list) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

















# 15. LIST SLICING
# Slicing is used to extract a contiguous portion of a list
# The original list remains unchanged

# Syntax:
# sliced_list = original_list[start:end:optional_step]
# Indexes: 0 1 2 3 4 5 6
slice_list = ["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]

# Using the slicer without any parameters just returns the original list.
#print(my_list[:]) # ["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]
#print(my_list[::]) # ["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]

# Get the first two elements.
my_slice = slice_list[0:2] # ['Joseph', 'Kelly']

# Get the second, third and fourth elements.
my_slice = slice_list[1:4] # ['Kelly', 'Eric', 'Tom']





#------------------------------------------------------------#
# OPTIONAL STEP PARAMETER to extract every N elemets
#------------------------------------------------------------#
slice_param = ["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]

# Stepped slicing, get every N items.
# Python will take N steps before grabbing an element.

my_slice = my_list[::2] # ['Joseph', 'Eric', 'Bernard', 'Josh']
my_slice = my_list[0:4:2] # ['Joseph', 'Eric']















# 16. PRACTICE! & SOLUTION
# For this exercise, you will create two lists. The first list will contain the work week days,
# the second list will contain the days of the weekend.
work_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend_days = ['saturday', 'sunday']

# Then, you need to concatenate both lists into a third new list that represents the full week.
full_week = work_days + weekend_days

# Then, can you think of an easy way to create a new list that contains the days of two full weeks?
fortnight = full_week * 2

# Finally, once you have two full weeks into a list, use the slicer to:
# 1. Extract week 1 into its own list. Use this list in the next two points.
week_1 = fortnight[0:7]

# 2. Write a slicer that will return the following: ['monday', 'wednesday', 'friday', 'sunday']
#print(week_1[::2])




















# 17. AGGREGATORS
# Aggregators are special functions that help us perform some basic list calculations

# Use min() to determine the smallest number in a list of numbers or
# the earliest alphabetical element in a list of strings. Same type only!
min([1, 2, 3]) # 1
min(['c', 'a', 'd']) # a

# Use max() exactly the same way, but for the highest value.
max([1, 2, 3]) # 3
max(['a', 'b', 'c']) # c

# Use sum() to add up the total in a list of numbers. Only things that evaluate to numbers!
sum([1, 2, 3]) # 6
sum([1, 2.0, 3.5]) # 6.5
sum([1, 2.0, 3.5, True, False]) # 7.5

















# 18. HELPERS
# Helpers can tell us some useful information about the list or its elements

# Use len() to find out the size of a list.
len([1, 2, 3, 4, 5]) # 5
len([[1, 2, 3], [4, 5, 6]]) # 2 - Why? 🤔

# Use my_list.index() to find the index of an element.
my_list = ["Joseph", "Kelly", "Tom"]
my_list.index("Kelly") # 1
my_list.index("Tom") # 2

# Use my_list.count() to find out how many times an element is in the list.
my_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
my_list.count(2) # 1
my_list.count(4) # 2
my_list.count(6) # 3
my_list = [True, True, False]
my_list.count(True) # 2
my_list.count(False) # 1











# 19. PRACTICE! & SOLUTION
# A company opened in 2010 and ceased operations in 2014.
# Imagine the following list contains the number of
# employees the company for each year:

# Year: 2010 2011 2012 2013 2014
employees = [ 93, 104, 89, 101, 93]

# We would like to know the following
# 1. What's the lowest number of employees the company ever had?
#print(min(employees)) # 89

# 2. What's the highest number of employees the company ever had?
#print(max(employees)) # 104

# 3. What's the total head count if all employees were different every year?
#print(sum(employees)) # 480

# 4. How many years had 93 employees?
#print(employees.count(93)) # 2 (2010 and 2014)

# 5. Can you think of a way to determine how many years the company was in business?
# Hint: If it's one list element per year, maybe you can count the number of elements.
#print(len(employees)) # 5



# CONGRATULATIONS!
# You finished Lists,
# BUT WAIT THERE'S MORE

# ...

# .....

# ......








# EXTRA [SELF-STUDY]: TUPLES

# Tuples are like lists but immutable
# When declaring a tuple, you have to pre-populated. You can’t add elements later.
#my_tuple = ("Joseph", "Kelly", 1, 2, 3, [100, 200, 300])
#
## This won't work
#my_tuple.append("Eric")
#my_tuple.remove("Joseph")
#
## This works just fine
#my_tuple.index("Kelly") # 1
#my_tuple.count("Joseph") # 1
#
## ANNOYANCE: If you ever need a tuple with a single element,
## you have to include a trailing comma.
#my_tuple = ("Joseph", )
#
## Extra Sets:
## Sets have a variety of methods and functions that allow you to manipulate them. Here’s a few:
## Create a set.
#my_set = {"Joseph", "Kelly"}
#print(my_set) # {'Kelly', 'Joseph'}
#
## Adding my name again doesn't make it show twice due to uniqueness.
#my_set.add("Joseph")
#print(my_set) # {'Kelly', 'Joseph'}
#
## Remove an element using remove(). If you try to remove an element that doesn't exist,
## you get an error.
#my_set.remove("Joseph") # Removes the element.
#my_set.remove("Joseph") # Raises a KeyError, as the element doesn't exist anymore.
#my_set.discard("Joseph") # Same as remove(), but doesn't raise an error if it doesn't exist.
#
## ANNOYANCE: You have to use set() to create an empty set, as {} is used to declare a dictionary.
#my_empty_set = {} # NOT what you want. This creates a dictionary.
#my_empty_set = set() # THIS is what you want. This creates an empty set


# Extra: Sets
# Sets have a variety of methods and functions that allow you to manipulate them. Here’s a few:
# Create a set.
#my_set = {"Joseph", "Kelly"}
#print(my_set) # {'Kelly', 'Joseph'}
#
## Adding my name again doesn't make it show twice due to uniqueness.
#my_set.add("Joseph")
#print(my_set) # {'Kelly', 'Joseph'}
#
## Remove an element using remove(). If you try to remove an element that doesn't exist,
## you get an error.
#my_set.remove("Joseph") # Removes the element.
#my_set.remove("Joseph") # Raises a KeyError, as the element doesn't exist anymore.
#my_set.discard("Joseph") # Same as remove(), but doesn't raise an error if it doesn't exist.
#
## ANNOYANCE: You have to use set() to create an empty set, as {} is used to declare a dictionary.
#my_empty_set = {} # NOT what you want. This creates a dictionary.
#my_empty_set = set() # THIS is what you want. This creates an empty set



# List comprehensions are a concise way to create lists.
# Traditional way
#squares = []
#for x in range(10):
#    squares.append(x**2)
#print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
## Using list comprehension
#squares = [x**2 for x in range(10)]
#print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
## With condition
#even_squares = [x**2 for x in range(10) if x % 2 == 0]
#print(even_squares)  # [0, 4, 16, 36, 64]










