# Exercise 17: Invert Dictionary (Given Approach)#

'''
Write a code to swap keys and values in a dictionary. Assume all values are unique

Given: original_dict1 = {'a': 1, 'b': 2, 'c': 3}
'''
print()

original_dict1 = {'a': 1, 'b': 2, 'c': 3}
print("original_dict1:", original_dict1)

def invert_dictionary(input_dict):
	inverted_dict = {}
	for key, value in input_dict.items():
		inverted_dict[value] = key
	return inverted_dict

res = invert_dictionary(original_dict1)

print("inverted_dict:", res)

