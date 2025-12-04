# Exercise 11: Print all prime numbers within a range #
# My approach (Essential code = 14 lines) #

print()

start = int(input('Start: '))
stop = int(input('Stop: '))

if (start > stop):
	start, stop = stop, start

i = start
while i <= stop:
	j = 1
	count = 0
	while j <= i:
		factor = i/j
		if (factor%1 == 0):
			count += 1
		j += 1
	if (count == 2):
		print(i, 'is a prime number')
	i += 1

# loop execution (e.g. Range = 1, 5) #

'''
i = start(1)
	i(1) <= stop(5) - True
		j(1) <= i(1) - True
			factor = 1/1 = 1
			if (1%1 == 0) - True
							>count = 1
		j(2) <= i(1) - False
	if (count == 2) - False


	i(2) <= stop(5) - True
		j(1) <= i(2) - True
			factor = 2/1 = 2
			if (2%1 == 0) - True
							>count = 1
		j(2) <= i(2) - True
			factor = 2/2 = 1
			if (1%1 ==0) - True
							>count = 2
		j(3) <= i(2) - False
	if (count == 2) - True
(Prints " i(2) is a prime number" )


	i(3) <= stop(5) - True
		j(1) <= i(3) - True
			factor = 3/1 = 3
			if (3%1 == 0) - True
							>count = 1
		j(2) <= i(3) - True
			factor = 3/2 = 1.5
			if (1.5%1 == 0) - False

		j(3) <= i(3) - True
			factor = 3/3 = 1
			if (i%1 == 0) - True
							>count = 2
		j(4) <= i(3) - False
	if (count == 2) - True
(Prints " i(3) is a prime number" )


	i(4) <= stop(5) - True
		j(1) <= i(4) - True
			factor = 4/1 = 4
			if (4%1 == 0) - True
							>count = 1
		j(2) <= i(4) - True
			factor = 4/2 = 2
			if (2%1 == 0) - True
							>count = 2
		j(3) <= i(4) - True
			factor = 4/3 = 1.33
			if (1.33%1 == 0) - False

		j(4) <= i(4) - True
			factor = 4/4 = 1
			if (1%1 == 0) - True
							>count = 3
		j(5) <= i(4) - False
	if (count == 2) - False


	i(5) <= stop(5) - True
		j(1) <= i(5) - True
			factor = 5/1 = 5
			if (5%1 == 0) - True
							>count = 1
		j(2) <= i(5) - True
			factor = 5/2 = 2.5
			if (2.5%1 == 0) - False

		j(3) <= i(5) - True
			factor = 5/3 = 1.66
			if (1.66%1 == 0) - False

		j(4) <= i(5) - True
			factor = 5/4 = 1.25
			if (1.25%1 == 0) - False

		j(5) <= i(5) - True
			factor = 5/5 = 1
			if (1%1 == 0) - True
							>count = 2
		j(6) <= i(5) - False
	if (count == 2) -True
(Prints " i(5) is a prime number" )


	i(6) <= stop(5) - False
'''