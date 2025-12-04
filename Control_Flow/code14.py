# Exercise 16: Calculate the cube of all numbers from 1 to a given number #

print()

num = int(input('Number up to which cubes are needed: '))

for i in range(1, num+1):
	print('Cube of', i, '=', i**3)