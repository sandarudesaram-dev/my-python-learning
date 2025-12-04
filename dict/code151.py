# Exercise 11: Create a dictionary by extracting the keys from a given dictionary (Given Approach 2) #

'''
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
'''
print()

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

print("sample_dict:", sample_dict)

keys = ["name", "salary"]

new_dict = dict()
for k in keys:
	new_dict.update({k:sample_dict[k]})
print("new_dict:", new_dict)