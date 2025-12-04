# Exercise 9: Copy Specific Elements From Tuple (Given Approach) #

'''
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Given: tuple1 = (11, 22, 33, 44, 55, 66)
'''
print()

tuple1 = (11, 22, 33, 44, 55, 66)
print("tuple1:", tuple1)

copy = tuple1[3:-1]
print("tuple2:", copy)