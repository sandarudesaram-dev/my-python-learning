# Exercise 4: Reverse a list (My approach) #

'''
Given: list1 = [100, 200, 300, 400, 500]
'''
print()

list1 = [100, 200, 300, 400, 500]

print("Given list:", list1)
print()

rev_list = []

i = len(list1) - 1
while i >= 0:
	rev_list.append(list1[i])
	i -= 1
print("Reversed list:", rev_list)