# Exercise 3: Intersection of Sets #

'''
Find the intersection of set1 and set2. Write a code to return a new set containing only the elements that are common to both set1 and set2

Given:
	set1 = {10, 20, 30, 40, 50}
	set2 = {30, 40, 50, 60, 70}
'''
print()

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("set1:", set1)
print("set2:", set2)

intersection = set1 & set2
print("Intersection of set1 and set2:", intersection)

# intersection() returns a new set containing elements that are common to both set1 and set2 #