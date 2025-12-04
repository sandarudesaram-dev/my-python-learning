# Exercise 10: Check Superset #

'''
Check if set2 = {10, 20, 30, 40} is a superset of set1 = {10, 20}.

Given:
	set1 = {10, 20}
	set2 = {10, 20, 30, 40}
'''
print()

set1 = {10, 20}
set2 = {10, 20, 30, 40}

print("set1:", set1)
print("set2:", set2)

res = set2.issuperset(set1)
print("set2 is a superset of set1:", res)