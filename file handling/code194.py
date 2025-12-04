# Exercise 1: Read a File (Given Approach 1) #

'''
Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
'''
print()

try:
	with open("sample.txt", "r") as f:
		print(f.read())
except FileNotFoundError:
	print("No such file or directory")