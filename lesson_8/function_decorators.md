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

1. `def main():` - This line defines a function named `main`. In Python, it's a convention to use a `main()` function as the entry point of a script.

2. `say_hello("Alice")` - Inside the `main()` function, we're calling the `say_hello()` function and passing the string "Alice" as an argument.

It's important to note that `say_hello()` is a decorated function in this script. It has the `@decorator_example` decorator applied to it. This means that when `say_hello("Alice")` is called, it actually goes through the `decorator_example` wrapper first.

The execution flow when this `main()` function runs will be:

1. The decorator's wrapper function is called.
2. It prints "Decorator func: Before the function execution".
3. The original `say_hello()` function is called with "Alice" as the argument.
4. The `say_hello()` function prints "Hello, Alice!".
5. The wrapper function then prints "Decorator func: After the function execution".

This `main()` function is typically called at the end of the script using the `if __name__ == '__main__':` idiom, which ensures 
that the code inside it only runs when the script is executed directly, 
not when it's imported as a module.


Using **Name Guarding** examples below
```python
# name guarding

def main():
    pass

if __name__=="__main__":
    main()

```

<br>

_Decorators_

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
_Note the `main()` function  is called using name guarding_


_not working
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
