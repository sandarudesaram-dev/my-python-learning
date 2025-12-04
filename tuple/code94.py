# Exercise 17: Sort a tuple of tuples by 2nd item (My Approach - 2) #

'''
Given: tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
'''
print()

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print("Unsorted tuple:", tuple1)

ans = tuple(sorted(tuple1, key = lambda num:num[1]))
print("Sorted tuple:", ans)