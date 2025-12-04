# Exercise 2: Print the following pattern #

'''
1
12
123
1234
12345
'''
print()

i = 1
while i <= 5:
	j = 1
	while j <= i:
		print(j, end='')
		j += 1
	i += 1
	print()