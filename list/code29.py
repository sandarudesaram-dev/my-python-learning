# Exercise 6: Find Maximum and Minimum (My approach) #

'''
Find and print the largest and smallest number in a list
Given: data = [8, 2, 15, 1, 9]
'''
print()

data = [8, 2, 15, 1, 9]

max = data[0]
min = data[0]

for i in data:
	if i >= max:
		max = i
	elif i <= min:
		min = i
print("Largest number in the list:", max)
print("Smallest number in the list:", min)

# loop execution #

'''
i = 8, 2, 15, 1, 9

i = 8,
	if i(8) >= max(8) - True
					max = i(8)

i = 2,
	if i(2) >= max(8) - False
	elif i(2) <= min(8) - True
					min = i(2)

i = 15,
	if i(15) >= max(8) - True
					max = i(15)

i = 1,
	if i(1) >= max(15)  - False
	elif i(1) <= min(2) - True
					min = i(1)

i = 9,
	if i(9) >= max(15) - False
	elif i(9) <= min(1) - False

max = 15
min = 1
'''