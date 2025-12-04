# Exercise 13: Check if a value exists in a dictionary (Given Approach) #

'''
While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.

Write a Python program to check if the value 200 is present in the provided dictionary.

Given: sample_dict = {'a': 100, 'b': 200, 'c': 300}
'''
print()

sample_dict = {'a': 100, 'b': 200, 'c': 300}
print("sample_dict:", sample_dict)

if 200 in sample_dict.values():
	print("200 is present in the dictionary")
else:
	print("200 is not present in the dictionary")