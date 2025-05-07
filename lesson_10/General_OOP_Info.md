# About OOP - Concepts & More

## When to use Object Oriented Programming in Python??

-------------------------------------------------------------


### - _If you find that you are passing the same set of related variables to a set of functions_
### - _Then consider grouping both the variables and functions into a class._

<br>

- **Using Object Oriented Programming in Python, is a design decision.**


- **However, in general, the _More Important_ , a set of data is, the more likely it is to have multiple functions specific to that data.**


- **Thus, the more useful it is to employ classes, with attributes and methods.**


<br>


## The different programming paradigms in Python

### Python supports multiple programming paradigms, each with its own approach to structuring and executing code:

<br>

1. **Imperative Programming**
   - Focuses on describing **how** a program operates _step by step_
   - Uses statements that change a program's state
   - **Example:** Using **loops**, **conditionals**, and **assignments**

<br>

2. **Procedural Programming**
   - **Organizes** code into procedures/**Functions**
   - Emphasizes **Separating** code into **Reusable** units
   - Example: Using **Functions** to **Modularize** code

<br>

3. **Object-Oriented Programming (OOP)**
   - **Organizes** code into **Objects** that **contain** _Data and Behavior_
   - Uses **classes** to define _object templates_
   - Key concepts: **inheritance**, **encapsulation**, **polymorphism**
   - Example: Creating **classes** to model real-world **entities**
   - Real life code examples linked below
     
   <br>

4. **Functional Programming**
   - Treats computation as the evaluation of mathematical functions
   - Avoids changing state and mutable data
   - Emphasizes immutability and pure functions
   - Example: Using map(), filter(), reduce(), and lambda functions

   <br>
5. **Declarative Programming**
   - Focuses on *what* the program should accomplish without specifying how
   - Example: List comprehensions, SQL-like queries

   <br>
6. **Event-Driven Programming**
   - Program flow is determined by events (user actions, sensor outputs, etc.)
   - Common in GUI applications and web development
   - Example: Using callbacks and event handlers

   <br>
   
7. **Aspect-Oriented Programming**
   - Separates cross-cutting concerns
   - Less common in Python but possible with decorators
   - Example: Using decorators for logging or authentication

   <br>
### Python's flexibility allows developers to mix these paradigms as needed for different parts of an application.

<br>

# Critical Concepts of OOP

- **Class:** is a _template_ for creating objects. 
- All objects created using the same class, will have the same characteristics.
- **Object:** is and _instance_ of a class. _(Collection of Data & Behaviours)_
- **Instantiate:** Is the _creation_ of an instance of a class `__init__`
- **Method:** is a _function_ that is defined in a class.
- **Attribute:**  is a _variable_ bound to an _instance_ of a class.

### And everyone asks, what is `self` ?? 

#### `self` is a reference to an instance of a class

```python
class Car:
    def __init__(self, make, model): # <- self in param
        self.make = make             # <- self in the attribute
        self.model = model

    def start_engine(self): # <- method
        pass

```
- In this example, `self` refers to `Car`

- `self` is included in the parameter
- it is part of the attributes (description)
- And is referenced in the methods

<br>

# When to Use Name Guarding in OOP

## When to Use Name Guarding (`if __name__ == "__main__":`)

1. **In Reusable Modules**
   - When your file contains classes or functions that might be imported elsewhere
   - When the file serves dual purposes as both a library and a standalone script

2. **In Testing Scenarios**
   - When you include test code or examples in the same file as your class definitions
   - When you want to demonstrate usage without forcing execution upon import

3. **In Framework Development**
   - When building components that might be used in different contexts
   - When creating utilities that can be both imported and run directly

4. **In Educational Code**
   - When writing example code that demonstrates concepts but might also be imported
   - When creating tutorials where code might be reused in different contexts

<br>

## When NOT to Use Name Guarding

1. **In Pure Script Files**
   - When the file is meant to be run directly and never imported
   - When writing simple, one-off scripts with no reusable components

2. **In Entry Point Files**
   - In files specifically designated as application entry points
   - In "main.py" or similar files whose sole purpose is to start the application

3. **In Configuration Files**
   - In files that only contain configuration settings or constants
   - In files with no executable code beyond variable assignments

4. **In Some Framework-Specific Files**
   - In files where the framework handles execution context (e.g., some web frameworks)
   - When the framework documentation explicitly recommends against it

## Best Practice Guidelines

- **Default to Using It**: When in doubt, include name guarding
- **Consider Future Use**: Even if you don't plan to import the file now, future requirements might change
- **Consistency**: Follow the conventions of your project or team
- **Documentation**: If your approach differs from project standards, document why

In OOP specifically, name guarding is particularly valuable because classes are designed for reuse, and separating definition from execution is a core principle of good object-oriented design.

<br>

## Real world example Python OOP 

-----

### [yt-dlp](https://github.com/yt-dlp/yt-dlp/tree/master)

**yt-dlp is a feature-rich command-line audio/video downloader**

<br>
