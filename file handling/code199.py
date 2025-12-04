# Exercise 4: Count Words From a File #

'''
Create a function that takes a filename as input and returns the total number of words in that file.
'''
print()

def word_count(file_name):
	count = 1
	with open(file_name, "r") as f:
		content = f.read()
		for i in content:
			if (i == ' ' or i == '\n'):
				count += 1		
	return count

file = "test.txt"
words = word_count(file)
print("Number of words in the file:", words)