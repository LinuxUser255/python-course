#  Lists code examples explained
  
  
```python  
my_heterogeneous_list = [1, 2, 3, 4, 5]  
my_heterogeneous_list =  ["Joseph", "Kelly", "Eric"]  
my_heterogeneous_list = [True, True, False]  
my_heterogeneous_list = [None, None, None]  
```  
  
This code shows that a single variable (`my_heterogeneous_list`) can be reassigned to hold lists containing different types of data:  
  
1. First, `my_heterogeneous_list` is assigned a list of integers: `[1, 2, 3, 4, 5]`  
2. Then, it's reassigned to a list of strings: `["Joseph", "Kelly", "Eric"]`  
3. Next, it's reassigned to a list of boolean values: `[True, True, False]`  
4. Finally, it's reassigned to a list of `None` values: `[None, None, None]`  
  
This demonstrates the "heterogeneity" property of Python lists, which means that lists can store elements of any data type. However, it's important to note that in this specific example, the variable is being reassigned to completely new lists each time, rather than showing a single list containing different types of elements.  
  
A true demonstration of heterogeneity would be something like:  
```python  
truly_heterogeneous_list = [1, "Kelly", True, None, [1, 2, 3]]  
```  
  
Where a single list contains elements of different types (integer, string, boolean, None, and another list) all at once.  
  
In the context of the lesson, this code is illustrating that Python lists are flexible in the types of data they can store, which is an important concept in Python's dynamic typing system.  
  
# Accessing Elements  
  
The selected code demonstrates how to access elements in a nested list using negative indexing in Python.  
  
Let's break down what's happening:  
  
```python  
print(my_list[-1])  
print(my_list[-1][0])  
print(my_list[-1][1])  
```  
  
1. `my_list = ['joe', 'bob',[33, 100]]` - This creates a list with three elements:  
   - First element (index 0): the string 'joe'  
   - Second element (index 1): the string 'bob'  
   - Third element (index 2): another list [33, 100]  
  
2. `print(my_list[-1])` - In Python, negative indices count from the end of the list. So `-1` refers to the last element of the list, which is `[33, 100]`. This line will print the entire inner list.  
  
3. `print(my_list[-1][0])` - This accesses the first element (index 0) of the inner list. So it's getting the first element of `[33, 100]`, which is `33`.  
  
4. `print(my_list[-1][1])` - This accesses the second element (index 1) of the inner list. So it's getting the second element of `[33, 100]`, which is `100`.  
  
When you run this code, the output will be:  
```  
[33, 100]  
33  
100  
```  
  
# List Practice: City, State, temps  
```python  
# 1st element: name of city  
# 2nd element: state or province  
# 3rd element: list of temperatures  
my_list = ['LA', 'CA', [75, 69, 72]]  
print(my_list[0])  # Output: LA  
print(my_list[1])  # Output: CA  
print(my_list[2])  # Output: [75, 69, 72]  
  
# Accessing elements in a nested list  
# my_list[2][0] accesses the first element of this nested list, which is the number 75  
print(my_list[2][0])  
```  
  
### print(my_list[2][0]) explained  
The selected code `print(my_list[2][0])` is accessing and printing a nested element within a list.  
  
Let's break it down:  
  
1. `my_list` is a list with three elements:  
   - `my_list[0]` is the string 'LA' (a city name)  
   - `my_list[1]` is the string 'CA' (a state abbreviation)  
   - `my_list[2]` is another list `[75, 69, 72]` (a list of temperatures)  
  
2. `my_list[2]` accesses the third element of `my_list`, which is the nested list `[75, 69, 72]`  
  
3. `my_list[2][0]` then accesses the first element of this nested list, which is the number `75`  
  
So the code `print(my_list[2][0])` will output: `75`  
  
This is an example of nested indexing, where you first access an element in the outer list, and then access an element within that inner list. It's a common pattern when working with more complex data structures in Python.  
  
  
This demonstrates how to access elements in a nested data structure using negative indexing, which is a powerful feature in Python for accessing elements from the end of sequences.  
  
### Checking if element exists  
```python  
# Checking if an element exists in a list  
# use the in or not in statements  
my_list = ["Houston", "Texas", [101, 102, 103]]  
print("Houston" in my_list)  
print("Texas" in my_list)  
print(101 in my_list)   # False,  Why??????  
print(101 in my_list[2])  
  
```  
`print(101 in my_list)   # False,  Why??????`  
# Explanation of the Selected Code  
  
The selected code is checking for the existence of an element in a list, but there's an important distinction between the two lines:  
  
```python  
print(101 in my_list)   # False,  Why??????  
print(101 in my_list[2]) # True  
```  
  
## Why `101 in my_list` returns `False`  
  
The first line checks if `101` exists as a direct element in `my_list`. Looking at the list definition:  
  
