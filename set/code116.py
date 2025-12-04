# Exercise 8: Remove Items From Set Simultaneously (My Approach)#

'''
Write a Python program to remove items 10, 20, 30 from the following set at once.

Given: set1 = {10, 20, 30, 40, 50}
'''
print()

set1 = {10, 20, 30, 40, 50}
print("set1:", set1)

for i in range(10,31,10):
	set1.discard(i)

print("After removing 10, 20, 30 from set1:", set1)