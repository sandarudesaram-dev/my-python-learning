# Exercise 7: Print the following number pattern (Approach 2) #

'''
Given:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
print()

for i, k in zip(range(5, 0, -1),range(1, 6)):
	for j in range(1, i+1):
		print(k, end = ' ')
	print()


# Just for my understanding #
print()
print(list(zip(range(5, 0, -1),range(1, 6))))