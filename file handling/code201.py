# Exercise 5: Count Total Number of Characters in File (Given Approach) #

'''
Write a function that takes a filename as input and returns the total number of characters in that file (including spaces and newlines).
'''
print()

def char_count(file_name):
	try:
		with open(file_name, "r") as f:
			return len(f.read())
	except FileNotFoundError:
		print(f"{file_name} doesn't exist")

file = "sample.txt"
chars = char_count(file)
print(f"Number of characters in {file}: {chars}")