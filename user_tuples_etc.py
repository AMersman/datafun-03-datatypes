"""
Ashley Mersman
Tuples and More
1/30/2023

"""


divider = "******************************************************"
print()
print(divider)
print()
print("Task 5.  Tuples and More")
print()
"""
Work through example_tuples_etc.py. 
Use the example code. 
Use your file, user_tuples_etc.py to practice with tuples, sets, and dictionaries in your domain. 
Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.
Sets: create two sets. Get the intersection and the union.
Dictionaries: See the examples. 
Use a dictionary to create key-value pairs of each word and its count from a file. 
See the example file. Using a loop is okay, but the true Python approach is a dictionary comprehension (fully defining how to build a dict from a list in one short line of code. """

travel_costs = (456, 96, 257)
hotel_costs = (97, 97, 106, 75, 75, 75)
food_costs = (25.77, 12.55, 5.76, 53.66, 3.65, 12.76, 55.66, 3.65)

print(f"The costs for transportation were: {travel_costs}")
print(f"The costs for lodging were: {hotel_costs}")
print(f"The costs for food were: {food_costs}")

#slicing and indexing tuples

print(f"The first flight cost: {travel_costs[0]}")
print(f"Food on the first day cost: {food_costs[:4]}")

#concatenate and repeat tuples
total_cost = travel_costs + hotel_costs + food_costs 
print(f"All the costs are listed: {total_cost}")
print(f"The travel costs for two people would be: {travel_costs * 2}")

print()
print(divider)
print()
print("Sets")
print()

setA = {"Mickey", "Minnie", "Donald", "Daisy", "Goofy", "Pete"}
setB = {"Mickey", "Bluey", "Minnie", "Bingo", "Mater", "Lightening McQueen"}

union = setA | setB
intersection = setA & setB

print(f"The union of the sets is {union}.")
print(f"The intersection of the sets is {intersection}.")

print()
print(divider)
print()
print("Dictionaries")
print()

with open("text_simple.txt", "r") as text:
    words = text.read().split()

dict_words = {word: words.count(word) for word in words}


print(f"The words in the text_simple are used this many times: {dict_words}.")
print()
print(divider)
print()
print("End")