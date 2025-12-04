# Exercise 13: Removing Duplicates from Tuple (Approach - 1) #

'''
Write a code to create a new tuple with only unique elements.

Given: my_tuple = (1, 2, 2, 3, 4, 4, 5)
'''
print()

my_tuple = (1, 2, 2, 3, 4, 4, 5)
print("my_tuple:", my_tuple)

set_of_tuple = set(my_tuple)
unique_tuple = tuple(set_of_tuple)
print("unique_tuple:", unique_tuple)