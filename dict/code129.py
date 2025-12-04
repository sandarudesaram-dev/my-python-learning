# Exercise 1: Perform basic dictionary operations #

'''
Given: my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

Perform following operations on given dictionary

	1. Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
	2. Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
	3. Access Key: Print the value associated with the city key.
'''
print()

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print("my_dict:", my_dict)

my_dict['profession'] = 'Doctor'
print("After adding new key-value pair:", my_dict)

my_dict['age'] = 40
print("After modifying age key:", my_dict)

res = my_dict['city']
print("my_dict['city']:", res)