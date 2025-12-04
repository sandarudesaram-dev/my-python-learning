# Exercise 2: Read text file into a variable and replace all newlines with space (Approach 2) #

'''
Given: Assume you have a following text file (sample.txt).

Line1
line2
line3
line4
line5
'''
print()

with open("sample.txt", "r") as f:
	data = f.read().replace('\n', ' ')
print(data)