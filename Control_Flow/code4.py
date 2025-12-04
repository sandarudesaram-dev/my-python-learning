# Exercise 4: Print multiplication table of a given number #

print()

n = int(input('Number>> '))

i = 0
while i <= 15:
	print(n, 'x', i, '=', n*i)
	i += 1