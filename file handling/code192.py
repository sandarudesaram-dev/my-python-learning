# Exercise 1: Read a File (My Approach 1) #

'''
Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
'''
print()

with open("sample.txt", "r") as f:
	print(f.read())