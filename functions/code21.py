# Exercise 6: Create a recursive function #

def fac(n):
	if (n == 0):
		return 1
	else:
		return n * fac(n-1)

factorial = fac(5)
print("Factorial of 5:", factorial)

# Function execution (e.g. n = 5) #

'''
step1: 5 * fac(4)	# So what is 4!? Ask myself again #
step2: 4 * fac(3)	# So what is 3!? Ask myself again #
step3: 3 * fac(2)	# So what is 2!? Ask myself again #
step4: 2 * fac(1)	# So what is 1!? Ask myself again #
step5: 1 * fac(0)	# So what is 0!? Ask myself again #
step6: fac(0) = 1

back to step5: 1 * 1 = 1
back to step4: 2 * 1 = 2
back to step3: 3 * 2 = 6
back to step2: 4 * 6 = 24
back to step1: 5 * 24 = 120
'''