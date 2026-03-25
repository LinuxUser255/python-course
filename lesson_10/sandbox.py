
"""
Classes an Object-Oriented Programming (OOP)

This programming design follows an easy to recognize structure.

1. Class declaration
2  Attribute creation (properties) of the class (describing the object)
3. Methods (functions) that operate on the attributes of the class
4. Create the objects, by setting name of the object = class_name(arguments)
5. Invoke methods on the objects, by object_name.method_name(arguments)
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def greeting(self, name):
        print(f"Hello {name}, I'm {self.name}")

class Dog(Animal):
    def greeting(self, name):
        print(f"Hello {name}, my name is {self.name} and I'm a dog! 🐶")
#
class Cat(Animal):
    def greeting(self, name):
        print(f"Hello {name}, my name is {self.name} the cat and I hate you. 😾")


dog = Dog('Fido')
dog.greeting('Josep')

cat = Cat('Max')
cat.greeting('Jane')