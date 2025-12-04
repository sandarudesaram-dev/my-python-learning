# Exercise 1: Reverse each word of a string (Approach 1) #

'''
Given: str = 'My Name is Jessa'
'''
print()

str = 'My Name is Jessa'
print(f"Original string: {str}")

lt = []
word = ''
for i in str:
	word += i
	if (i == ' '):
		lt.append(word)
		word = ''
lt.append(' ')
lt.append(word)

ltz = []
for j in lt:
	ltz.append(j[::-1])

rev = ''
for text in ltz:
	rev += text
print(f"Reversed string:{rev}")