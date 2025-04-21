# lesson 6 code example comments



# Properties of Lists: Zero-Based Indexing
```python
# Properties of Lists: Zero-Based Indexing
#             0        1        2      3
my_list = ['Joseph', 'Kelly', 'Eric', 'Tom']
print(my_list[0])
# etc...


# Indexing is always consistent,
# regardless of how the contents change.


# delete an item using del + the index



```



# Mutability
```python

# Mutability
# Create a list.

# use del to Remove Index 1 of the list.

# Change the value of an element by  using the = to assign a new value.

# Add more elements at the end.

```




# Ordered Lists
```python
# Ordered Lists

# Create an empty list.

# Add a few items in a particular order.

# Index 0

# Index 1

```


# Creating lists
```python
# Creating lists
# You can create an empty list by using empty square brackets []
my_list = []

# You can create a pre-populated list by declaring the elements inside the brackets.


# Alternatively, You can also use variables to create the list contents


# REMEMBER: You can mix and match data types. Even other lists!


```


# Retrieveing individual elements
```python
# Retrieveing individual elements
# Indexes     0       1         2        3         4
my_list = ['Honda', 'Toyota', 'Kia', 'Ferrari', 'Ford']

# Access individual elements directly using "positive indexing".


# Access elements from the end of the list using "negative indexing".


# Access a list element inside another list


```


# Practice


# Practice SOLUTION
```python

# Practice SOLUTION

# Create a list that holds the following information about your location.
# - The first element should be the city name.
# - The second element should be the state or province.
# - The third element should be a list containing the maximum temperatures
# - of the last three days.
my_location = ["Miami", "Florida", [101, 93, 99]]


# Now, create print statements to display the following information:
# - The city name:
# - The state or province:
# - The list of temperatures: []


# Bonus
# - The first temperature of the list of temperatures: 101


```


# Add and Remove Elements
```python
# Add and Remove Elements
# We will start with an empty list, but you could also start with a pre-populated list.


# You can use "append", which adds a single item to the end of the list.


# ["Joseph", "Tom"]


# To remove items from the list, you use the "del" statement, with the index.


# You can also remove by value. This will remove the first value it finds.


# !!  Warning: Using "del" directly on the list itself removes the whole list from memory.
# del my_list

```



# Practice! (solution)
```python

# Practice! (solution)
# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal
my_list = []


# Then, remove the State, without using the indexes.


# Bonus: Remove the last element, using a negative index.


```



# Check if an element exists
```python
# Check if an element exists
# An easy way to check if an element exists in a list, is to use the “in” or “not in” statements


# Prints False, why?


# We can use it as part of an "if" statement.



```



# Sort a list
```python

# Sort a list
# Sorting in place: Use this when the original order is not important. Saves memory.


# Sorting to a new copy: Use this when the original order is important.


```



# Reverse a list
```python
# Reverse a list


# Reversing in place using the "reverse" method, which reverses
# the original list.



# Reversing to a new copy of the list using the "reversed" function,
# which leaves the original list unchanged, but needs to be cast to a list.


```




# Practice! (solution)
```python
# Create a list that contains the ingredients for a sandwich. Yum.🥪
# If you want to use an empty list and add stuff to it, or start
# with a pre-populated list is up to you.
# Some people like cheese, some people don't. ONLY add cheese to your
# list of ingredients if you really like cheese.🧀




# Then, use an if/else statement to print a message that will tell us
# whether you like cheese, based on its presence in the list.




# Then, to make it look pretty, sort the list in alphabetical order and print it out.
# Our computer is very old and it doesn't have a lot of memory. Also, we don't care
# about the original order of the ingredients.



```




# Concatenation
```python
# Concatenation
# Concatenation means stitching stuff together using the + operator
# When you concatenate lists, the order of the elements is preserved


# Another way to stitch lists together is to multiply them with
# the * operator, which repeats them.


```


# List slicing
```python
# List slicing
# Slicing is used to extract a contiguous portion of a list
# The original list remains unchanged
# Syntax: new_list = original_list[start:end:optional_step]
# Indexes: 0  1   2   3   4   5   6


# Using the slicer without any parameters just returns the original list.
print(my_list[:]) # prints the entire list
print(my_list[::])


# Get the first two elements.


# Get the second, third and fourth elements.



```



# List slicing: Optional Step parameter
```python
# List slicing
# You can use an optional step parameter to extract every N elements



# Stepped slicing, get every N items.
# Python will take N steps before grabbing an element.




```



