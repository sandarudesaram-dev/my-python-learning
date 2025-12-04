# Exercise 5: Create an inner function #

def outfun(a, b):
	square = a**2

	def addition(a, b):
		return a + b
	add = addition(a, b)

	return 5 + add

result = outfun(3, 5)
print(result)