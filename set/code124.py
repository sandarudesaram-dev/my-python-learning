# Exercise 14: Find Common Elements in Two Lists #

'''
list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], find the common elements using sets.

Given:
	list1 = [10, 20, 30, 40]
	list2 = [30, 40, 50, 60]
'''
print()

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print("list1:", list1)
print("list2:", list2)

list1 = set(list1)
list2 = set(list2)

res = list1.intersection(list2)
print("Common elements in 2 lists:", res)