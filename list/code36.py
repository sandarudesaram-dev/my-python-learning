# Exercise 9: Create a copy of a list (Given Approach - 1)  #

'''
Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
'''
print()

original_list = [10, 20, 30]

copy_list = original_list.copy()
copy_list.pop()

print("original_list:", original_list)
print("copy_list:", copy_list)