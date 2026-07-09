#!/usr/bin/env python3
"""
Method Overriding Demonstration

Shows how a child class can override a parent class's __init__ method
and still reuse the parent's logic with super().

The Book class overrides Product's __init__ to accept extra parameters,
calls super().__init__() to set up the inherited attributes, then adds
its own attributes on top.
"""


class Product:

    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Product):

    def __init__(self, title, author, price):
        super().__init__(title, price)
        self.author = author
        self.publication_year = 2022

    def print_book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")


def main():
    book1 = Book("Python Programming", "Joe Sabido", 19.99)
    book1.print_book_info()


if __name__ == "__main__":
    main()