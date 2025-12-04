# Exercise 8: Create an inner function (Given approach)#

'''
Question Description:

~ Create an outer function that accepts two strings, x & y (where x = 'Emma' & y = 'Kelly').

~ Create an inner function within the outer function that concatenates x & y.

~ Finally, the outer function will join the word 'Developers' to the result of the inner function's concatenation.
'''
print()

def outer(x, y):
	def inner(x, y):
		return x + y
	z = inner(x, y)
	return z + "Developers"

x = input("x:")
y = input("y:")

res = outer(x, y)
print(res)