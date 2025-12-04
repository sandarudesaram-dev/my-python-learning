# Exercise 2: Read a text file into a variable and replace all newlines with spaces (My Approach) #

'''
Given: Assume you have a following text file (sample.txt).

Line1
line2
line3
line4
line5
'''
print()

with open("simple.txt", "r") as f:
	content = ''
	word = ''
	for i in f.read():
		if (i != "\n"):
			word += i
		else:
			content += (word + " ")
			word = ''
	content += i

print(content)