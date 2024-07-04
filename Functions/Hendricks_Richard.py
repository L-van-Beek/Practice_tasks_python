# Task:
# James Bond is a classic movie character that fights bad guys and introduces himself in an iconic way: “Bond, James Bond.”
# write a greetings() function that takes in two parameters:

# first_name
# last_name
# Print out the phrase with the last name, followed by a comma, and then the full name.

# Next, call the function using your own name, like:

# - greetings('Richard', 'Hendricks')
# The output should look like:

# Hendricks, Richard Hendricks

# Code: 
def greetings(first_name, last_name):
  print(last_name + ", " + first_name + " " + last_name)

greetings("Richard", "Hendricks")
