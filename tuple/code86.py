# Exercise 14: Filter Tuples (Approach - 1) #

'''
Write a code to filter out students with scores less than 90 from a given a list of tuples.

Given: students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
'''
print()

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print("students:", students)

low_scorers = []

for i in range(len(students)):
	if (students[i][1] < 90):
		low_scorers.append(students[i][0])
low_scorers = tuple(low_scorers)
print("Students with scores less than 90:", low_scorers)