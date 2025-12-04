# Exercise 8: Remove Items From Set Simultaneously (Given Approach)#

'''
Write a Python program to remove items 10, 20, 30 from the following set at once.

Given: set1 = {10, 20, 30, 40, 50}
'''
print()

set1 = {10, 20, 30, 40, 50}
print("set1:", set1)

set1.difference_update({10, 20, 30})
print("After removing 10, 20, 30 from set1:", set1)