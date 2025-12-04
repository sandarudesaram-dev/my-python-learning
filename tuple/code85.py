# Exercise 13: Removing Duplicates from Tuple (Approach - 2) #

'''
Write a code to create a new tuple with only unique elements.

Given: my_tuple = (1, 2, 2, 3, 4, 4, 5)
'''
print()

my_tuple = (1, 2, 2, 3, 4, 4, 5)
print("my_tuple:", my_tuple)

unique_list = []

for item in my_tuple:
	if (item not in unique_list):
		unique_list.append(item)
unique_tuple = tuple(unique_list)
print("unique_tuple:", unique_tuple)