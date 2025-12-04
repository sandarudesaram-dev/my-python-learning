# Exercise 19: Check if all items in the tuple are the same (Approach - 2) #

'''
tuple1 = (45, 45, 45, 45)
'''
print()

tuple1 = (45, 45, 45, 45)

Result = all(i == tuple1[0] for i in tuple1)
print("All items in the tuple are the same:", Result)