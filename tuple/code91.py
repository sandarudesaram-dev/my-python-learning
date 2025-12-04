# Exercise 16: Modify Tuple (My Approach) #

'''
Given is a nested tuple. Write a program to modify the first item (22) of the list inside the following tuple to 222

Given: tuple1 = (11, [22, 33], 44, 55)
'''
print()

tuple1 = (11, [22, 33], 44, 55)
print("Original tuple:", tuple1)

list_of_tuple1 = list(tuple1)
list_of_tuple1[1][0] = 222
tuple1 = tuple(list_of_tuple1)

print("Modified tuple:", tuple1)