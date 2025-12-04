# Exercise 3: Sum and average of all numbers in a list (My approach) #

'''
Calculate and print the sum and average of all numbers in a list.
Given: my_list = [10, 20, 30, 40, 50]
'''
print()

my_list = [10, 20, 30, 40, 50]

print("Given list:", my_list)
print()

sum = 0
for i in my_list:
	sum += i

count = len(my_list)
avg = sum/count

print("Sum:", sum)
print("Average:", avg)