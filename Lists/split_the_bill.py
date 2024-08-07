# Task: Split the Bill
# Suppose you and three of your friends all went out for a meal together. The bill comes due, and all of you decide to split the bill evenly.

# Here is a Python list of prices for what was ordered:
# - bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

# Using this bill list, calculate the total amount and then divide it four ways.
# Initialize the total with zero and loop through the bill list to add everything up.
# With the total, store what each person has to pay in a my_share variable and then print the result to the terminal.

# Code: 

bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0
for i in bill:
  total += i

my_share = round(total / 4, 2) #2 refers to two decimal digits
print(my_share)
