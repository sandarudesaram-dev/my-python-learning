# Exercise 1: Perform Basic List Operations #

'''
Given: my_list = [10, 20, 30, 40, 50]
Perform following operations on given list
	1. Access Elements: Print the third element.
	2. List length: Print the number of elements in the list.
	3. Check if empty: Write a code to check if list is empty.
'''
print()

my_list = [10, 20, 30, 40, 50]

print("Initial list:", my_list)
print()

# Q1 #
print("Third element:", my_list[2])

# Q2 #
print("Length of the list:", len(my_list))

# Q3 #
if len(my_list) == 0:
	print("List is empty")
else:
	print("List is not empty")


