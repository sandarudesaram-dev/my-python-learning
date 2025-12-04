# Exercise 11: Set Intersection Check (My Approach) #

'''
Write a code to check if two sets have any elements in common. If yes, display the common elements


Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {60, 70, 80, 90, 10}
'''
print()

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

print("set1:", set1)
print("set2:", set2)

res = set1.isdisjoint(set2)
print("set1 and set2 have elements in common:", not(res))

if res == False:
	print("Common elements:", set1.intersection(set2))