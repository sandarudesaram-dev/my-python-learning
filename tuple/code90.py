# Exercise 15: Map Tuples (Given Approach) #

'''
Given a tuple of numbers, create a new tuple where each number is squared.

Given: t = (1, 2, 3, 4)
'''
print()

t = (1, 2, 3, 4)
print("Original tuple:", t)

squared = tuple(map(lambda x: x ** 2, t))
print("Squared tuple:", squared) 