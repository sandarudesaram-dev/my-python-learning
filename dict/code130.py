# Exercise 2: Perform dictionary operations (My approach 1) #

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
print(my_dict.items())
print()

# 3 #

print("Does 'age' exist?", 'age' in my_dict)