# Practice! (solution)
```python
# Practice! (solution)
# For this exercise, you will create two lists. The first list will contain the work week days,
# the second list will contain the days of the weekend.



# Then, you need to concatenate both lists into a third new list that represents the full week.



# Then, can you think of an easy way to create a new list that contains
# the days of two full weeks?



# Finally, once you have two full weeks into a list, use the slicer to:
# 1. Extract week 1 into its own list. Use this list in the next two points.



# 2. Write a slicer that will return the following: ['monday', 'wednesday', 'friday', 'sunday']

```



# Aggregators
```python
# Aggregators
# Aggregators are special functions that help us perform some basic list calculations
# Use min() to determine the smallest number in a list of numbers or
# the earliest alphabetical element in a list of strings. Same type only!


# Use max() exactly the same way, but for the highest value.



# Use sum() to add up the total in a list of numbers.
# Only things that evaluate to numbers!

```



# Helpers
```python
# Helpers
# Helpers can tell us some useful information about the list or its elements
# Use len() to find out the size of a list.


# Use my_list.index() to find the index of an element.


# Use my_list.count() to find out how many times an element is in the list.


```

# Practice! (solution)
```python
# Practice! (solution)
# A company opened in 2010 and ceased operations in 2014.
# Imagine the following list contains the number of
# employees the company for each year:


# Year: 2010    2011   2012   2013   2014
employees = [ 93, 104, 89, 101, 93]


# 1. What's the lowest number of employees the company ever had?




# 2. What's the highest number of employees the company ever had?




# 3. What's the total head count if all employees were different every year?




# 4. How many years had 93 employees?




# 5. Can you think of a way to determine how many years the company was in business?
# Hint: If it's one list element per year, maybe you can count the number of elements.


```

# BRIEF INTRO & EXPLANATION OF LIST COMPREHENSION
```python

# List Comprehension is a concise way of creating a list.
# Combine 2 to 3 lines of code in a one-liner

# Basic Syntax
# [expression for item in iterable if condition]

# Where:

# expression is what you want to include in the new list
# item is the variable representing each element in the iterable
# iterable is the source collection (list, tuple, string, etc.)
# condition is an optional filter
# Use Cases
# List comprehensions are ideal for:

# Creating new lists by transforming elements from another iterable
# Filtering elements from an iterable
# Replacing complex loops with a single line of code
# Making code more readable and Pythonic
# Improving performance for list creation operations


# Example One: Traditional Loop
my_list = []
for x in range(11):
    my_list.append(x)
print(my_list)

# Example Two: Basic list Comprehension --> Compact 3 lines in one
my_list_comp = [x for x in range(10)]
print(my_list_comp)

# Example Three: List Comprehension with Filtering
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]


# Example Four: Dictionary Comprehension
cubes = {x: x ** 3 for x in range(5)}
print(cubes)  # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# Example Five: Set Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = {num for num in numbers if num % 2 == 0}
print(evens)  # {2, 4, 6, 8, 10}

```


CONGRATS, END OF TODAY'S LESSON


EXTRA SELF-STUDY: TUPLES - EXPLAIN THEM


IDE: LIVE CODING DEMO AND EXPLANATION OF TUPLES
 ```python

    # When declaring a tuple, you have to pre-populated. You can’t add elements later.
    my_tuple = ("Joe", "Kate", 1, 2, 3, [100, 200, 300])

    # This won't work


    # This works just fine


    # ANNOYANCE: If you ever need a tuple with a single element,
    # you have to include a trailing comma.

```


 EXTRA STUDY: SETS - TWO SLIDES


 IDE: LIVE CODE DEMMO OF SETS
```python

# Sets have a variety of methods and functions that allow you to manipulate them. Here’s a few:
# Create a set.
my_set = {"Joe", "Kate"}
print(my_set) # {'Kate', 'Joe'}

# Adding my name again doesn't make it show twice due to uniqueness.
my_set.add("Joe")
print(my_set) # {'Kate', 'Joe'}

# Remove an element using remove(). If you try to remove an element that doesn't exist,
# you get an error.
my_set.remove("Joe") # Removes the element.
my_set.remove("Joe") # Raises a KeyError, as the element doesn't exist anymore.
my_set.discard("Joe") # Same as remove(), but doesn't raise an error if it doesn't exist.

# ANNOYANCE: You have to use set() to create an empty set, as {} is used to declare a  dictionary.
my_empty_set = {} # NOT what you want. This creates a dictionary.
my_empty_set = set() # THIS is what you want. This creates an empty set.

```


 PDF: HOMEWORK


Wrap up
-----------------------------

OK, In this lesson we learned lists,
This includes:

- List Properties:
- Zero-Based Indexing
- Mutability
- Orderd lists
- Heterogeneity

- List Creation
- Retrieving individual elements
- Adding & Removing Elements
- Checking if an element exists

- Sorting
- Reversing
- Concatenation
- List Slicing

- Aggregators
- Helpers
- List Comprehension
- Tuples
