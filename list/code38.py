# Exercise 9: Create a copy of a list (Given Approach - 3)  #

'''
Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
'''
print()

original_list = [10, 20, 30]

copy_list = original_list[:]
copy_list.append(40)

print("original_list:", original_list)
print("copy_list:", copy_list)