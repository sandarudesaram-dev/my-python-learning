# Exercise 19: Check if all items in the tuple are the same (Approach - 1) #

'''
tuple1 = (45, 45, 45, 45)
'''
print()

tuple1 = (45, 45, 45, 45)

if tuple1.count(45) == len(tuple1):
	print("All items in the tuple are the same")
else:
	print("All items in the tuple are not the same")