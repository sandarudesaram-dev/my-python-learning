# Exercise 9: Create a copy of a list (My Approach)  #

'''
Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
'''
print()

original_list = [10, 20, 30]

copy_list = []
copy_list.extend(original_list)
copy_list.insert(2, 300)

print("original_list:", original_list)
print("copy_list:", copy_list)