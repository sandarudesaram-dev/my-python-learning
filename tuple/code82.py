# Exercise 11: Function Returning Tuple (My Approach)

'''
Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.

Given:

def get_min_max(numbers):
    # Write your code here

# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")
'''
print()

def get_min_max(numbers):
	numbers.sort()
	min = numbers[0]
	max = numbers[len(numbers)-1]
	return (min, max)

my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")