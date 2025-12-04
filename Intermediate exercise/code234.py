# Exercise 2: Read text file into a variable and replace all newlines with space (Approach 1) #

'''
Given: Assume you have a following text file (sample.txt).

Line1
line2
line3
line4
line5
'''
print()

with open ("sample.txt", "r") as file:
	str = ''
	txt = file.readlines()
	for i in txt:
		word = ''
		for j in i:
			if j != "\n":
				word += j
			else:
				str += (word + ' ')
print(str + word)

# Loop execution #

'''
str = ''

txt = ['Line1\n', 'line2\n', 'line3\n', 'line4\n', line5]

i = 'Line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5'

i = 'Line1\n'
word = ''
	j = 'L', 'i', 'n', 'e', '1', '\n'

	j = 'L'
		if j('L') != "\n" (True)
		word = 'L'
	j = 'i'
		if j('i') != "\n" (True)
		word = 'Li'
	j = 'n'
		if j('n') != "\n" (True)
		word = 'Lin'
	j = 'e'
		if j('e') != "\n" (True)
		word = 'Line'
	j = '1'
		if j('1') != "\n" (True)
		word = 'Line1'
	j = '\n'
		if j('\n') != "\n" (False)
		str = 'Line1' + ' ' = 'Line1 '

i = 'line2\n'
word = ''
	j = 'l', 'i', 'n', 'e', '2', '\n'

	j = 'l'
		if j('l') != "\n" (True)
		word = 'l'
	j = 'i'
		if j('i') != "\n" (True)
		word = 'li'
	j = 'n'
		if j('n') != "\n" (True)
		word = 'lin'
	j = 'e'
		if j('e') != "\n" (True)
		word = 'line'
	j = '2'
		if j('2') != "\n" (True)
		word = 'line2'
	j = '\n'
		if j('\n') != "\n" (False)
		str = 'Line1 ' + 'line2' + ' '	= 'Line1 line2 '

i = 'line3\n'
word = ''
	j = 'l', 'i', 'n', 'e', '3', '\n'

	j = 'l'
		if j('l') != "\n" (True)
		word = 'l'
	j = 'i'
		if j('i') != "\n" (True)
		word = 'li'
	j = 'n'
		if j('n') != "\n" (True)
		word = 'lin'
	j = 'e'
		if j('e') != "\n" (True)
		word = 'line'
	j = '3'
		if j('3') != "\n" (True)
		word = 'line3'
	j = '\n'
		if j('\n') != "\n" (False)
		str = 'Line1 line2 ' + 'line3' + ' ' = 'Line1 line2 line3 '

i = 'line4\n'
word = ''
	j = 'l', 'i', 'n', 'e', '4', '\n'

	j = 'l'
		if j('l') != "\n" (True)
		word = 'l'
	j = 'i'
		if j('i') != "\n" (True)
		word = 'li'
	j = 'n'
		if j('n') != "\n" (True)
		word = 'lin'
	j = 'e'
		if j('e') != "\n" (True)
		word = 'line'
	j = '4'
		if j('4') != "\n" (True)
		word = 'line4'
	j = '\n'
		if j('\n') != "\n" (False)
		str = 'Line1 line2 line3 ' + 'line4' + ' ' = 'Line1 line2 line3 line4 '

i = 'line5'
word = ''
	j = 'l', 'i', 'n', 'e', '5'

	j = 'l'
		if j('l') != "\n" (True)
		word = 'l'
	j = 'i'
		if j('i') != "\n" (True)
		word = 'li'
	j = 'n'
		if j('n') != "\n" (True)
		word = 'lin'
	j = 'e'
		if j('e') != "\n" (True)
		word = 'line'
	j = '5'
		if j('5') != "\n" (True)
		word = 'line5'

str = 'Line1 line2 line3 line4 ' + 'line5' = 'Line1 line2 line3 line4 line5'
'''