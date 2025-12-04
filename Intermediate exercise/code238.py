# Exercise 3: Remove items from a list while iterating (DEBUG - Attempt2 (FAIL))#

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
		number_list.insert(i, '')
for j in number_list:
	if j == '':
		number_list.remove(j)
print(number_list)
print(id(number_list))

# Loop(j) execution #

'''
number_list = [10, 20, 30, 40, 50, '', '', '', '', '']

j = 10, 20, 30, 40, 50, '', '', '', '', ''

j = 10
	if j(10) == '' (False)
j = 20
	if j(20) == '' (False)
j = 30
	if j(30) == '' (False)
j = 40
	if j(40) == '' (False)
j = 50
	if j(50) == '' (False)
j = ''
	if j('') == '' (True)
	number_list = [10, 20, 30, 40, 50, '', '', '', '']

j = ''
	if j('') == '' (True)
	number_list = [10, 20, 30, 40, 50, '', '', '']

j = ''
	if j('') == '' (True)
	number_list = [10, 20, 30, 40, 50, '', '']

j = ''
	if j('') == '' (True)
	number_list = [10, 20, 30, 40, 50, '']

j = ''
	if j('') == '' (True)
	number_list = [10, 20, 30, 40, 50]
'''