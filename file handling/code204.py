# Exercise 7: Write To a File #

'''
Write a Python program to create a new file named “output.txt” and write the string “Hello, PYnative!” into it.
'''
print()

f = open("output.txt", "w")
f.write("Hello, PYnative!")
f.close()