# Exercise 5: Accept a list of 5 float numbers as an input from the user #

list = []

for i in range(5):
	num = float(input("Enter float number>>"))
	list.append(num)

print("list:", list)
