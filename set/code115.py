# Exercise 7: Set Difference Update #

'''
Given two Python sets, write a program to update the first set with only the items that are unique to it (i.e., not present in the second set).

Given:
	set1 = {10, 20, 30}
	set2 = {20, 40, 50}
'''
print()

set1 = {10, 20, 30}
set2 = {20, 40, 50}

print("set1:", set1)
print("set2:", set2)

set1 -= set2
print("set1 with only items that are unique to it:", set1)