# Exercise 4: Difference of Sets #

'''
Find the difference (set1 - set2). Write a code to returns a new set containing elements that are present in set1 but not in set2.

Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {30, 40, 50, 60, 70}
'''
print()

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("set1:", set1)
print("set2:", set2)

unique_set1 = set1 - set2
print("Elements that are in set1 but not in set2:", unique_set1)
