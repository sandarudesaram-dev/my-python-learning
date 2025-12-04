# Exercise 6: Count Character Frequencies (My Approach) #

'''
Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

Given: string1 = 'Jessa'
'''
print()

string1 = 'Jessa'
print("string1:", string1)

mydict = {}
for i in string1:
	mydict[i] = mydict.get(i, 0) + 1

print("mydict:", mydict)