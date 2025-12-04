# Exercise 7: Print the following number pattern (Approach 3) #

'''
Given:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
print()

k = 1
for i in range(5, 0, -1):
	for j in range(1, i+1):
		print(k, end = ' ')
	print()
	k += 1