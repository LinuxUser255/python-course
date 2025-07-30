
# Lists in Python


# Python Lists

## Overview

Lists are one of Python's most versatile and commonly used data structures. They allow you to store multiple items in a single variable, and are mutable (can be changed after creation).

## List Properties

### Zero-Based Indexing
- Elements in a list are accessed by their position (index)
- The first element is at index 0
- Example:

```python
 # Indexes     0         1      2       3
my_list = ['Joseph', 'Kelly', 'Eric', 'Tom']
# my_list[0]: 'Joseph'
# my_list[1]: 'Kelly'
# my_list[2]: 'Eric'
# my_list[3]: 'Tom'

# Indexing is always consistent,
# regardless of how the contents change.

del my_list[1]

# One could expect the list to end up like this:

# my_list[0]: 'Joseph'
# my_list[2]: 'Eric'
# my_list[3]: 'Tom' 
```

<br>


### Mutability
- Lists can be modified after creation
- You can add, remove, or change elements
- Example:
 
```python
# Create a list.
my_list = [1, "Joseph", True]

# Remove Index 1 of the list.
del my_list[1]

# Change the value of an element.
my_list[1] = "Eric" # Changes index 1 from “Joseph” to “Eric”.

# Add more elements at the end.
my_list.append("Kelly")
```
<br>

### Ordered
- Elements maintain their insertion order
- Example:
 
```python
# Create an empty list.
my_list = []

# Add a few items in a particular order.
my_list.append("Joseph") # Index 0
my_list.append("Kelly") # Index 1
my_list.append("Eric") # Index 2

print(my_list[0]) # Joseph
print(my_list[1]) # Kelly
print(my_list[2]) # Eric

```
<br>

### Heterogeneous
- Lists can contain elements of different data types
- Example:

```python
my_list = [1, 2, 3, 4, 5]
my_list = ["Joseph", "Kelly", "Eric"]
my_list = [True, True, False]
my_list = [None, None, None]

# Store different data types at the same time, even other lists and other collection types.

my_list = [
 1, # Integers
 2.00, # Floats
 True, # Booleans
 "Joseph", # Strings
 None, # None (Python's NULL)
 [100, 200, 300], # Other lists
 {"Cars", "Motorcycles"}, # Sets, dictionaries, classes - Anything!
]
```

<br>

## Creating Lists

### Empty List

```python
# You can create an empty list by using empty square brackets []
my_list = []

# You can create a pre-populated list by declaring the elements inside the brackets.
my_list = [1, 2, 3]
my_list = ['Joseph', 'Kelly', 'Eric']

# You can also use variables.
employee_1 = 'Joseph'
employee_2 = 'Kelly'
employee_3 = 'Eric'
my_list = [employee_1, employee_2, employee_3]

# REMEMBER: You can mix and match data types. Even other lists!
my_list = [1, 1.00, False, None, ['Joseph', 'Kelly']]

```

<br>

### Retrieving individual elements
```python
# Indexes 0 1 2 3 4
my_list = ["Joseph", "Kelly", "Eric", "Tom", [100, 200]]

# Access individual elements directly using "positive indexing".
my_list[0] # Joseph
my_list[3] # Tom

# Access elements from the end of the list using "negative indexing".
my_list[-1] # Whatever the last item is, in this case the list [100, 200]
my_list[-2] # Whatever the second to last item is, in this case "Tom"

# Access a list element inside another list
my_list[4][0] # 100
my_list[4][1] # 200
```

<br>

### Pactice Solution
```python
# Create a list that holds the following information about your location.
# - The first element should be the city name.
# - The second element should be the state or province.
# - The third element should be a list containing the maximum temperatures
# of the last three days.
my_list = ["Houston", "Texas", [101, 104, 103]]

# Now, create print statements to display the following information:
print(my_list[0]) # - The city name: Houston
print(my_list[1]) # - The state or province: Texas
print(my_list[2]) # - The list of temperatures: [101, 104, 103]

# Bonus
print(my_list[2][0]) # - The first temperature of the list of temperatures: 101
```

<br>

### Add and Remove Elements

```python
# We will start with an empty list, but you could also start with a pre-populated list.
my_list = []

# You can use "append", which adds a single item to the end of the list.
my_list.append("Joseph") # ["Joseph"]
my_list.append("Tom") # ["Joseph", "Tom"]
my_list.append("Kelly") # ["Joseph", "Tom", "Kelly"]

# To remove items from the list, you use the "del" statement, with the index.
del my_list[1] # Removes "Tom"
del my_list[-1] # Removes "Kelly" (last)

# You can also remove by value. This will remove the first value it finds.
my_list.remove("Tom")

# Warning: Using "del" directly on the list itself removes the whole list from memory.
del my_list

```

<br>

### Practice Solution
```python
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
```

<br>

## Checking if an Element Exists

```python
my_list = ["Honda", "Toyota", "Kia"]
if "Toyota" in my_list:
    print("Toyota is in the list")
```


<br>

### Sorting
```python
# In-place sorting (modifies original list)
my_list = [10, 4, 8, 3, 1]
my_list.sort()
print(my_list)  # [1, 3, 4, 8, 10]

# Creating a new sorted list
my_list = [10, 4, 8, 3, 1]
sorted_list = sorted(my_list)
print(sorted_list)  # [1, 3, 4, 8, 10]
```

<br>

