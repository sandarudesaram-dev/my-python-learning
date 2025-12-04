# Exercise 5: Display all duplicate items from a list (Approach 1) #

'''
Given: sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
'''
print()

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
print(f"sample_list: {sample_list}")

dict = {}
for i in sample_list:
	dict[i] = dict.get(i, 0) + 1

dup = []
for i, j in dict.items():
	if j != 1:
		dup.append(i)

print(f"Duplicate items: {dup}")