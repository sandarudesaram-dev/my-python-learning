# update() method for dict #

'''
The update() method in Python dictionaries is used to add key-value pairs to an existing dictionary or to merge another dictionary or iterable of key- value pairs into it. This method modifies the dictionary in-place and does not return a new dictionary.
'''
print()

# Example 1 - Updating with another dictionary #

my_dict = {'a':1, 'b':2}
other_dict = {'b':3, 'c':4}
my_dict.update(other_dict)
print(my_dict)
print()

# Example 2 - Updating with a list of tuples #

another_dict = {'x':10}
new_items = [('y', 20), ('z', 30)]
another_dict.update(new_items)
print(another_dict)
print()

# Example 3 - Updating a single key-value pair #

single_update_dict = {'name':'Alice', 'age':30}
single_update_dict.update({'city':'New York'})
print(single_update_dict)
