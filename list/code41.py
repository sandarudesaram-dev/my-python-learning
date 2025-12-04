# Exercise 11: Remove empty strings from the list of strings #

'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
'''
print()

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("Before removing empty strings:", list1)

for i in list1:
	if i == "":
		list1.remove("")
print("After removing empty strings:", list1)