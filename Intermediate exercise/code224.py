# Exercise 6: Filter dictionary to contain keys present in the given list #

'''
Given:

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']
'''
print()

d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
print(f"d1(Before filtering): {d1}")

l1 = ['A', 'C', 'F']

for i in l1:
	if i in d1:
		del d1[i]

print(f"di(After filtering): {d1}")