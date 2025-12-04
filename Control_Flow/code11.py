# Exercise 12: Display Fibonacci series up to 10 terms #

'''
Fibonacci series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
fib(8) = 21
fib(9) = 34
fib(10) = 55
fib(11) = 89
fib(12) = 144 ...

e.g. ===> fib(4) = fib(2) + fib(3)
		i.e. fib(n) = fib(n-2) + fib(n-1)
'''
print()

print('Fibonacci series upto 10 terms\n')

fib_0 = 0
fib_1 = 1

print('fib( 0 ) =', fib_0)
print('fib( 1 ) =', fib_1)

for i in range(2,11):
	f = fib_0 + fib_1
	print('fib(', i, ') =', f)
	fib_0 = fib_1
	fib_1 = f

# loop execution #

'''
range(2,11)
i =2,3,4,5,6,7,8,9,10

i = 2,
	f = 0 + 1 = 1
				>(prints fib( 2 ) = 1 )
	fib_0 = 1
	fib_1 = 1

i = 3,
	f = 1 + 1 = 2
				>(prints fib( 3 ) = 2 )
	fib_0 = 1
	fib_1 = 2

i = 4,
	f = 1 + 2 = 3
				>(prints fib( 4 ) = 3 )
	fib_0 = 2
	fib_1 = 3

i = 5,
	f = 2 + 3 = 5
				>(prints fib( 5 ) = 5 )
	fib_0 = 3
	fib_1 = 5

i = 6,
	f = 3 + 5 = 8
				>(prints fib( 6 ) = 8 )
	fib_0 = 5
	fib_1 = 8

i = 7,
	f = 5 + 8 = 13
				>(prints fib( 7 ) = 13 )
	fib_0 = 8
	fib_1 = 13

i = 8,
	f = 8 + 13 = 21
				>(prints fib( 8 ) = 21 )
	fib_0 = 13
	fib_1 = 21

i = 9,
	f = 13 + 21 = 34
				>(prints fib( 9 ) = 34 )
	fib_0 = 21
	fib_1 = 34

i = 10,
	f = 21 + 34 = 55
				>(prints fib( 10 ) = 55 )
	fib_0 = 34
	fib_1 = 55
'''