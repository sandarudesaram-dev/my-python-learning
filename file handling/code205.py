# Exercise 8: Append To a File #

'''
Modify the previous program to append the string “This is an appended line.” to the end of “output.txt”.
'''
print()

f = open("output.txt", "a")
f.write("\nThis is an appended line.")
f.close()