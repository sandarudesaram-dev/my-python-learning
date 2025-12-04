# Exercise 6: Count the total number of digits in a number #

print()

num = int(input('Number>> '))

count = 0
n = num

if (n < 0):
	n *= -1

while n > 0:
	count += 1
	n //= 10

print('Total number of digits in', num, '=', count)