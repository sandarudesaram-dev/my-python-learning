# Exercise 7: Count Occurrences (My approach) #

'''
Count and print how many times 'Football' appears in the list
Given: sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
'''
print()

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print("sports:", sports)
print()

count = 0
for i in sports:
	if i == 'Football':
		count += 1
print("Number of times 'Football' appears in the list:", count)