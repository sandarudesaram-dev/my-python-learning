# Exercise 12: Set Symmetric Difference Update #

'''
Write a program to update set1 by adding items from set2 that are not common to both sets.

Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {30, 40, 50, 60, 70}
'''
print()

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("set1:", set1)
print("set2:", set2)

set1 ^= set2
print("Updated set1 after adding items from set2 that are not common to both:", set1)