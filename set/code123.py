# Exercise 13: Set Intersection Update #

'''
Write a code to remove items from set1 that are not present in set2.

Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {30, 40, 50, 60, 70}
'''
print()

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("set1:", set1)
print("set2:", set2)

set1 &= set2
print("Elements in set1 taht are in set2:", set1)