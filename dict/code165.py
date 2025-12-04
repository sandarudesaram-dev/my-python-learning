# Exercise 19: Sort Dictionary by Values (Approach 2) #

'''
Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).

Given: my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
'''
print()

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print("my_dict:", my_dict)

res = sorted(my_dict.items(), key = lambda item:item[1])
print("Sorted by values:", dict(res))