# Exercise 3: Dictionary from Lists (Given Approach 2) #

'''
Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
'''
print()

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print("keys:", keys)
print("values:", values)

mydict = {}
for i in range(len(keys)):
	mydict.update({keys[i]:values[i]})
print("mydict:", mydict)