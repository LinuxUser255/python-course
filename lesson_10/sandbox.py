
class Product:
    def __init__(self, title, price):
        self.title = title # book title (attribute)
        self.price = price # book price (attribute)


class Book(Product):
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


