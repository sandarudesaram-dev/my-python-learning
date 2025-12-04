# Exercise 13: Check if a value exists in a dictionary (My Approach) #

'''
While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.

Write a Python program to check if the value 200 is present in the provided dictionary.

Given: sample_dict = {'a': 100, 'b': 200, 'c': 300}
'''
print()

sample_dict = {'a': 100, 'b': 200, 'c': 300}
print("sample_dict:", sample_dict)

for v in sample_dict.values():
	if (v == 200):
		print("Value 200 is present in the dictionary")
		break
else:
	print("Value 200 is not present in the dictionary")