# Exercise 3.2: Remove items from a list while iterating (Approach 1) #

'''
In this question, you need to remove items from a list during iteration without creating a seperate copy of the list.

Remove numbers greater than 50

Given: number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
print()

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"number_list(Original): {number_list}")
print(f"ID: {id(number_list)}")

n = len(number_list)

i = 0
while i < n:
	if number_list[i] > 50:
		del number_list[i]
		n -= 1
	else:
		i += 1

print(f"number_list(Altered): {number_list}")
print(f"ID: {id(number_list)}")

# Loop execution #

'''
n = 10
i = 0

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i(0) < n(10) - True
	number_list[i(0)] = 10
	if 10 > 50 - False
	i = 1

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i(1) < n(10) - True
	number_list[i(1)] = 20
	if 20 > 50 - False
	i = 2

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i(2) < n(10) - True
	number_list[i(2)] = 30
	if 30 > 50 - False
	i = 3

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i(3) < n(10) - True
	number_list[i(3)] = 40
	if 40 > 50 - False
	i = 4

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i(4) < n(10) - True
	number_list[i(4)] = 50
	if 50 > 50 - False
	i = 5

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i(5) < n(10) - True
	number_list[i(5)] = 60
	if 60 > 50 -True
		# 60 deleted #
		n = 9

number_list = [10, 20, 30, 40, 50, 70, 80, 90, 100]
i(5) < n(9) - True
	number_list[i(5)] = 70
	if 70 > 50 - True
		# 70 deleted #
		n = 8

number_list = [10, 20, 30, 40, 50, 80, 90, 100]
i(5) < n(8) - True
	number_list[i(5)] = 80
	if 80 > 50 - True
		# 80 deleted #
		n = 7

number_list = [10, 20, 30, 40, 50, 90, 100]
i(5) < n(7) - True
	number_list[i(5)] = 90
	if 90 > 50 - True
		# 90 deleted #
		n = 6

number_list = [10, 20, 30, 40, 50, 100]
i(5) < n(6) - True
	number_list[i(5)] = 100
	if 100 > 50 - True
		# 100 deleted #
		n = 5

number_list = [10, 20, 30, 40, 50]
i(5) < n(5) - False
'''
