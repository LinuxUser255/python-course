# THIS FILE: LESSONS-DEMO.PY is  FOR LIVE DEMONSTRATION

# LISTS
#-------------------------------------------------------

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
 # Indexes     0         1      2       3
#my_list = ['Joseph', 'Kelly', 'Eric', 'Tom']
# my_list[0]: 'Joseph'

#del my_list[1]

# For future reference
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
# Create a list.
#my_list = [1, "Joseph", True]

# Remove Index 1 of the list.
#del my_list[0] # print(my_list) # ['Joseph', True]
#del my_list[1] # print(my_list) # [True]
#print(my_list) # prints ['Joseph']


# Change the value of an element.
#my_list[0] = "Kelly" # replaces the number 1 at zero index with a string "Kelly"
#print(my_list) # prints ['Kelly', 'Joseph', True]
#
#my_list[2] = False # replaces the boolean value at index 2 with a new boolean value
#print(my_list) # prints ['Kelly', 'Joseph', False]
#
## Add more elements at the end.
#my_list.append("foo")
#print(my_list)


















# 3.  PROPERTIES OF LISTS: ORDERED
# Create an empty list.
#my_list = []
#
## Add a few items in a particular order.
#my_list.append("Joseph") # Index 0
#print(my_list[0]) # Joseph
#
## Index 1
#my_list.append(500)
#print(my_list[1]) # 500
#
## Index 2
#my_list.append("foo")
#print(my_list[2]) # foo
#



















# 4.  PROPERTIES OF LISTS: HETEROGENEITY
#my_list = [1, 2, 3, 4, 5]
#my_list = ["Joseph", "Kelly", "Eric"]
#my_list = [True, True, False]
#my_list = [None, None, None]
#
## Store different data types at the same time, even other lists and other collection types.
#
#my_list = [
# 1, # Integers
# 2.00, # Floats
# True, # Booleans
# "Joseph", # Strings
# None, # None (Python's NULL)
# [100, 200, 300], # Other lists
# {"Cars", "Motorcycles"}, # Sets, dictionaries, classes - Anything!
#]



















# 5.  CREATING LISTS
# You can create an empty list by using empty square brackets []
#my_list = []
#my_list.append('chris')
#
## You can create a pre-populated list by declaring the elements inside the brackets.
#my_list = [1, 2, 3]
#my_list = ['Joseph', 'Kelly', 'Eric']
#print(my_list)
#
# You can also use variables.
#employee_1 = 'Joseph'
#employee_2 = 'Kelly'
#employee_3 = 'Eric'
#my_list = [employee_1, employee_2, employee_3]

# REMEMBER: You can mix and match data types. Even other lists!
#my_list = [1, 1.00, False, None, ['Joseph', 'Kelly']]
#print(my_list)



















# 6.  RETRIEVING INDIVIDUAL ELEMENTS
# Indexes     0       1        2       3         4
#my_list = ["Joseph", "Kelly", "Eric", "Tom", [100, 200]]

# Access individual elements directly using "positive indexing".
#my_list[0] # Joseph
#my_list[3] # Tom

# Access elements from the end of the list using "negative indexing".
#my_list[-1] # Whatever the last item is, in this case the list [100, 200]
#my_list[-2] # Whatever the second to last item is, in this case "Tom"
#print(my_list[-1])

# Access a list element inside another list
#print(my_list[4][1]) # 100
#my_list[4][1] # 200


















# 7.  PRACTICE! & SOLUTION
# Create a list that holds the following information about your location.
# - The first element should be the city name.
# - The second element should be the state or province.
# - The third element should be a list containing the maximum temperatures
# of the last three days.
#my_list = ["Raleigh", "North Carolina", [101, 98, 88]]

## Now, create print statements to display the following information:
#print(my_list[0]) # - The city name: Raleigh

## Bonus - The first temperature of the list of temperatures: 101

















# 8.  ADD AND REMOVE ELEMENTS
# We will start with an empty list, but you could also start with a pre-populated list.
# can use del[] to remove an element by index.
# .insert(index, value) to add an element at a specific index.
# .pop() to remove an element by index and returns it.
# .remove(value) to remove the first occurrence of a specific value.

# names = ['Joseph', 'Kelly', 'Eric']
#print(names) # ["Joseph", "Tom"]

## To remove items from the list, you use the "del" statement, with the index.
#del names[1] # Removes "Tom"
#print(names) # ["Joseph"]

