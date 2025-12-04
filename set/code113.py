# Exercise 5: Symmetric Difference #

'''
Find the symmetric difference of set1 and set2. Write a code to return a new set containing elements that are unique to either set1 or set2, but not in both. It’s like finding the union and then removing the intersection.

Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {30, 40, 50, 60, 70}
'''
print()

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("set1:", set1)
print("set2:", set2)

unique_both = set1.symmetric_difference(set2)
print("Elements that are unique to either set1 or set2, but not in both:", unique_both)