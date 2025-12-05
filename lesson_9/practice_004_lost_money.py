
# PRACTICE: WHO HAS THE $100?

# WHICH FOR LOOP IS MOST SUITABLE FOR THIS PROBLEM?
# Write a Python script that prints out the name of the person who has the 100 dollar bill in their wallet.
# This dictionary shows the bills each person has in their wallet and how many.
# Iterate over the wallets and check if each wallet has the 100 dollar bill.
# When you find the 100, print the name of the person that has it.

wallets = {
    'tom': {5: 2, 10: 1}, # Tom has 2 $5 bills and 1 $10 bill.
    'kelly': {1: 5}, # Kelly has 5 $1 bills.
    'joseph': {100: 1} # Joseph has 1 $100 bill.
}

# Loop A: USE THIS FOR LOOP. Cleaner and more Pythonic.
for name, bills in wallets.items():
    if 100 in bills:
        print(f'{name} has 100 dollars.')
        break # Stop checking once you find the 100 dollar bill.

# Loop B
#for name, wallet in wallets.items():
#    if 100 in wallet.keys():
#        print(f'{name} has 100 dollars.')
#        break # Stop checking once you find the 100 dollar bill.