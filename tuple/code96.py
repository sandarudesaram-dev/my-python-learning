# Exercise 18: Count Elements (My Approach - 2) #

'''
Write a code to counts the number of occurrences of item 50 from a tuple.

Given: tuple1 = (50, 10, 60, 70, 50)
'''
print()

tuple1 = (50, 10, 60, 70, 50)
print("tuple1:", tuple1)

count = 0
for item in tuple1:
	if (item == 50):
		count += 1
print("Number of occurrences of item 50:", count)