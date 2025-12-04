# Exercise 2: Perform dictionary operations (Given approach) #

'''
Given: my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

Perform following operations on given dictionary

	1. Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
	2. Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
	3. Check if Key Exists in the dictionary
'''
print()

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print("my_dict:", my_dict)
print()

# 1 #

del my_dict['profession']
print("After removing profession key-value pair:", my_dict)
print()

# 2 #

print("Printing all key-value pairs")
for key, value in my_dict.items():
	print(key, ":", value)
# 3 #

def check_key_exists(dictionary, key_to_check):
	return key_to_check in dictionary

key1 = 'age'
print("Does", key1, "exist?", check_key_exists(my_dict, key1))