# Exercise 4: Reverse Dictionary mapping (Given Approach)#

'''
Given: ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
'''
print()

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
print(f"Original dict: {ascii_dict}")

rev = {value:key for key, value in ascii_dict.items()}

print(f"Reversed dict: {rev}")