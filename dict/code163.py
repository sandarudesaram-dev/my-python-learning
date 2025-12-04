# Exercise 18: Sort Dictionary by Keys (Approach 1) #

'''
Sort a dictionary by its keys and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).

Given: my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
'''
print()

my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
print("my_dict:", my_dict)

res = sorted(my_dict.items())
print("OrderedDict:", dict(res))