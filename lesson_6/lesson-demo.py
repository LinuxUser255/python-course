# LESSONS: DEMO

# LISTS
#-------------------------------------------------------

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

# EXAMPLE LISTS
#electronics = ['Laptop', 'Smartphone', 'Tablet', 'Camera', 'Smartwatch']

#colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']

#fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango']

#countries = ['USA', 'Canada', 'Germany', 'Japan', 'India']

#sports = ['Soccer', 'Basketball', 'Tennis', 'Cricket', 'Baseball']

#languages = ['Python', 'JavaScript', 'Rust', 'Go', 'C++']

#animals = ['Dog', 'Cat', 'Elephant', 'Tiger', 'Zebra']

#location = ['Raleigh', 'North Carolina', [85, 90, 78]]


# 1.  PROPERTIES OF LISTS: ZERO-BASED INDEXING
# Indexes     0        1        2       3        4
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']

students[0]
students[1]
students[2]
students[3]
students[4]
print(students[0])

print(students[1])
del students[1]

print(students)
# change the 0s from 0 - 4
# Put your cursor on the first 0 in the column (in students[0]).
# Enter Visual Block Mode:
# Press Ctrl + v
# Use j to highlight down to the last 0.
# Press g (this begins a special command).
# Then press Ctrl + a (this tells Neovim to increment each number).

# Indexing is always consistent,
# regardless of how the contents change.

# del students[1]

# One could expect the list to end up like this:

# students[0]: 'Joseph'
# students[2]: 'Eric'
# students[3]: 'Tom'

# String methods to add and remove elements:
# .append()
# .insert()
# .remove()
# .pop()
# .sort()
# .sorted()
# .reverse()
# del[] an indexed element
















# 2.  PROPERTIES OF LISTS: MUTABILITY
# create a list
mutable_list = [1, 'Joe', True]
print(mutable_list)

# Remove Index 1 of the list  del-->  del list_name[]


# Change the value of an element.
mutable_list[1] = 'Kelly'
print(mutable_list)
print()
mutable_list.append('Chris')
print(mutable_list)
print()
mutable_list.insert(0, 'foo')
print(mutable_list)
print()
print()



# Add more elements at the end, use the append() method.
# these methods and functions can be too
# .append() .insert() .remove() .pop() .sort() .sorted() .reverse() del[] an indexed element

















# 3.  PROPERTIES OF LISTS: ORDERED
# Create an empty list.
append_list = []

append_list.append('Alice')
append_list.append('bob')
append_list.append('kelly')

# use the .apnped() sting method to Add a few items in a particular order.


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
#print(het_list_vert)














# 5.  CREATING LISTS
# You can create an empty list by using empty square brackets []

# You can create a pre-populated list by declaring the elements inside the brackets.

# You can also use variables.

# REMEMBER: You can mix and match data types. Even other lists!
















# 6.  RETRIEVING INDIVIDUAL ELEMENTS
# Indexes 0 1 2 3 4

print()
print()














# 7.  PRACTICE! & SOLUTION  RETRIEVING INDIVIDUAL ELEMENTS
# Create a list that holds the following information about your location.
# - The first element should be the city name.
# - The second element should be the state or province.
# - The third element should be a list containing the maximum temperatures
# of the last three days.
location = ['Raleigh', 'North Carolina', [85, 90, 78]]

# Print statments to display city, state, and temperatures, use index[0]
print(location[0])
print(location[1])
print(location[2])


# Bonus: The first temperature of the list of temperatures
print(location[2][0])


print()
print()
print()
print()
print()





















# 8.  ADD AND REMOVE ELEMENTS
# String methods to add and remove elements:
# .append()
# .insert()
# .remove()
# .pop()
# .sort()
# .sorted()
# .reverse()
# del[] with an indexed element

# We will start with an empty list, but you could also start with a pre-populated list.
add_and_remove_elements = []

# You can use "append", which adds a single item to the end of the list.
add_and_remove_elements.append('Raleigh')
add_and_remove_elements.append('Miami')
del add_and_remove_elements[1] #
print(add_and_remove_elements)

print()
# add miami an las vegas
print()
add_and_remove_elements.append('Las Vegas')
# add Chapel Hill, then remove Miami from the list
# Can also use .pop(), and .remove() to remove an element by value.


# You can also remove by value .remove() .pop()


pop_this_element = add_and_remove_elements.pop(1) # Miami

# AND YES, YOU CAN PRE-PEND ELEMENTS TO THE LIST USING THE .INSERT() METHOD
languages = ['Python', 'JavaScript', 'Rust', 'Go', 'C++']
# listname.insert(index number, the element)
# .insert() # insert Haskell at the beginning of the list
#print(languages)




















# 9. PRACTICE: Add and Remove  Similar to the other one with state and cities
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
work_location.append('North Carolina')


# - A list with the temperatures the last three days
work_location.append([85, 90, 78])


# - Your favorite animal
work_location.append('cats')
print(work_location)


# Then, remove the State, WITHOUT USING THE INDEXES.
# Hint, you'll use the exact name of the state.

# Bonus: Remove the last element, using a negative index..
# lsit del[]
#print()

# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []
my_list.append("Houston")
my_list.append("Texas")
my_list.append([101, 102, 103])
my_list.append("Sloth")

# Then, remove the State, without using the indexes.
my_list.remove("Texas")

# Bonus: Remove the last element, using a negative index.
del my_list[-1]
print(my_list)


















print()



# 10. CHECK IF AN ELEMENT EXISTS
# An easy way to check if an element exists in a list,
# is to use the “in” or “not in” statements

work_location = ['Raleigh', 'North Carolina', 'Houston', 'New York']

print('Raleigh' in work_location) # city
#print('North Carolina') # State

# This one prints FALSE, why?
#print(101 in work_location)

#print(101 in students[2]) # Prints True
#
# using it as part of an 'if' statement.
if 'Raleigh' in work_location:
    print('Raleigh was found in the list')

if 'Chapel Hill' not in work_location:
    print('Chapel Hill was found in the list')


print()


















# 11. SORT A LIST
#!!! DEMONSTRATE THIS IN SORTING.PY !!!
"""
SORT() VS SORTED()

Clear the confusion
===================
Key Differences Between sort() and sorted()
Return Value:

sort() is a METHOD that modifies the list in-place and returns None
sorted() is a FUNCTION that returns a new sorted list without modifying the original

MUTABILITY:
============
sort() permanently changes the order of the original list
sorted() leaves the original list unchanged

Applicability:
===============
sort() only works on lists
sorted() works on any iterable (lists, tuples, strings, etc.)

"""
# .sort()
# .sorted()

# Sorting in place: Use this when the original order is not important. Saves memory.

# Sorting to a new copy:
# Use this when the original order is important.
# this one uses the .sorted() and the syntax is a bit different
print( )
print( )

# Example showing the difference between sort() and sorted()
cars = ['Toyota', 'Honda', 'BMW', 'Kia', 'Ford']
print('Original list of cars:')
print(cars)
print()

# Using sorted() - creates a new sorted list without changing original
print('Using sorted() - returns a new sorted list:')
sorted_cars = sorted(cars)
print(f"sorted_cars = {sorted_cars}")
print(f"Original cars list = {cars}")  # Original list remains unchanged
print()

# Using sort() - modifies the original list
print('Using sort() - modifies the original list:')
cars.sort()
print(f"After cars.sort(), cars = {cars}")  # Original list is now sorted
print()

# You can still modify the list after sorting
print('Modifying the list after sorting:')
cars.append('Mercedes')
print(f"After adding 'Mercedes', cars = {cars}")  # List is modified but still sorted up to the new addition



print()
print()


















# 12. REVERSE A LIST
# Reversing in place using the
# .reverse() method, which reverses the original list.
# In-place reversal
#rv_list = [10, 4, 8, 3, 1]
#rv_list.reverse()
#print(rv_list)  # [1, 3, 8, 4, 10]
print()

# Creating a new reversed list
num_list = [10, 4, 8, 3, 1]
reversed_list = list(reversed(num_list))
print(reversed_list)  # [1, 3, 8, 4, 10]

print()
print()

# List of students
#students = ['Mike', 'John', 'Sarah', 'David', 'Emily']





















# 13. PRACTICE! & SOLUTION
# Create a list that contains the ingredients for a sandwich. Yum.🥪
# If you want to use an empty list and add stuff to it, or start
# with a pre-populated list is up to you.

# Some people like cheese, some people don't. ONLY add cheese to your
# list of ingredients if you really like cheese.🧀
sandwich = ["bread", "ham", "tomato", "cheese"]

if "cheese" in sandwich:
    print("i love cheese! ���")
else:
    print("i don't like cheese. ��")

sandwich.sort()
print(sandwich)


# Then, use an if/else statement to print a message that will tell us
# whether you like cheese, based on its presence in the list.
# use the 'in' keyword ... is sandwich




# Then, to make it look pretty, sort the list in alphabetical order and print it out.
# Our computer is very old and it doesn't have a lot of memory. Also, we don't care
# about the original order of the ingredients.


#print(students)






















# 14. CONCATENATION
# Concatenation means stitching stuff together using the + operator
# When you concatenate lists, the order of the elements is preserved
my_list_1 = ["Joseph", "Kelly"]
my_list_2 = ["Tom", "Bernard"]

my_catted_list = my_list_1 + my_list_2
print(my_catted_list)

# Another way to stitch lists together is to multiply them with
# the * operator, which repeats them.
# students = [1, 2, 3]
# my_repeated_list = students * 3
# print(my_repeated_list) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Create a list that contains the ingredients for a sandwich. Yum.🥪
# If you want to use an empty list and add stuff to it, or start
# with a pre-populated list is up to you.
# Some people like cheese, some people don't. ONLY add cheese to your
# list of ingredients if you really like cheese.🧀

my_list = ["bread", "ham", "tomato", "cheese"]

# Then, use an if/else statement to print a message that will tell us
# whether you like cheese, based on its presence in the list.

if "cheese" in my_list:
 print("I love cheese")
else:
 print("I hate cheese")

