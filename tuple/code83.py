# Exercise 12: Comparing Tuples #

'''
Compare two tuples and find out which one is “greater” and why?

Given:
	t1 = (1, 2, 3)
	t2 = (1, 2, 4)
'''
print()

print("Python compares tuples lexicographically (element by element) from left to right. The first pair of elements that differ determines the outcome.")
print()

t1 = (1, 2, 3)
t2 = (1, 2, 4)

print("t1:", t1)
print("t2:", t2)

if (t1 > t2):
	print("t1 is greater than t2")
elif (t1 < t2):
	print("t1 is less than t2")
else:
	print("t1 is equal to t2")