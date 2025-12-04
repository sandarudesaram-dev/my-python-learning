# Exercise 14: Filter Tuples (Approach - 3) #

'''
Write a code to filter out students with scores less than 90 from a given a list of tuples.

Given: students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
'''
print()

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print("students:", students)

low_scorers = [student[0] for student in students if student[1] < 90]

low_scorers = tuple(low_scorers)
print("Students with scores below 90:", low_scorers)