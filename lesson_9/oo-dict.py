#!/usr/bin/env python3

import sys

class PhoneBook:
    def __init__(self):
        # Internal dictionary to store contacts, begin with an empty dictionary.
        self.contacts = {}
        print("[DEBUG] PhoneBook instance created")

    def add_contact(self, name, phone_number):
        """Add or update a contact."""
        print(f"[DEBUG] Adding/updating contact: {name} with number {phone_number}")
        self.contacts[name] = phone_number
        print(f"Added/Updated: {name} -> {phone_number}")
        print(f"[DEBUG] Current contacts: {self.contacts}")

    def remove_contact(self, name):
        """Remove a contact by name."""
        print(f"[DEBUG] Attempting to remove contact: {name}")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Removed contact: {name}")
            print(f"[DEBUG] Contact removed successfully")
        else:
            print(f"Contact '{name}' not found.")
            print(f"[DEBUG] Contact not found in dictionary")
        print(f"[DEBUG] Current contacts: {self.contacts}")

    def find_contact(self, name):
        """Find and return the phone number of a contact."""
        print(f"[DEBUG] Searching for contact: {name}")
        if name in self.contacts:
            print(f"{name}'s number is {self.contacts[name]}")
            print(f"[DEBUG] Contact found")
            return self.contacts[name]
        else:
            print(f"Contact '{name}' not found.")
            print(f"[DEBUG] Contact not found in dictionary")
            return None

    def list_contacts(self):
        """List all contacts."""
        print(f"[DEBUG] Listing contacts. Current count: {len(self.contacts)}")
        if not self.contacts:
            print("Phone book is empty.")
        else:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f" - {name}: {number}")
        print(f"[DEBUG] Contact listing complete")

def main(): # 4
    print(f"[DEBUG] Starting main function")
    pb = PhoneBook() # 5

    # Add contacts
    print(f"[DEBUG] Preparing to add contacts")
    contacts = [
        ("Alice", "555-1234"),
        ("Bob", "555-5678"),
        ("Charlie", "555-8765")
    ]
    for name, phone in contacts:
        print(f"[DEBUG] Processing contact: {name}")
        pb.add_contact(name, phone)

    # List contacts
    print(f"[DEBUG] Listing all contacts after additions")
    pb.list_contacts()

    # Search for contacts
    print(f"[DEBUG] Starting contact search operations")
    for name in ("Bob", "Diana"):
        print(f"[DEBUG] Searching for: {name}")
        pb.find_contact(name)

    # Remove contacts
    print(f"[DEBUG] Starting contact removal operations")
    for name in ("Alice", "Diana"):
        print(f"[DEBUG] Removing: {name}")
        pb.remove_contact(name)

    # Final listing
    print(f"[DEBUG] Final contact listing")
    pb.list_contacts()

    print(f"[DEBUG] Main function completed")


if __name__ == "__main__": # 1.hits the name guarding first, then the print statement below
    print(f"[DEBUG] Script started with Python {sys.version}") # 2.
    main() # 3.
    print(f"[DEBUG] Script execution completed")
