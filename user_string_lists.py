"""
Ashley Mersman
String Lists
1/30/2023

"""
#import
import random

divider = "******************************************************"
print()
print(divider)
print()
print("Task 4. String Lists")


cities = ["London", "Cabo San Lucas", "Oceanside, CA", "Phoenix, AZ", "Frankfurt", "Vienna"]
countries = ["England", "Mexico", "USA", "USA", "Germany", "Germany"]
continent = ["Europe", "North America", "North America", "North America", "Europe", "Europe"]
months = ["May", "January", "Februrary", "February", "June", "July"]

print(f"We traveled to {len(cities)} cities thus far.")

print(f"The continents we have been to are : {set(continent)}.")

city_country = zip(cities, countries, continent)
print(f"These are the locations: {list(city_country)}")
print()
print(divider)
print()
print("String Lists 2. Random Choice")
print()
"""Use random.choice() to pick a random value from one of your lists.
Customize the sentence generator to create random sentences about your domain. """
random_sentence = f"We are traveling to {random.choice(cities)}, which is in {random.choice(countries)}. The best time to go there is {random.choice(months)}. Or not."

print(random_sentence)


divider = "******************************************************"
print()
print(divider)
print()
print("String Lists 3. Get Unique Words")
print()
"""Choose one of the text data files in the repo - or add another related your your domain.
Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
Sort the list. 
Use len() to get the length display it to the console.
How good is your list? """

with open("text_woodchuck.txt", "r") as file:
    text = file.read()
    words = text.split()
    unique_words = set(words)

sorted = sorted(unique_words)
length = len(sorted)


print(f"There are {length} unique words in text_woodchuck.txt")
print()
print(divider)
print()
