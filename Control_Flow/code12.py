# Exercise 13: Find the factorial of a given number #

print()

n = int(input('Number>> '))

i = 1
fac = 1
while i <= n:
	fac *= i
	i += 1
print('Factorial of', n, '=', fac)