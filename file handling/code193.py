# Exercise 1: Read a File (My Approach 2) #

'''
Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
'''
print()

f = open("sample.txt", "r")
print(f.read())
f.close()