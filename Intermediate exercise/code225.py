# Exercise 7: Print the following number pattern (Approach 1) #

'''
Given:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
print()

i = 5
k = 1

while i >= 1:
	j = 1
	while j <= i:
		print(k, end = ' ')
		j += 1
	print()
	k += 1
	i -= 1

# loop execution #

'''
i = 5
k = 1

i(5) >= 1 - True
	j = 1
	j(1) <= i(5) - True
		> 1 (without moving to the next line)
		j = 2
	j(2) <= i(5) - True
		> 1 (without moving to the next line)
		j = 3
	j(3) <= i(5) - True
		> 1 (without moving to the next line)
		j = 4
	j(4) <= i(5) - True
		> 1 (without moving to the next line)
		j = 5
	j(5) <= i(5) - True
		> 1 (without moving to the next line)
		j = 6
	j(6) <= i(5) - False

	# Breaks the row and starts a new line #
	k = 2
	i = 4

Pattern ===> 1 1 1 1 1 - (By loop i = 5)

i(4) >= 1 - True
	j = 1
	j(1) <= i(4) - True
		> 2 (without moving to the next line)
		j = 2
	j(2) <= i(4) - True
		> 2 (without moving to the next line)
		j = 3
	j(3) <= i(4) - True
		> 2 (without moving to the next line)
		j = 4
	j(4) <= i(4) - True
		> 2 (without moving to the next line)
		j = 5
	j(5) <= i(4) - False

	# Breaks the row and starts a new line #
	k = 3
	i = 3

Pattern ===> 1 1 1 1 1
	     2 2 2 2 - (By loop when i = 4)

i(3) >= 1 - True
	j = 1
	j(1) <= i(3) - True
		> 3 (without moving to the next line)
		j = 2
	j(2) <= i(3) - True
		> 3 (without moving to the next line)
		j = 3
	j(3) <= i(3) - True
		> 3 (without moving to the next line)
		j = 4
	j(4) <= i(3) - False

	# Breaks the row and starts a new line #
	k = 4
	i = 2

Pattern ===> 1 1 1 1 1 
	     2 2 2 2 
	     3 3 3 - (By loop when i = 3)

i(2) >= 1 - True
	j = 1
	j(1) <= i(2) - True
		> 4 (without moving to the next line)
		j = 2
	j(2) <= i(2) - True
		> 4 (without moving to the next line)
		j = 3
	j(3) <= i(2) - False

	# Breaks the row and starts a new line #
	k = 5
	i = 1

Pattern ===> 1 1 1 1 1 
	     2 2 2 2 
	     3 3 3
	     4 4 - (By loop when i = 2)

i(1) >= 1 - True
	j = 1
	j(1) <= i(1) - True
		> 5 (without moving to the next line)
		j = 2
	j(2) <= i(1) - False

	# Breaks the row and starts a new line #
	k = 6
	i = 0

Pattern ===> 1 1 1 1 1 
	     2 2 2 2 
	     3 3 3 
	     4 4 
	     5 - (By loop when i = 1)

i(0) >= 1 - False

Pattern ===> 1 1 1 1 1 
	     2 2 2 2 
	     3 3 3 
	     4 4 
	     5
'''