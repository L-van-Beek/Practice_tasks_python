# Snapple is a famous tea drink brand from Queens, New York. Each bottle cap comes with a silly fun fact.

# Use the random module to create a number from 0 to 5.

# Then use an if/elif/else statement to print out one of these six random Snapple facts:

    # 0 - 'Flamingos turn pink from eating shrimp.'
    # 1 - 'The only food that doesn't spoil is honey.'
    # 2 - 'Shrimp can only swim backwards.'
    # 3 - 'A taste bud's life span is about 10 days.'
    # 4 - 'It is impossible to sneeze while sleeping.'
    # 5 - 'It is illegal to sing off-key in North Carolina.'


# Code: 
import random 
fun_fact = random.randint(0, 5)
print(fun_fact) #Here I also wanted to see what number is being drawn 
if fun_fact == 0:
  print("Flamingos turn pink from eating shrimp")
elif fun_fact == 1:
  print("The only food that doesn't spoil is honey")
elif fun_fact == 2:
  print("Shrimp can only swim backwards.")
elif fun_fact == 3:
  print("A taste bud's life span is about 10 days")
elif fun_fact == 4:
  print("It is impossible to sneeze while sleeping")
elif fun_fact == 5:
  print("It is illefal to sing off-key in North Carolina")
