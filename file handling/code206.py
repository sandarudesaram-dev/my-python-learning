# Exercise 9: Copy a File #

'''
Write a program that takes two filenames as input (source and destination) and copies the content of the source file to the destination file.
'''
print()

def copy(source, destination):
	mode = input("Overwrite(w) or Append(a) :")
	try:
		with open(source, "r") as s, open(destination, mode) as d:
			content = s.read()
			d.write("\n" + content)
	except FileNotFoundError:
		print(f"'{source}' or '{destination}' doesn't exist.")
	except ValueError:
		print(f"Invalid mode.")

copy("source.txt", "destination.txt")