# Then, to make it look pretty, sort the list in alphabetical order and print it out.
# Our computer is very old and it doesn't have a lot of memory. Also, we don't care
# about the original order of the ingredients.












print()

print()


# 15. LIST SLICING
# Slicing is used to extract a contiguous portion of a list
# The original list remains unchanged


print()
print()
my_list = [0, 1, 2, 3, 4, 5, 6]

# Basic slicing: [start:end] (end is exclusive)
print(my_list[1:4])  # [1, 2, 3]

# With step: [start:end:step]
print(my_list[0:7:2])  # [0, 2, 4, 6]

# Defaults
print(my_list[:])  # Entire list
print(my_list[2:])  # From index 2 to end
print(my_list[:3])  # From start to index 3 (exclusive)


print()
print()


#------------------------------------------------------------#
# OPTIONAL STEP PARAMETER to extract every N elemets
#------------------------------------------------------------#

slice_param = ["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]

# Stepped slicing, get every N items.
# Python will take N steps before grabbing an element.

my_slice = students[::2] # ['Joseph', 'Eric', 'Bernard', 'Josh']
my_slice = students[0:4:2] # ['Joseph', 'Eric']
print(my_slice)












print()

# 16. PRACTICE! & SOLUTION CONCATENATION
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
print(week_1[::2])


print()


















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

# Use students.index() to find the index of an element.
students = ["Joseph", "Kelly", "Tom"]
students.index("Kelly") # 1
students.index("Tom") # 2

# Use students.count() to find out how many times an element is in the list.
students = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
students.count(2) # 1
students.count(4) # 2
students.count(6) # 3
students = [True, True, False]
students.count(True) # 2
students.count(False) # 1











# 19. PRACTICE! & SOLUTION AGGREGATORS & HELPERS
# A company opened in 2010 and ceased operations in 2014.
# Imagine the following list contains the number of
# employees the company for each yeareekend_d:

print()
# Year: 2010 2011 2012 2013 2014
employees = [ 93, 104, 89, 101, 93]

# We would like to know the following
# 1. What's the lowest number of employees the company ever had?
print(min(employees)) # 89

# 2. What's the highest number of employees the company ever had?
print(max(employees)) # 104

# 3. What's the total head count if all employees were different every year?
print(sum(employees)) # 480

# 4. How many years had 93 employees?
print(employees.count(93)) # 2 (2010 and 2014)

# 5. Can you think of a way to determine how many years the company was in business?
# Hint: If it's one list element per year, maybe you can count the number of elements.
print(len(employees)) # 5

print()



# CONGRATULATIONS!
# You finished Lists,
# BUT WAIT THERE'S MORE

# ...

# .....

# ......








# EXTRA [SELF-STUDY]: TUPLES

# Tuples are like lists but immutable
# When declaring a tuple, you have to pre-populated. You can’t add elements later.
my_tuple = ("Joseph", "Kelly", 1, 2, 3, [100, 200, 300])

# This won't work
#my_tuple.append("Eric")
#my_tuple.remove("Joseph")

# This works just fine
my_tuple.index("Kelly") # 1
my_tuple.count("Joseph") # 1
print(my_tuple[1]) # Kelly1

# ANNOYANCE: If you ever need a tuple with a single element,
# you have to include a trailing comma.
#my_tuple = ("Joseph", )
print()
# Extra Sets:
# Sets have a variety of methods and functions that allow you to manipulate them. Here’s a few:
# Create a set.
my_set = {"Joseph", "Kelly"}
print(my_set) # {'Kelly', 'Joseph'}

print()
# Adding my name again doesn't make it show twice due to uniqueness.
my_set.add("Joseph")
print(my_set) # {'Kelly', 'Joseph'}

# Remove an element using remove(). If you try to remove an element that doesn't exist,
# you get an error.
my_set.remove("Joseph") # Removes the element.

# ANNOYANCE: You have to use set() to create an empty set, as {} is used to declare a dictionary.
#my_empty_set = {} # NOT what you want. This creates a dictionary.
#my_empty_set = set() # THIS is what you want. This creates an empty set


# Extra: Sets
# Sets have a variety of methods and functions that allow you to manipulate them. Here’s a few:
# Create a set.
my_set = {"Joseph", "Kelly"}
print(my_set) # {'Kelly', 'Joseph'}

# Adding my name again doesn't make it show twice due to uniqueness.
#my_set.add("Joseph")
#print(my_set) # {'Kelly', 'Joseph'}

# Remove an element using remove(). If you try to remove an element that doesn't exist,
# you get an error.
#my_set.remove("Joseph") # Removes the element.
#my_set.remove("Joseph") # Raises a KeyError, as the element doesn't exist anymore.
#my_set.discard("Joseph") # Same as remove(), but doesn't raise an error if it doesn't exist.

# ANNOYANCE: You have to use set() to create an empty set, as {} is used to declare a dictionary.
#my_empty_set = {} # NOT what you want. This creates a dictionary.
#my_empty_set = set() # THIS is what you want. This creates an empty set



# List comprehensions are a concise way to create lists.
# Traditional way
#squares = []
#for x in range(10):
#    squares.append(x**2)
#print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# Using list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

