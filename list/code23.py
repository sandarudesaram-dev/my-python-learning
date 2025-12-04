# Exercise 2: Perform List Manipulation #

'''
Given: my_list = [10, 20, 30, 40, 50]
Perform following list manipulation operations on given list
	1.Change Element: Change the second element of the list to 200 and print the updated list.
	2.Append Element: Add 600 to the end of the list and print the new list.
	3.Insert Element: Insert 300 at the third position (index 2) of the list and print the result.
	4.Remove Element (by value): Remove 600 from the list and print the list.
	5.Remove Element (by index): Remove the element at index 0 from the list print the list.
'''
print()

my_list = [10, 20, 30, 40, 50]

print("Initial list:", my_list)
print()

# Q1 #
my_list[1] = 200
print("List after first alteration:", my_list)

# Q2 #
my_list.append(600)
print("List after second alteration:", my_list)

# Q3 #
my_list.insert(2, 300)
print("List after third alteration:", my_list)

# Q4 #
my_list.pop()
print("List after fourth alteration:", my_list)

# Q5 #
my_list.pop(0)
print("List after fifth alteration:", my_list)