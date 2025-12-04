# Exercise 5: Count Total Number of Characters in File (My Approach) #

'''
Write a function that takes a filename as input and returns the total number of characters in that file (including spaces and newlines).
'''
print()

def char_count(file_name):
	try:
		with open(file_name, "r") as f:
			lt = []
			for i in f.read():
				lt.append(i)
		return len(lt)
	except FileNotFoundError:
		print(f"{file_name} doesn't exist")

file = "test.txt"
chars = char_count(file)
print("Number of characters in the file:", chars)