```python  
my_list = ["Houston", "Texas", [101, 102, 103]]  
```  
  
`my_list` contains three elements:  
1. The string `"Houston"`  
2. The string `"Texas"`  
3. A nested list `[101, 102, 103]`  
  
When you check `101 in my_list`, Python looks for `101` as a top-level element in the list. Since `101` is not directly in `my_list` (it's inside a nested list), the result is `False`.  
  
## Why `101 in my_list[2]` returns `True`  
  
The second line accesses the third element of `my_list` (which is the nested list `[101, 102, 103]`) using the index `[2]`, and then checks if `101` exists in that nested list.  
  
Since `101` is indeed an element of the nested list `[101, 102, 103]`, the expression `101 in my_list[2]` returns `True`.  
  
```python  
my_list = ["Houston", "Texas", [101, 102, 103]]  
print("Houston" in my_list)  
print("Texas" in my_list)  
  
print(101 in my_list)   # False,  Why??????  
# When you check 101 in my_list, Python looks for 101 as a top-level element in the list.(outer list)  
# Since 101 is not directly in my_list (it's inside the nested list), # therefore, the result is False.  
  
# This one however; 'Reaches' into the sublist, & therefore returns True  
print(101 in my_list[2]) # True  
  
# This demonstrates an important concept in Python: # the in operator only checks for membership at the current # level of a data structure, NOT within nested structures.  
```  
  
## Sort a list  
```python  
# Sorting in place: Use this when the original order is not important. This Saves memory.  
my_list = [5, 4, 3, 2, 1]  
my_list.sort()  
  
# Sorting to a new copy: Use this when the original order is important.  
# The sorted() function is useful when you need both the original list  
# and a sorted version of it.  
my_list = [5, 4, 3, 2, 1]  
my_sorted_list = sorted(my_list)  
  
print(my_list)  
print(my_sorted_list)  
  
```  
  
# Reversed list explanations  
  
## Reversing a List Using the `reversed()` Function - Explained Simply  
  
The comment you're asking about explains how to create a reversed copy of a list without changing the original list.  
  
## In Simple Terms:  
  
Imagine you have a row of numbered cards on a table: 5, 4, 7, 2, 1.  
  
There are two ways to reverse these cards:  
  
1. **The first way** (using `.reverse()` method): You physically rearrange the cards on the table to be in reverse order: 1, 2, 7, 4, 5. Now your original arrangement is gone.  
  
2. **The second way** (using `reversed()` function): You take a photo of the cards, then create a new row of cards in the reverse order. Now you have both the original row (5, 4, 7, 2, 1) AND a new reversed row (1, 2, 7, 4, 5).  
  
  
## Code Example:  
  
```python  
my_list = [5, 4, 7, 2, 1]  
  
# This creates a reversed view but doesn't create a new list yet  
reversed_view = reversed(my_list)  
  
# Convert the view to an actual list  
reversed_list = list(reversed_view)  
  
print(my_list)        # Original: [5, 4, 7, 2, 1]  
print(reversed_list)  # New reversed copy: [1, 2, 7, 4, 5]  
```  
  
Or more simply:  
  
```python  
my_list = [5, 4, 7, 2, 1]  
reversed_list = list(reversed(my_list))  
```  
  
This approach is useful when you want to keep your original list intact while working with a reversed version of it.  
  
  
### More Slicing  
  
The selected code is demonstrating list slicing in Python:  
  
```python  
  
# Goal: Get the second, thrid and fourth elements  
# Indexes:    0         1        2       3      4           5    6  
students = ["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]  
  
print(students[1:4:1]) # Kelly, Eric, Tom  
```  
  
This line is printing a slice of the `students` list using the syntax `[start:stop:step]` where:  
  
1. `start = 1`: The slice begins at index 1 (the second element, since Python uses zero-based indexing)  
2. `stop = 4`: The slice ends at index 4 (exclusive, meaning it includes elements up to but not including index 4)  
3. `step = 1`: The slice takes elements with a step size of 1 (every element in the range)  
  
_Jumps up to, but not including, 4, (Bernard)_  
  
Breaking it down:  
- The `students` list contains: `["Joseph", "Kelly", "Eric", "Tom", "Bernard", "Jack", "Josh"]`  
- Index 1 is "Kelly"  
- Index 2 is "Eric"  
- Index 3 is "Tom"  
- Index 4 is "Bernard" (not included in the slice)  
  
So `students[1:4:1]` returns the sublist `["Kelly", "Eric", "Tom"]`, which is then printed to the console.  
  
The comment at the end of the line correctly indicates the expected output.  
  
## Helpers   
```python  
# Use len() to find out the size of a list.  
number_length = len([1, 2, 3, 4, 5]) # 5  
print(number_length)  
  
letter_length = len([[1, 2, 3], [4, 5, 6]])  # 2 - Why?  
# because the outer list contains exactly two elements  
  
print(letter_length)  
```  
The selected code is demonstrating the behavior of the `len()` function when applied to a nested list.  
  
```python  
len([[1, 2, 3], [4, 5, 6]])  # 2 - Why?  
```  
  
This returns `2` because:  
  
1. The outer list `[[1, 2, 3], [4, 5, 6]]` contains exactly 2 elements:  
   - The first element is `[1, 2, 3]` (a list)  
   - The second element is `[4, 5, 6]` (another list)  
  
2. The `len()` function counts the number of top-level elements in the list, not the total number of items across all nested structures.  
  
3. Even though each inner list contains 3 elements (for a total of 6 numbers), the `len()` function only counts the number of items directly contained in the list you're measuring.  
  
If you wanted to count all the elements in the nested lists, you would need to sum the lengths of each inner list:  
```python  
nested_list = [[1, 2, 3], [4, 5, 6]]  
total_elements = sum(len(inner_list) for inner_list in nested_list)  # 6  
```  
  
This is an important concept to understand when working with nested data structures in Python.  
  
  
<br>  
  
# List Comprehension  
  
List comprehension is a concise way to create lists in Python. It provides a more compact syntax for creating lists based on existing lists or other iterable objects. List comprehension is often more readable and faster than traditional loops for creating lists.  
  
## Basic Syntax  
  
```python  
[expression for item in iterable if condition]  
```  
  
Where:  
- `expression` is what you want to include in the new list  
- `item` is the variable representing each element in the iterable  
- `iterable` is the source collection (list, tuple, string, etc.)  
- `condition` is an optional filter  
  
## Use Cases  
  
List comprehensions are ideal for:  
1. Creating new lists by transforming elements from another iterable  
2. Filtering elements from an iterable  
3. Replacing complex loops with a single line of code  
4. Making code more readable and Pythonic  
5. Improving performance for list creation operations  
  
## Examples based on course content  
```python  
  
# using a traditional for loop  
my_list = []  
for x in range(11):  
    my_list.append(x)  
print(my_list)  
  
my_list_comp = [x for x in range(10)]  
print(my_list_comp)  
  
  
# List comprehension is a concise way to create lists.  
# writing a for loop inside a list  
list_comp_one = [x for x in range(10)]  
print(list_comp_one)  
  
# even numbers  
list_comp_two = [x for x in range(10) if x % 2 == 0]  
print(list_comp_two)  
  
# Gives a list of even numbers five times  
list_comp_three = [[x for x in range(10) if x % 2 == 0] for _ in range(5) ]  
print(list_comp_three)  
  
my_list = ['Joseph', 'Kelly', 'Eric', 'Tom']  
# my_list[0]: 'Joseph'  
# my_list[1]: 'Kelly'  
# my_list[2]: 'Eric'  
# my_list[3]: 'Tom'  
  
# element to add for every iteration of the loop  
list_comp_four = [my_list[i] for i in range(len(my_list))]  
print(list_comp_four)  
```  
  
  
  
## Other Examples  
  
  
### Example One: Traditional Loop  
```python  
use_loop = []  for x in range(11):  
    use_loop.append(x)  
print("Values generated via for-loop:", use_loop)  
```  
This is the traditional way of creating a list using a for loop. It creates a list of numbers from 0 to 10.  
  
### Example Two: Basic List Comprehension  
```python  
use_comp = [x for x in range(11)] print("List creating list comprehension:", use_comp)  
```  
This is the list comprehension equivalent of Example One. It creates the same list (0-10) but in a single line. The expression is simply `x`, meaning we're including each value as-is.  
  
### Example Three: List Comprehension with Filtering  
```python  
squares = [x**2 for x in range(10) if x % 2 == 0]  
print(squares)  # [0, 4, 16, 36, 64]  
```  
This creates a list of squares of even numbers from 0 to 9. The `if x % 2 == 0` part filters to include only even numbers, and `x**2` transforms each value to its square.  
  
### Example Four: Dictionary Comprehension  
```python  
cubes = {x: x ** 3 for x in range(5)}  
print(cubes)  # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}  
```  
This is a dictionary comprehension (a variation of list comprehension). It creates a dictionary where keys are numbers 0-4 and values are their cubes.  
  
### Example Five: Set Comprehension  
```python  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
evens = {num for num in numbers if num % 2 == 0}  
print(evens)  # {2, 4, 6, 8, 10}  
```  
This is a set comprehension (another variation). It creates a set of even numbers from the `numbers` list. Note the use of curly braces `{}` without key-value pairs, which creates a set.  
  
## Summary  
  
List comprehensions and their variations (dictionary and set comprehensions) provide a powerful, concise way to create collections in Python. They combine the steps of iteration, optional filtering, and transformation into a single line of code, making your code more readable and often more efficient.