# Warning: Using "del" directly on the list itself removes the whole list from memory.
#del some_list

# You can also remove by value using "remove()" - removes first occurrence

cities = ['Raleigh', 'Durham', 'Cary', 'Apex']

cities.remove('Raleigh')
print(f"After removing 'Raleigh': {cities}")


# Use .pop() to remove an element by index.
# can add / prepend using .insert(index, value) to add an element at a specific index.
# "pop()" removes an element at a specific index and returns it
popped_city = cities.pop(1)  #
print(f"Popped city: {popped_city}")  # '
print(f"After pop at index 1: {popped_city}")  #
print()

names = ['Joseph', 'Kelly', 'Eric', 'Tom']
print(names)  # ['Joseph', 'Kelly', 'Eric', 'Tom']

popped_names = names.pop(0)

print(names)





















# 9.  PRACTICE!
# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

#my_list = []
#my_list.append('Raleigh')
#my_list.append('North Carolina')
#my_list.append([101, 102, 103])
#my_list.append("Cat")
#
## Then, remove the State, without using the indexes.
#my_list.remove('North Carolina')
#
## Bonus: Remove the last element, using a negative index.
#del my_list[-1]
#

















# 10. CHECK IF AN ELEMENT EXISTS
#location = ["Raleigh", "North Carolina", [101, 98, 90]]
#
#print("Raleigh" in my_list) # Prints True
#print("North Carolina" in my_list) # Prints True
#print(101 in my_list) # Prints False, why? 🤔
#print(101 in my_list[2]) # Prints True
#
#if 'Raleigh' in location:
#    print('Raleigh was found in the list')
#
#if 'Chapel Hill' not in location:
#    print('Chapel Hill was NOT found in the list')
## the in and not in explained:
#"""
#In Python, the in and not in operators are used to check for membership in an iterable,
#such as a list, string, tuple, or set.
#They return a boolean value (True or False) based on whether a specified value is present (or absent) in the iterable.
#Here's a detailed explanation of how they work, particularly in this context.
#
#The `in` Operator
#Purpose: Checks if a value exists within an iterable.
#Returns: True if the value is found, False otherwise.
#Usage: value in iterable
#
#`not in` Operator
#Purpose: Checks if a value does not exist within an iterable.
#Returns: True if the value is not found, False if it is present.
#Usage: value not in iterable
#
#"""
#check_location = ["Raleigh", "North Carolina", [101, 98, 90]]
#
#if 'Raleigh' in check_location:
#    print('Raleigh was found in the list')
#else:
#    print('Raleigh was NOT found in the list')




















# 11. SORT A LIST
# In-place sorting (modifies original list)
#my_list = [10, 4, 8, 3, 1]
#my_list.sort()
#print(my_list)  # [1, 3, 4, 8, 10]
#
## Creating a new sorted list
#my_list = [10, 4, 8, 3, 1]
#sorted_list = sorted(my_list)
#print(sorted_list)  # [1, 3, 4, 8, 10]
#

















# 12. REVERSE A LIST
## In-place reversal
#my_list = [10, 4, 8, 3, 1]
#my_list.reverse()
#print(my_list)  # [1, 3, 8, 4, 10]
#
## Creating a new reversed list
#my_list = [10, 4, 8, 3, 1]
#reversed_list = list(reversed(my_list))
#print(reversed_list)  # [1, 3, 8, 4, 10]


















# 13. PRACTICE! & SOLUTION
# Create a list that contains the ingredients for a sandwich. Yum.🥪
# If you want to use an empty list and add stuff to it, or start
# with a pre-populated list is up to you.
# Some people like cheese, some people don't. ONLY add cheese to your
# list of ingredients if you really like cheese.🧀

#my_list = ["bread", "ham", "tomato", "cheese"]
#
## Then, use an if/else statement to print a message that will tell us
## whether you like cheese, based on its presence in the list.
#
#if "cheese" in my_list:
# print("I love cheese")
#else:
# print("I hate cheese")
#
## Then, to make it look pretty, sort the list in alphabetical order and print it out.
## Our computer is very old and it doesn't have a lot of memory. Also, we don't care
## about the original order of the ingredients.
#
#my_list.sort()
#print(my_list)
#

















