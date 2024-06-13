# The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

# Create a weight conversion program that:

    # Asks the user what their Earth weight is (as a float).
    # Asks the user for a planet number (as an int).

# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

# To calculate the user's weight:
# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14

# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.


# Code: 

print("~~~~~~~~~~~~~~~")
print("It is time for a new planet expedition!")
print("~~~~~~~~~~~~~~~")
print("Before you leave, we need to convert your weight to see how much you will be weighting at another planet")

earth_weight= float(input("Type in your weight in kilograms and grams: "))
planet= int(input("What planet are do you want to travel to? Type the number (1-7): "))
if planet== 1:
  destination_weight = earth_weight * float(0.38)
  print(destination_weight)
elif planet == 2:
  destination_weight = earth_weight * float(0.91)
  print(destination_weight)
elif planet == 3:
  destination_weight = earth_weight * float(0.38)
  print(destination_weight)
elif planet == 4:
  destination_weight = earth_weight * float(2.53)
  print(destination_weight)
elif planet == 5:
  destination_weight = earth_weight * float(1.07)
  print(destination_weight)
elif planet == 6:
  destination_weight = earth_weight * float(0.89)
  print(destination_weight)
elif planet == 7:
  destination_weight = earth_weight * float(1.14)
  print(destination_weight)
else:
  print("Invalid planet number")
