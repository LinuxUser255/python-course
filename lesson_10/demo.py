
class Printer:
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity =  capacity


    def print_document(self, pages):
        # prints the attributes of the printer
        print(f"Brand: {self.brand}, Model: {self.model}, Capacity: {self.capacity}")



def main():

    # use brand names for creating instances
    hp = Printer("HP", "OfficeJet", 150)

    # call the print_document method
    hp.print_document(50)

if __name__ == "__main__":
    main()