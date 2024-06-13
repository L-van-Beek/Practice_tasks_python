# Dice Roll

# Suppose we have two dice. 🎲 🎲

# Create a game where one guesses the total value after rolling a pair of dice once.

# Each die has the integer values 1 to 6. Since there's two dice, the range of possible values is between 2 and 12 (inclusive).

# Use the random module to “roll” the dice and store the random values of each die variable in a new total variable.

# Until the correct value is guessed, use a while loop to keep prompting the user for a number.

# Use while loops along with methods from the random module to solve this challenge.

# Solution: 
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2
guess = int(input("Guess the total value of the roll: "))
while guess != total:
  guess = int(input("Try again: "))
  if guess == total:
    print("You got it!")
