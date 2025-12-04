# Exercise 3: Dictionary from Lists (My Approach 1) #

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
for key, value in zip(keys, values):
	mydict[key] = value

print("mydict:", mydict)