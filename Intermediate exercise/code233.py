# Exercise 1: Reverse each word of a string (Approach 2) #

'''
Given: str = 'My Name is Jessa'
'''
print()

def string_reverse(string):

	list = str.split()

	rev_list = [word[::-1] for word in list]

	rev = " ".join(rev_list)
	print(rev)

str = 'My Name is Jessa'

string_reverse(str)
