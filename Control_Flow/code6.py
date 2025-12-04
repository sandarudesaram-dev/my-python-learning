# Exercise 7: Print the following pattern #

'''
54321
4321
321
21
1
'''
print()

i = 1
while i <= 5:
	j = 6 - i
	while j >= 1:
		print(j, end='')
		j -= 1
	i += 1
	print()
		

