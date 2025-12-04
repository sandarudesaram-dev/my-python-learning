# Exercise 11: Create a dictionary by extracting the keys from a given dictionary (Given Approach 1) #

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

new_dict = {k : sample_dict[k] for k in keys}	# dict comphrehension #
print("new_dict:", new_dict)