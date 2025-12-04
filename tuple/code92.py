# Exercise 16: Modify Tuple (Given Approach) #

'''
Given is a nested tuple. Write a program to modify the first item (22) of the list inside the following tuple to 222

Given: tuple1 = (11, [22, 33], 44, 55)
'''
print()

tuple1 = (11, [22, 33], 44, 55)
print("Original tuple:", tuple1)

tuple1[1][0] = 222
print("Modified tuple:", tuple1)