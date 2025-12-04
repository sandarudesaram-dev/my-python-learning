# Exercise 3: Sum and average of all numbers in a list (Given approach) #

'''
Calculate and print the sum and average of all numbers in a list.
Given: my_list = [10, 20, 30, 40, 50]
'''
print()

my_list = [10, 20, 30, 40, 50]

print("Given list:", my_list)
print()

total_list = sum(my_list)
avg = total_list / len(my_list)

print("Sum:", total_list)
print("Average:", avg)