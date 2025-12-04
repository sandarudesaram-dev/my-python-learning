# Exercise 3.2: Remove items from a list while iterating (Approach 2) #

'''
In this question, you need to remove items from a list during iteration without creating a seperate copy of the list.

Remove numbers greater than 50

Given: number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
print()

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"number_list(Original): {number_list}")
print(f"ID: {id(number_list)}")

for i in range(len(number_list) - 1, -1, -1):
	if number_list[i] > 50:
		del number_list[i]

print(f"number_list(Altered): {number_list}")
print(f"ID: {id(number_list)}")
