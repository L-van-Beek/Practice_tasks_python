# A number is "squared" when it is either multiplied by itself or taken to the second power (e.g., 4² = 4 x 4 = 16).

# First, ask the user for an integer with int(input()) and store it in a number variable. Then, define a total variable with an initial value of 0.

# Note: You can pass a string prompt to int(input()).

# Next, use a for loop and range() function to calculate the total of the squares of all integers from 1 to that number.

# Last, print the output as an integer value.

# For example, if number is 5, the total should be 55 because:
# 12+22+32+42+52
# =1+4+9+16+25
# =55

# Solution: 
number = int(input("type a whole number: "))
total = 0
for num in range(1, number + 1):
  square = int(num ** 2)
  total = total + square
print(total)
