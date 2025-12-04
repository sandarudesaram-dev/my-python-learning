# Exercise 7: Accept any 3 strings from one input() call #

'''
Write a program to take 3 names as input from the user in a single call to the input() function.
'''
print()

name1, name2, name3 = input("Enter 3 names:").split()

print(f"name1: {name1}")
print(f"name2: {name2}")
print(f"name3: {name3}")