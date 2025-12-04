# Exercise 3.1: Remove items from a list while iterating #

'''
In this question, you need to remove items from a list during iteration.

Remove numbers greater than 50

Given: number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
print()

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"number_list: {number_list}")
print(f"ID: {id(number_list)}")

number_list = [x for x in number_list if x <= 50]
print(f"number_list: {number_list}")
print(f"ID: {id(number_list)}")