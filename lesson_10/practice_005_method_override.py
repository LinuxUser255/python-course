"""
Method overriding using Python's built-in super() function'
Take the Dog and Cat classes you built in the last practice and
override the greeting method to give the following output:

Dog: "Hello <NAME>, my name is <DOG_NAME> and I'm a dog! 🐶"
Cat: "Hello <NAME>, my name is <CAT_NAME> the cat and I hate you. 😾"
"""

class Product:
    def __init__(self, title, price):
        self.title = title # book title (attribute)
        self.price = price # book price (attribute)


class Book(Product):
    """
    1. Method Override: The Book class overrides the parent's __init__ method to accept additional parameters
    2. `super().__init__(title, price)`: Calls the parent class's constructor to initialize inherited attributes (title and price)
    3. Additional Attributes:
        self.author - specific to books only
        self.publication_year - also specific to books
    """

    def __init__(self, title, author, price):
        super().__init__(title, price)
        self.author = author
        self.publication_year = 2022 # book publication year (attribute)

    def print_book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")


def main():
    book1 = Book("Python Programming", "Joe Sabido", 19.99)
    book1.print_book_info()


if __name__ == "__main__":
    main()