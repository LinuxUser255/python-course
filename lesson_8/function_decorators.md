#  Advanced Python Feature - Decorators

<br>

### First, recap of using the `main()` function, & name guarding

The code below defines the `main()` function, which is a common practice in Python scripts.
explained in detail:

_Name Guarding_ ensures the entire script-code can only be run directly, not when imported into another script

```python

#!/usr/bin/env python3

"""
The three steps to create a function in Python
# 1. Define the function
# 2. Write the code to execute
# 3. Call the function
"""

# 1. Define the function
def main():
    # 2. Write the code to execute
    print("This is the main function.")

# 3. Call the function
main()

```

<br>

Using **Name Guarding:**

`if __name__=="__main__":`


```python
# name guarding

def main():
    pass

if __name__=="__main__":
    main()

```

<br>

### Use of decorators and name guarding

```python
#!/usr/bin/env python3

"""
How to use decorators in Python
Basic example:
"""

# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

# 1. Define the function with decorator
@my_decorator
def main():
    # 2. Write the code to execute
    print("This is the main function.")

# 3. Call the main function
if __name__ == "__main__":
    main()

```

This `main()` function is typically called at the end of the script using the `if __name__ == '__main__':` idiom, which ensures 
that the code inside it only runs when the script is executed directly, 
not when it's imported as a module.




<br>

_Decorators and *args *kwargs function parameters_

```python
#!/usr/bin/env python3

def decorator_example(func):
    """
    - A decorator function that wraps another function to add behavior before and after its execution.
    - This decorator prints messages before and after the execution of the decorated function.
    Parameters:
    func (callable): The function to be decorated.

    Returns:
    callable: A new function that wraps the original function with additional behavior.
    """
    def wrapper(*args, **kwargs):
        print(f'Decorator func: Before the function execution')
        result = func(*args, **kwargs)
        print(f'Decorator func: After the function execution')
        return result

    return wrapper

# this the equivalent of saying:
# say_hello = decorator_example(say_hello)
@decorator_example
def say_hello(name):
    """
    Prints a greeting message to the given name.
    
    - Parameters:
      name (str): The name of the person to greet.
    - Returns:
      None
    """
    print(f'Hello, {name}!')

# The main function calls the decorated function, not the decorator itself.
def main():
    """
    - The main function that demonstrates the usage of the decorated say_hello function.
    - This function calls say_hello with the argument "Alice".

    Returns:
    None
    """
    say_hello("Alice")

if __name__=='__main__':
    main()
```

<br>


### Example of fixing a bug
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f'Opening file: {self.filename}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f'Closing file: {self.filename}')
        if exc_type:
            print(f'An error occurred: {exc_val}')
            return True


    def run_file_manager(self):
        with FileManager('file.txt', 'w') as file:
            file.write('Hello, World!\n')
            print('File written successfully.')

            # If there's an exception within the 'with' block, it will be handled by __exit__.
            with FileManager('non_existent_file.txt', 'r') as file:
                content = file.read()
                print(f'File content: {content}')

if __name__ == '__main__':
    FileManager.run_file_manager()
```
<br>

To fix the warning "Parameter 'self' unfilled" for the `run_file_manager()` method, we need to change it from an instance method 
to a class method using the `@classmethod` decorator. 
This way, it can be called on the class itself without needing an instance. 
Here's the fixed code block:

```python
    @classmethod
    def run_file_manager(cls):
        with FileManager('file.txt', 'w') as file:
            file.write('Hello, World!\n')
            print('File written successfully.')

            # If there's an exception within the 'with' block, it will be handled by __exit__.
            with FileManager('non_existent_file.txt', 'r') as file:
                content = file.read()
                print(f'File content: {content}')

if __name__ == '__main__':
    FileManager.run_file_manager()
```

### This modification allows you to call `run_file_manager()` on the `FileManager` class directly, resolving the "Parameter 'self' unfilled" warning.

<br>
