# Exercise 20: Check if All Values are Unique (Approach 1) #

'''
Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.

Given:
	dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique #
	dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated # 
	dict3 = {} # Empty dictionary (all values are vacuously unique) #
'''
print()

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'x':10, 'y':20, 'z':10}
dict3 = {}

def Unique_value_check(input_dict):
	unique = []
	for value in input_dict.values():	
		if value in unique:
			return False
			break
		unique.append(value)
	else:
		return True

res1 = Unique_value_check(dict1)
res2 = Unique_value_check(dict2)
res3 = Unique_value_check(dict3)

print("All values in dict1 are unique:", res1)
print("All values in dict2 are unique:", res2)
print("All values in dict3 are unique:", res3)