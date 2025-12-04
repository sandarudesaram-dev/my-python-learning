# Exercise 6: Count Specific Word From a File #

'''
Write a program to count the occurrences of a specific word (e.g., “hello”) in a given file.
'''
print()

def Occurrences(file_name, word):
	try:
		lt = []
		string = ''
		count = 0
		with open(file_name, "r") as f:
			content = f.read()
			for i in content:
				if (i == ' ' or i == '\n' or i == '.' or i == ',' or i == '[' or i == ']' or i == '(' or i == ')' or i == '{' or i == '}' or i == '/' or i == '<' or i == '>' or i == '?' or i == ':' or i == ';'):
					lt.append(string)
					string = ''
				else:
					string += i
			for j in lt:
				if (j == word):
					count += 1
		print(f"Number of occurrences of the word '{word}' in '{file_name}' = {count}")
	except FileNotFoundError:
		print(f"{file_name} doesn't exist")

Occurrences("test.txt", "the")
