# Exercise 14: Reverse a integer number #

print()

num =int(input('Number to be reversed: '))

rev = 0
n = num
N = 0

while n > 0:
	N = n%10
	rev = rev*10 + N
	n //= 10
print('Reversed number:', rev)