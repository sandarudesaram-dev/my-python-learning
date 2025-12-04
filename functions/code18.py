# Exercise 3: Return multiple values from a function #

def calculation(x, y):
	addition = x + y
	subtraction = x - y
	return addition, subtraction

result = calculation(10, 40)
print(result)