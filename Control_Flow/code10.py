# Exercise 11: Print all prime numbers within a range #
# Given approach (Essential code = 9 lines) #

print()

start = int(input('Start: '))
stop = int(input('Stop: '))

if (start > stop):
	start, stop = stop, start

for num in range(start, stop+1):
	if (num > 1):
		for i in range(2, num):
			if (num%i == 0):
				break
		else:					# The 'else' block executes only if the loop finishes without hitting a 'break' #
			print(num, 'is a prime number') 

# loop exution (e.g. Range = 1, 5)#

'''
range = (0,6)
num = 0,1,2,3,4,5

num = 0,
	if (0 > 1) - False

num = 1,
	if (1 > 1) - False

num = 2,
	if (2 > 1) - True
		range = (2,2) - This range is empty, loop body never runs
				# else block gets executed #
> 2 is a prime number

num = 3,
	if (3 > 1) - True
		range = (2,3)
		i = 2
			if (3%2 == 0) - False
# 'else' block gets executed as loop didn't hit 'break' #
> 3 is a prime number

num = 4,
	if (4>1) - True
		range = (2,4)
		i = 2,3
			i = 2,
			if (4%2 == 0) - True # hits 'break' #

n = 5,
	if (5>1) - True
		range = (2,5)
		i = 2,3,4
			i = 2,
			if (5%2 == 0) - False
			i = 3,
			if (5%3 == 0) - False
			i = 4,
			if (5%4 == 0) - False
# 'else' bleck gets executed as loop didn't hit 'break #
> 5 is a prime number
'''
		