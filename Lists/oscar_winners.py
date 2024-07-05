# Task: The Oscars 
# Every year at the Oscars, the Academy Award for Best Picture is awarded to a single film. It's usually the last award presented and is considered to be the most prestigious.
# Let's use a Python list to document the recent winners!

# Start with the following list:
# best_pictures = ['2019 - Parasite','2018 - Green Book','2017 - The Shape of Water','2016 - Moonlight','2015 - Spotlight','2014 - Birdman','2013 - 12 Years a Slave','2012 - Argo','2011 - The Artist','2010 - The King\'s Speech']

# Google the Best Picture winners from 2020, 2021, and 2022. Then, add them to the front of the best_pictures list.

# Lastly, print the best_pictures list. Make sure that the updated list starts with the winner for 2022, then 2021, then 2020, and so on.

# Code: 
best_pictures = ["2020 - Parasite", "2019 - Green Book", "2018 - The Shape of Water", "2017 - Moonlight", "2016 - Spotlight", "2015 - Birdman", "2014 - 12 Years a Slave", "2013 - Argo", "2012 - The Artist", "2011 - The King's Speech", "2010 - The Hurt Locker"]
# Best picture 2021 - NOMADLAND
# Best picture 2022 - CODA
# Best picture 2023 - EVERYTHING EVERYWHERE ALL AT ONCE
# Best picture 2024 - OPPENHEIMER 
new_winners = ["2021 - Nomadland", "2022 - Coda", "2023 - Everything Everywhere All At Once", "2024 - Oppenheimer"]
best_pictures = new_winners + best_pictures
print(best_pictures)
