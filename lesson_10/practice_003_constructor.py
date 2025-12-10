#!/usr/bin/env python3
"""
Now that you can use a constructor, modify your Printer class so you can
pass the brand, model and paper capacity. Create an instance for each
of the following models:

   Brand       Model       Capacity
   ------     ------    ----------
   HP          7955e       125 sheets
   Brother     HL-L2310D   250 sheets
   Canon       G4270       100 sheets

Add a print_document() instance method that receives a string and prints
it out. The printout should include the brand and model of the printer.
"""

class Printer:
    def __init__(self, brand, model, paper_capacity):
        self.brand = brand
        self.model = model
        self.paper_capacity = paper_capacity
        print(f"Initializing an instance of Printer..{brand} {model}..")


    def notify_low_ink(self):
        print("Ink is low.")

    def notify_out_of_paper(self):
        print("Printer is out of paper.")



# create instance of Printer
hp = Printer('HP', '7955e', 125)
brother = Printer('Brother', 'HL-L2310D', 250)
cannon = Printer('Canon', 'G4270', 100)

# call the methods by using dot notation on the instance
# instance_name.method_name()
hp.notify_low_ink()
hp.notify_out_of_paper()

brother.notify_low_ink()
brother.notify_out_of_paper()

cannon.notify_low_ink()
cannon.notify_out_of_paper()

