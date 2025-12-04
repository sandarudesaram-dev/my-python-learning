# Exercise 17: Find the sum of a series of a number up to n terms #

print()

print('Define series')

type = input('Type of sequence: ')

if (type == 'arithmetic'):
	a = int(input('First term: '))
	d = int(input('Common difference: '))
	n = int(input('nth term: '))
	sum = n/2 * ( 2*a + (n-1)*d )
	print('Sum of first', n, 'th terms =', sum)

elif (type == 'geometric'):
	while True:
		a = int(input('First term: '))
		r = int(input('Common ratio: '))
		n = int(input('nth term: '))
		if (r > 1):
			sum = ( a*(r**n - 1)) / (r-1)
			print('Sum of first', n, 'th terms =', sum)
			break
		elif (r < 1):
			sum = ( a*(1 - r**n)) / (1-r)
			print('Sum of first', n, 'th terms =', sum)
			break
		else:
			print('r cannot be equal to 1')
			print('Re-enter r')
			print()
			continue
else:
	print('Invalid type')
		