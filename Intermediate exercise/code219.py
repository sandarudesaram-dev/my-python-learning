# Exercise 4: Reverse Dictionary mapping (My Approach 1)#

'''
Given: ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
'''
print()

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
print(f"Original dict: {ascii_dict}")

rev = {}
for i, j in zip(ascii_dict, ascii_dict.values()):
	rev[j] = i
print(f"Reversed dict: {rev}")