# Exercise 2: Read File Line by Line (My Approach) #

'''
Write a Python program to read the text file named “sample.txt” line by line and print each line.
'''
print()

try:
	with open("sample.txt", "r") as f:
		print(f.readline())
		print(f.readline())
except FileNotFoundError:
	print("No such file or directory")