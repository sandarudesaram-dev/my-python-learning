# Exercise 10: Initialize dictionary with default values (Given Approach) #

'''
In Python, we can initialize the keys with the same values.

Given:
	employees = ['Kelly', 'Emma']
	defaults = {"designation": 'Developer', "salary": 8000}
'''
print()

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

print("employees:", employees)
print("defaults:", defaults)

info = dict.fromkeys(employees, defaults)
print("info:", info)