# Exercise 5: Merge two Python dictionaries into one (Given Approach 2) #

'''
Write a code to merge two dictionaries into a new dictionary and print it.

Given:
	dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
	dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
print()

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print("dict1:", dict1)
print("dict2:", dict2)

dict3 = {**dict1, **dict2}
print("dict3:", dict3)
