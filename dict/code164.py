# Exercise 19: Sort Dictionary by Values (Approach 1) #

'''
Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).

Given: my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
'''
print()

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print("my_dict:", my_dict)

my_dict1 = {}
for value in set(sorted(my_dict.values())):
	for key, Value in my_dict.items():
		if (value == Value):
			my_dict1[key] = Value

print("Sorted by values:", my_dict1)

# loop execution #

'''
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
my_dict1 = {}

sorted(my_dict.values()) = [1, 1, 2, 3, 4]
set(sorted(my_dict.values())) = {1, 2, 3, 4}
value = 1, 2, 3, 4

value = 1
	key = 'Jessa', 'Kelly', 'Jon', 'Kerry', 'Joy'
	Value = 3, 1, 2, 4, 1
		key = 'Jessa', Value = 3
			if value(1) == Value(3) - False
		key = 'Kelly', Value = 1
			if value(1) == Value(1) - True
my_dict1 = {'Kelly':1}
		key = 'Jon', Value = 2
			if value(1) == Value(2) - False
		key = 'Kerry', Value = 4
			if value(1) == Value(4) - False
		key = 'Joy', Value = 1
			if value(1) == Value(1) - True
my_dict1 = {'Kelly':1, 'Joy':1}

value = 2
	key = 'Jessa', 'Kelly', 'Jon', 'Kerry', 'Joy'
	Value = 3, 1, 2, 4, 1
		key = 'Jessa', Value = 3
			if value(2) == Value(3) - False
		key = 'Kelly', Value = 1
			if value(2) == Value(1) - False
		key = 'Jon', Value = 2
			if value(2) == Value(2) - True
my_dict1 = {'Kelly':1, 'Joy':1, 'Jon':2}
		key = 'Kerry', Value = 4
			if value(2) == Value(4) - False
		key = 'Joy', Value = 1
			if value(2) == Value(1) - False

value = 3
	key = 'Jessa', 'Kelly', 'Jon', 'Kerry', 'Joy'
	Value = 3, 1, 2, 4, 1
		key = 'Jessa', Value = 3
			if value(3) == Value(3) - True
my_dict1 = {'Kelly':1, 'Joy':1, 'Jon':2, 'Jessa':3}
		key = 'Kelly', Value = 1
			if value(3) == Value(1) - False
		key = 'Jon', Value = 2
			if value(3) == Value(2) - False
		key = 'Kerry', Value = 4
			if value(3) == Value(4) - False
		key = 'Joy', Value = 1
			if value(3) == Value(1) - False

value = 4
	key = 'Jessa', 'Kelly', 'Jon', 'Kerry', 'Joy'
	Value = 3, 1, 2, 4, 1
		key = 'Jessa', Value = 3
			if value(4) == Value(3) - False
		key = 'Kelly', Value = 1
			if value(4) == Value(1) - False
		key = 'Jon', Value = 2
			if value(4) == Value(2) - False
                key = 'Kerry', Value = 4
			if value(4) == Value(4) - True
my_dict1 = {'Kelly':1, 'Joy':1, 'Jon':2, 'Jessa':3, 'Kerry':4}
		key = 'Joy', Value = 1
			if value(4) == Value(1) - False

Therefore,
my_dict1 = {'Kelly':1, 'Joy':1, 'Jon':2, 'Jessa':3, 'Kerry':4}
'''

