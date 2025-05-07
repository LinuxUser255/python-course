#!/usr/bin/env python3

"""
* Create a Printer class that has two functions:
* notify_low_ink() should print a message saying ink is low.
* notify_out_of_paper() should print a message saying printer is low on paper.
* Create an instance of the printer,
    then call each of the instance methods to test the messages.
"""
# Original Refactored Again

class Printer:
    def __init__(self, ink_level=100, paper=50):
        self.ink_level = ink_level
        self.paper = paper

    def print_document(self, pages):
        """Print a document with the specified number of pages."""
        if pages > self.paper:
            print(f"Not enough paper to print {pages} pages.")
            return

        print(f"Printing {pages} pages...")
        self.paper -= pages
        self.ink_level -= pages * 0.5  # Assuming each page uses 0.5% ink

        self.check_status() # call the next method, check_status

    def check_status(self):
        """Check printer status and notify if needed."""
        self.notify_low_ink() # call the next method, notify_low_ink
        self.notify_out_of_paper() # call the next method, notify_out_of_paper

    def notify_low_ink(self):
        """Notify if ink level is low."""
        if self.ink_level <= 10:
            print("Warning: Ink is low.")
        else:
            print(f"Ink level: {self.ink_level}%")

    def notify_out_of_paper(self):
        """Notify if paper is low or out."""
        if self.paper == 0:
            print("Error: Printer is out of paper.")
        elif self.paper <= 10:
            print(f"Warning: Low on paper. Only {self.paper} sheets remaining.")
        else:
            print(f"Paper remaining: {self.paper} sheets")


if __name__ == "__main__":
    # Create an instance of the printer
    hp = Printer()

    # Test the printer methods
    print("Initial printer status:")
    hp.check_status()

    print("\nPrinting 33 pages:")
    hp.print_document(33)

    print("\nPrinting 20 more pages:")
    hp.print_document(20)
