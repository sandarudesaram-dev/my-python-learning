# Exercise 6: Add a list of Elements to a Set #

'''
Given a Python list, write a program to add all of its elements into a given set.

Given:
	sample_set = {"Yellow", "Orange", "Black"}
	sample_list = ["Blue", "Green", "Red"]
'''
print()

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

print("sample_set:", sample_set)
print("sample_list:", sample_list)

sample_set.update(sample_list)
print("After adding list to set:", sample_set)