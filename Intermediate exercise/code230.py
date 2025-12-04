# Exercise 9: Modify the element of a nested list inside the following list #

'''
Given: list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

Change the element 35 to 3500.
'''
print()

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
print(f"Original list: {list1}")

list1[1][2][2][1] = 3500
print(f"Modified list: {list1}")