# Exercise 5: Display all duplicate items from a list (Approach 2) #

'''
Given: sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
'''
print()

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
print(f"sample_list: {sample_list}")

exist = []
dup = []

for i in sample_list:
	if i not in exist:
		exist.append(i)
	else:
		dup.append(i)

print(f"Duplicate items: {dup}")