# Exercise 1: Calculate the multiplication and sum of two numbers (My approach - 2) #

'''
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
Given 1: number1 = 20
	 number2 = 30
Given 2: number1 = 40
	 number2 = 30
'''
print()

def product_sum(number1, number2):
	product = number1 * number2

	if (product <= 1000):
		return product
	else:
		return (number1 + number2)

x = int(input("number1:"))
y = int(input("number2:"))

set = product_sum(x, y)
print("The result is", set)
