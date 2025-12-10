"""
Create an g class. Its constructor should take the name of the animal
and store it as an instance attribute.
This g class should also have a greeting() instance method that takes a name as an argument and prints

out the message: "Hello <NAME>, I'm <NAME_OF_ANIMAL>"

Create Dog and Cat classes that inherit from g.
Create instances and make them greet you.
"""
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello {self.name}, I'm {self.name}")

# Child class
class Dog(Animal):
     pass

dog = Dog('Buddy')
