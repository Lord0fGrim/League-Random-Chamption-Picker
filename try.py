import random

# Open the file in read mode
with open("LeagueChampion.txt", "r") as f:
    # Read the contents of the file into a string
    contents = f.read()

# Split the string into a list of items
items = contents.split(",")

# Pick a random item from the list
random_item = random.choice(items)

print(random_item)
