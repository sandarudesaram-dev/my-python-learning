# Exercise 1: Reverse each word of a string (Approach 2) #

'''
Given: str = 'My Name is Jessa'
'''
print()

str = 'My Name is Jessa'
print(f"Original string: {str}")

lt = [i[::-1] for i in str.split()]

rev = ''
for word in lt:
	rev += word
	rev += ' '
print(f"Reversed string: {rev}")