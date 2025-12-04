# Exercise 1: Reverse each word of a string (Approach 1) #

'''
Given: str = 'My Name is Jessa'
'''
print()

str = 'My Name is Jessa'

j = ''
rev = ''
for i in str:
	if i != ' ':
		j += i 
	else:
		rev += (j[::-1] + ' ')
		j = ''
rev += j[::-1]
print(rev)

# Loop execution #

'''
str = 'My name is Jessa'

j = ''
rev = ''

i = 'M', 'y', ' ', 'N', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'J', 'e', 's', 's', 'a'

i = 'M'
	if i('M') != ' ' (True)
		j = 'M'
i = 'y'
	if i('y') != ' ' (True)
		j = 'My'
i = ' '
	if i(' ') != ' ' (False)
		rev = 'yM '
		j = ''

i = 'N'
	if i('N') != ' ' (True)
		j = 'N'
i = 'a'
	if i('a') != ' ' (True)
		j = 'Na'
i = 'm'
	if i('m') != ' ' (True)
		j = 'Nam'
i = 'e'
	if i('e') != ' ' (True)
		j = 'Name'
i = ' '
	if i(' ') != ' ' (False)
		rev = 'yM ' + 'emaN ' = 'yM emaN '
		j = ''

i = 'i'
	if i('i') != ' ' (True)
		j = 'i'
i = 's'
	if i('s') != ' ' (True)
		j = 'is'
i = ' '
	if i(' ') != ' ' (False)
		rev = 'yM emaN ' + 'si ' = 'yM emaN si '
		j = ''

i = 'J'
	if i('J') != ' ' (True)
		j = 'J'
i = 'e'
	if i('e') != ' ' (True)
		j = 'Je'
i = 's'
	if i('s') != ' ' (True)
		j = 'Jes'
i = 's'
	if i('s') != ' ' (True)
		j = 'Jess'
i = 'a'
	if i('a') != ' ' (True)
		j = 'Jessa'

rev = 'yM emaN si ' + 'asseJ' = 'yM emaN si asseJ'
'''
	
