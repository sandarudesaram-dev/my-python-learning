# Exercise 9: Check Subset #

'''
Check if set1 is a subset of set2. Write a code to return True if every element in the set1 is also present in the set2.

Given:
	set1 = {10, 20}
	set2 = {10, 20, 30, 40}
'''
print() 

set1 = {10, 20}
set2 = {10, 20, 30, 40}

print("set1:", set1)
print("set2:", set2)

res = set1.issubset(set2)
print("set1 is a subset of set2:", res)