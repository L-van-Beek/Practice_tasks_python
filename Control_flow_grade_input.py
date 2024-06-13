# U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨
# First, ask the user to enter their grade as an integer.

# Create a four-year high school grade system using an if/elif/else statement:

    # grade is 9, print 'Freshman'
    # grade is 10, print 'Sophomore'
    # grade is 11, print 'Junior'
    # grade is 12, print 'Senior'
    # Everything else is 'TBD'


user_grade = int(input ("What grade are you in? Type the number to be assigned to the grade system: \n "))
if user_grade == 9: 
  print("Freshman")
elif user_grade == 10:
  print("Sophomore")
elif user_grade == 11:
  print("Junior")
elif user_grade == 12:
  print("Senior")
else:
  print("TBD")
