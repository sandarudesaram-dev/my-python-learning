# Exercise 17: Sort a tuple of tuples by 2nd item (My Approach - 1) #

'''
Given: tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
'''
print()

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print("Unsorted tuple with tuples:", tuple1)

list1 = []
for tuple2 in tuple1:
	list2 = list(tuple2)
	list1.append(list2)
print("Unsorted list with lists:", list1)

reverse = []
for list2 in list1:
	list2.reverse()
	reverse.append(list2)
print("Unsorted list with reversed lists:", reverse)

reverse.sort()
print("Sorted list with reversed lists:", reverse)

sorted = []
for reverse_list in reverse:
	reverse_list.reverse()
	sorted.append(reverse_list)
print("Sorted list with lists:", sorted)

sorted_list = []
for list in sorted:
	tuple2 = tuple(list)
	sorted_list.append(tuple2)
print("Sorted list with tuples:", sorted_list)

sorted_tuple = tuple(sorted_list)
print("Sorted tuple with tuples:", sorted_tuple)