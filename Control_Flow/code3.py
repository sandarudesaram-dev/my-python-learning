# Exercise 3: Calculate sum of all numbers from 1 to a given number #

print()

n = int(input('Number up to which sum should be calculated: '))

sum = 0
i = 1
while i <= n:
	sum += i
	i += 1

print('Sum of all numbers from 1 to', n, '=', sum)