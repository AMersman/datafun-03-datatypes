"""
Ashley Mersman
Data Analytics Fundamentals
Module 3; Project 3
1/29/2023

"""

# import some modules first - how many can you make use of?

import math
import statistics as stats
print("==================")
print("Task 3 - Numeric Lists")
"""Create list1 - a fairly long (20 or more list of numbers)
Create listx representing 10 integer times Hint: use range(10) to generate the list, or type it out.
Create listy representing 10 values/measurements read at those times (make up something that loosely fits your domain.
Create listy so the values are pretty much linear, but not exactly - we'll draw a straight-line through the data to make predictions."""

"""list1 is represents a list of travel distances 
in the past 5 years"""
list1 = [235, 500, 1164, 660, 15362, 223, 2003, 
990, 2323, 531, 736, 127, 674, 9735, 673, 1246, 12452, 1222, 
997, 174, 292, 986, 674, 872, 957]
print(f"list1 = {list1}")
listx = list(range(1,11))
print(f"listx = ={listx}")
listy = [20, 40, 62, 83, 95, 121, 139, 156, 184, 210]
print(f"listy = {listy}")

print()
print("Task 3- 1 : List Statistics")
print()
"""Calculate the mean, median, and mode (hint: import statistics module)
Calculate the standard deviation and variance """

print(f'The mean is list1 is {stats.mean(list1)}, listx is {stats.mean(listx)}, and listy is {stats.mean(listy)}.')
print(f'The median is list1 is {stats.median(list1)}, listx is {stats.median(listx)}, and listy is {stats.median(listy)}.')
print(f'The mode is list1 is {stats.mode(list1)}, listx is {stats.mode(listx)}, and listy is {stats.mode(listy)}.')
print(f'The standard deviation is list1 is {round(stats.stdev(list1),2)}, listx is {round(stats.stdev(listx),2)}, and listy is {round(stats.stdev(listy),2)}.')
print(f'The variance is list1 is {round(stats.variance(list1),2)}, listx is {round(stats.variance(listx),2)}, and listy is {round(stats.variance(listy),2)}.')

print()
print("Task 2 - Correlation")
print()
"""Calculate the correlation between listx and listy
Calculate the slope and intercept of the best fit line. Hint: use statistics.linear_regression()
Set a future time = 15. 
Predict the y value at the future time  y = mx + b where m is the slope and b is the y intercept"""

corr = round(stats.correlation(listx, listy),3)
slope, intercept = stats.linear_regression(listx, listy)
x_future = 15
y_future = round(slope * x_future + intercept, 2)

print(f"Correlation is {corr}.")
print(f"Slope is {slope}.")
print(f"Intercept is {intercept}.")
print(f"The predicted y value for x = 15 is {y_future}.")

print()
print("Built in List Functions in Python")
print()

def list_functions(list):
    list_min = min(list)
    list_max = max(list)
    list_length = len(list)
    list_sum = sum(list)
    list_avg = list_sum / list_length
    list_set = set(list)
    asc_list = sorted(list)
    desc_list = sorted(list, reverse = True)
    print(f"Min = {list_min}, Max = {list_max}, Length = {list_length}, Sum = {list_sum}, Average = {list_avg}, Set = {list_set}, Ascending = {asc_list} Descending = {desc_list}.")
    
list_functions(list1)

print()
print("Built in List Methods in Python")
print()

print(listx)

listx.append(11)
print(listx)
listx2 = [12,13,14,15]
listx.extend(listx2)
print(listx)
listx.insert(0,0)
listx.insert(8,7.5)
print(listx)
listx.remove(7.5)
print(listx)
print(f"2 appears {listx.count(2)} times in the list.")
print(f"List sorted ascending = {sorted(listx)}")
print(f"List sorted descending = {sorted(listx, reverse = True)}")
listy = listx.copy()
print(f"Pop first item: {listx.pop(0)}")
print(f"Pop last item: {listx.pop(-1)}")

print()
print("List Transformations - Using filter() and map()")
print()

"""
Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
Use the built in map() function to map each x to cuberoot of x (hint: use math module)
Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side"""

sm_list = [1,2,3,4,5,6,7,8]
print(f"Small list: {sm_list}")
odd = list(filter(lambda x: x % 2 == 1, sm_list))
print(f"The odd numbers from the list: {odd}")
list_squared = list(map(lambda x: x ** 2, odd))
print(f"The odd numbers squared: {list_squared}")
list_divided = list(map(lambda x: round(x/(x**3),4), list_squared))
print(f"The squared numbers divided by cubed value: {list_divided}")

print()
print("Lists 6. List Transformations - Using List Comprehension")
print()

"""Comprehension means to "grasp together" 
Or to use one list to "completely describe" a new list
Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 
Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 
Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice."""



# define some functions

even = [x for x in sm_list if x%2 ==0]
print(f"Even numbers using list comprehension: {even}")
x3 = [x*3 for x in even]
print(f"List values times 3 for even numbers: {x3}")
x_by_max = [x/max(x3) for x in x3]
print(f"Previous values divided by the max value in the list: {x_by_max}")


print()
print()
print("=====================")
print("End of numeric lists")



