# Exercise 2: Union of Sets #

'''
Find the union of set1 and set2. Write a Python program to return a new set with unique items from both sets by removing duplicates.

Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {30, 40, 50, 60, 70}
'''
print()

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}

print("set1:", set1)
print("set2:", set2)

print()

union = set1 | set2
print("Union of set1 and set2:", union)

# union() returns a new set containing all unique elements from both set1 and set2 #