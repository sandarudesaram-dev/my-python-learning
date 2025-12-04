# fromkeys() method in Python #

'''
fromkeys() method - Is a class method of the dict type that creates a new dictionary. It is used to construct a dictionary where all keys are taken from a provided iterable, all values are set to a specified value.

syntax:
	dict.fromkeys(iterable[, value])

parameters:

~ iterable (required): Any iterable object (e.g., a list, tuple, set or string) whose elements will become the keys of the new dictionary.

~ value (optional): The value wil be assigned to all keys in the new dictionary. If this argument is ommited, the default value for all keys will be 'None'.

Return value: The fromkeys() method returns a new dictionary.
'''
print()

# Example 1 - Creating a dictionary with 'None' as default values #

keys = ['apple', 'banana', 'orange']
my_dict = dict.fromkeys(keys)
print(my_dict)
print()

# Example 2 - Creating a dictionary with a specified default value #

keys = ['name', 'age', 'city']
default_value1 = 'unknown'
default_value2 = {'status':'unknown'}
mydict1 = dict.fromkeys(keys, default_value1)
mydict2 = dict.fromkeys(keys, default_value2)
print(mydict1)
print(mydict2)
