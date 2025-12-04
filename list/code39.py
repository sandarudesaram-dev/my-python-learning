# Exercise 10: Combine two lists (My Approach) #

'''
Combine given two lists into a single list and print it.
Given:
	list_a = [1, 2]
	list_b = [3, 4]
'''
print()

list_a = [1, 2]
list_b = [3, 4]

combined_list = list(list_a)
combined_list.extend(list_b)

print("list_a:", list_a)
print("list_b:", list_b)
print("combined_list:", combined_list)