# Exercise 4: Reverse Dictionary mapping (My Approach 2)#

'''
Given: ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
'''
print()

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
print(f"Original dict: {ascii_dict}")

rev = {}
for i in ascii_dict.values():
	for j in ascii_dict:
		if j not in rev.values():
			rev[i] = j
			break

print(f"Reversed dict: {rev}")