### Reversing a list
```python
# In-place reversal
my_list = [10, 4, 8, 3, 1]
my_list.reverse()
print(my_list)  # [1, 3, 8, 4, 10]

# Creating a new reversed list
my_list = [10, 4, 8, 3, 1]
reversed_list = list(reversed(my_list))
print(reversed_list)  # [1, 3, 8, 4, 10]
```

<br>


## Practice! (solution)
```python
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

my_list.sort()
print(my_list)
```

<br>


## Concatenation
● Concatenation means stitching stuff together using the + operator

● When you concatenate lists, the order of the elements is preserved
```python
my_list_1 = ["Joseph", "Kelly"]
my_list_2 = ["Tom", "Bernard"]

my_concatenated_list = my_list_1 + my_list_2
print(my_concatenated_list) # ['Joseph', 'Kelly', 'Tom', 'Bernard']

my_concatenated_list = my_list_2 + my_list_1
print(my_concatenated_list) # ['Tom', 'Bernard', 'Joseph', 'Kelly']

# Another way to stitch lists together is to multiply them with
# the * operator, which repeats them.
my_list = [1, 2, 3]
my_repeated_list = my_list * 3

print(my_repeated_list) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

```


<br>

### List Slicing
```python
my_list = [0, 1, 2, 3, 4, 5, 6]

# Basic slicing: [start:end] (end is exclusive)
print(my_list[1:4])  # [1, 2, 3]

# With step: [start:end:step]
print(my_list[0:7:2])  # [0, 2, 4, 6]

# Defaults
print(my_list[:])  # Entire list
print(my_list[2:])  # From index 2 to end
print(my_list[:3])  # From start to index 3 (exclusive)
```

<br>


## Concatenation Practice! (solution)
```python
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

```
<br>

### Aggregators
```python
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
```
<br>

### Helpers
```python
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

```
<br>

### Practice Solution - Helpers
```python
# A company opened in 2010 and ceased operations in 2014.
# Imagine the following list contains the number of
# employees the company for each year:

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

```
<br>

# Extra: Tuples
```python
# When declaring a tuple, you have to pre-populated. You can’t add elements later.
my_tuple = ("Joseph", "Kelly", 1, 2, 3, [100, 200, 300])

# This won't work
my_tuple.append("Eric")
my_tuple.remove("Joseph")

# This works just fine
my_tuple.index("Kelly") # 1
my_tuple.count("Joseph") # 1

# ANNOYANCE: If you ever need a tuple with a single element,
# you have to include a trailing comma.
my_tuple = ("Joseph", )
```

<br>

## Extra: Sets
```python
# Sets have a variety of methods and functions that allow you to manipulate them. Here’s a few:
# Create a set.
my_set = {"Joseph", "Kelly"}
print(my_set) # {'Kelly', 'Joseph'}

# Adding my name again doesn't make it show twice due to uniqueness.
my_set.add("Joseph")
print(my_set) # {'Kelly', 'Joseph'}

# Remove an element using remove(). If you try to remove an element that doesn't exist,
# you get an error.
my_set.remove("Joseph") # Removes the element.
my_set.remove("Joseph") # Raises a KeyError, as the element doesn't exist anymore.
my_set.discard("Joseph") # Same as remove(), but doesn't raise an error if it doesn't exist.

# ANNOYANCE: You have to use set() to create an empty set, as {} is used to declare a dictionary.
my_empty_set = {} # NOT what you want. This creates a dictionary.
my_empty_set = set() # THIS is what you want. This creates an empty set

```



<br>



### Pre-populated List
```python
my_list = ["Honda", "Toyota", "Kia"]
```


<br>

### Using Variables
```python
item1 = "Honda"
item2 = "Toyota"
my_list = [item1, item2]
```
<br>

## Accessing Elements

### Positive Indexing
```python
my_list = ['Honda', 'Toyota', 'Kia', 'Ferrari', 'Ford']
print(my_list[0])  # Honda
print(my_list[2])  # Kia
```
<br>

### Negative Indexing
```python
print(my_list[-1])  # Ford (last element)
print(my_list[-2])  # Ferrari (second-to-last element)
```
<br>

### Nested Lists
```python
nested_list = ['Honda', 'Toyota', 'Kia', ['nested', 'list', 1, 2]]
print(nested_list[3][0])  # 'nested'
print(nested_list[3][2])  # 1
```

## Modifying Lists

### Adding Elements
```python
my_list = []
my_list.append("Honda")  # Adds to the end
```
<br>

### Removing Elements
```python
# By index
my_list = ["Honda", "Toyota", "Kia"]
del my_list[1]  # Removes "Toyota"

# By value
my_list.remove("Kia")  # Removes the first occurrence of "Kia"
```

<br>




## Useful List Functions


## List Comprehension

List comprehension provides a concise way to create lists based on existing lists.

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Using list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```
<br>

## Practice Exercises

1. Create a list of your favorite foods
2. Add a new food to the list
3. Remove one food from the list
4. Check if a specific food is in your list
5. Sort your list alphabetically
6. Create a new list that contains only foods that start with a specific letter
7. Use list comprehension to create a list of the lengths of each food name

<br>

## Summary

- Lists are ordered, mutable collections that can contain elements of different types
- Elements are accessed by index (zero-based)
- Lists can be modified (add, remove, change elements)
- Many built-in functions and methods make working with lists efficient
- List comprehension provides a concise way to create and transform lists
