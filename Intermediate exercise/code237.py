# Exercise 3: Remove items from a list while iterating (DEBUG - Attempt1 (FAIL))#

'''
In this question, you need to remove items from a list during iteration without creating a separate copy of the list.

Remove numbers greater than 50

Given: number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
print()

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(number_list)
print(id(number_list))

for i in range(len(number_list)):
	if number_list[i] > 50:
		number_list.pop(i)
		i -= 1 # Pythons 'for' loop ignores any manual changes to i #
print(number_list)
print(id(number_list))