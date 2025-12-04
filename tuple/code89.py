# Exercise 15: Map Tuples (My Approach) #

'''
Given a tuple of numbers, create a new tuple where each number is squared.

Given: t = (1, 2, 3, 4)
'''
print()

t = (1, 2, 3, 4)
print("Original tuple:", t)

squared = [x**2 for x in t]
squared = tuple(squared)
print("Squared tuple:", squared)