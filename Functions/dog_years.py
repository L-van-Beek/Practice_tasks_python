# Task: Dog Years 
# People say that every year of a dog's life is roughly equal to seven years of a human's life. 🥲

# Write a dog_years() function that takes two parameters:

# - name (string)
# - age (integer)
# It should calculate and return a string featuring the dog's name as well as its age in human years.

# Code: 
def dog_years(name, age):
  doggy = int(age * 7)
  return f"{name} is {doggy} years old in human years"

print(dog_years("Landon", 3))
print(dog_years("Red Bean", 6))
print(dog_years("Cooper", 2))