## 14. CONCATENATION
#my_list_1 = ["Joseph", "Kelly"]
#my_list_2 = ["Tom", "Bernard"]
#
#my_concatenated_list = my_list_1 + my_list_2
#print(my_concatenated_list) # ['Joseph', 'Kelly', 'Tom', 'Bernard']
#
#my_concatenated_list = my_list_2 + my_list_1
#print(my_concatenated_list) # ['Tom', 'Bernard', 'Joseph', 'Kelly']
#
## Another way to stitch lists together is to multiply them with
## the * operator, which repeats them.
#my_list = [1, 2, 3]
#my_repeated_list = my_list * 3
#
#print(my_repeated_list) # [1, 2, 3, 1, 2, 3, 1, 2, 3]



















# 15. LIST SLICING
# Syntax: new_list = original_list[start:end:optional_step]
#my_list = [0, 1, 2, 3, 4, 5, 6]
#
## Basic slicing: [start:end] (end is exclusive)
#print(my_list[1:4])  # [1, 2, 3]
#
## With step: [start:end:step]
#print(my_list[0:7:2])  # [0, 2, 4, 6]
#
## Defaults
#print(my_list[:])  # Entire list
#print(my_list[2:])  # From index 2 to end
#print(my_list[:3])  # From start to index 3 (exclusive)
#
#
## You can use an optional step parameter to extract every N elements
#my_slice = my_list[::2]
#my_slice = my_list[0:4:2]



































# 16. PRACTICE! & SOLUTION
# For this exercise, you will create two lists. The first list will contain the work week days,
# the second list will contain the days of the weekend.
#work_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
#weekend_days = ['saturday', 'sunday']
#
## Then, you need to concatenate both lists into a third new list that represents the full week.
#full_week = work_days + weekend_days
#
## Then, can you think of an easy way to create a new list that contains the days of two full weeks?
#fortnight = full_week * 2
#
## Finally, once you have two full weeks into a list, use the slicer to:
## 1. Extract week 1 into its own list. Use this list in the next two points.
#week_1 = fortnight[0:7]
#
## 2. Write a slicer that will return the following: ['monday', 'wednesday', 'friday', 'sunday']
#print(week_1[::2])
#


















# 17. AGGREGATORS
# Use min() to determine the smallest number in a list of numbers or
# the earliest alphabetical element in a list of strings. Same type only!
#min([1, 2, 3]) # 1
#min(['c', 'a', 'd']) # a
#
## Use max() exactly the same way, but for the highest value.
#max([1, 2, 3]) # 3
#max(['a', 'b', 'c']) # c
#
## Use sum() to add up the total in a list of numbers. Only things that evaluate to numbers!
#sum([1, 2, 3]) # 6
#sum([1, 2.0, 3.5]) # 6.5
#sum([1, 2.0, 3.5, True, False]) # 7.5


















# 18. HELPERS
## Use len() to find out the size of a list.
#len([1, 2, 3, 4, 5]) # 5
#len([[1, 2, 3], [4, 5, 6]]) # 2 - Why? 🤔
#
## Use my_list.index() to find the index of an element.
#my_list = ["Joseph", "Kelly", "Tom"]
#my_list.index("Kelly") # 1
#my_list.index("Tom") # 2
#
## Use my_list.count() to find out how many times an element is in the list.
#my_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
#my_list.count(2) # 1
#my_list.count(4) # 2
#my_list.count(6) # 3
#
#my_list = [True, True, False]
#my_list.count(True) # 2
#my_list.count(False) # 1
#
















# 19. PRACTICE! & SOLUTION - HELPERS
# A company opened in 2010 and ceased operations in 2014.
# Imagine the following list contains the number of
# employees the company for each year:
# Hint, use aggregators to solve.
# min() max() sum() .count() len()

# Year: 2010 2011 2012 2013 2014
#employees = [ 93, 104, 89, 101, 93]
#
## We would like to know the following
## 1. What's the lowest number of employees the company ever had?
#print(min(employees)) # 89
#
## 2. What's the highest number of employees the company ever had?
#print(max(employees)) # 104
#
## 3. What's the total head count if all employees were different every year?
#print(sum(employees)) # 480
#
## 4. How many years had 93 employees?
#print(employees.count(93)) # 2 (2010 and 2014)
#
## 5. Can you think of a way to determine how many years the company was in business?
## Hint: If it's one list element per year, maybe you can count the number of elements.
#print(len(employees)) # 5
#
















# CONGRATULATIONS!
# EXTRA [SELF-STUDY]: TUPLES
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
#
#
#
#
#
## Tuples are like lists but immutable
#
## Extra: Sets
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
#
#
#
#print("List Comprehension Example:")
## List Comprehension
## Traditional way
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



