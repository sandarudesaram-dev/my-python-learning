# Exercise 17: Invert Dictionary (My Approach)#

'''
Write a code to swap keys and values in a dictionary. Assume all values are unique

Given: original_dict1 = {'a': 1, 'b': 2, 'c': 3}
'''
print()

original_dict1 = {'a': 1, 'b': 2, 'c': 3}
print("original_dict1:", original_dict1)

inverted_dict = {}

for i in original_dict1:
	inverted_dict[original_dict1[i]] = i

print("inverted_dict:", inverted_dict)