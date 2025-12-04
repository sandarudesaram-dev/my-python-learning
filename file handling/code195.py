# Exercise 1: Read a File (Given Approach 2) #

'''
Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
'''
print()

try:
	with open("sample.txt", "r") as f:
		content = f.read()
		print(content)
except FileNotFoundError:
	print("Error: 'sample.txt' not found.")