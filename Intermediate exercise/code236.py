# Exercise 3: Remove items from a list while iterating (HAS A BUG)#

'''
In this question, you need to remove items from a list during iteration without creating a separate copy of the list.

Remove numbers greater than 50

Given: number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
print()

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(number_list)
print(id(number_list))

for i in range(len(number_list)):
	if number_list[i] > 50:
		number_list.pop(i)
print(number_list)
print(id(number_list))

# Loop execution #

'''
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = range(10) = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

i = 0
	if number_list[0] = 10 > 50 (False)
i = 1
	if number_list[1] = 20 > 50 (False)
i = 2
	if number_list[2] = 30 > 50 (False)
i = 3
	if number_list[3] = 40 > 50 (False)
i = 4
	if number_list[4] = 50 > 50 (False)
i = 5
	if number_list[5] = 60 > 50 (True)
	number_list.pop(5)
	===> number_list = [10, 20, 30, 40, 50, 70, 80, 90, 100]

i = 6
	if number_list[6] = 80 > 50 (True)
	number_list.pop(6)
	===> number_list = [10, 20, 30, 40, 50, 70, 90, 100]

i = 7
	if number_list[7] = 100 > 50 (True)
	number_list.pop(7)
	===> number_list = []10, 02, 30, 40, 50, 70, 90]

i = 8
	if number_list[8] <===== INDEX OUT OF RANGE
'''