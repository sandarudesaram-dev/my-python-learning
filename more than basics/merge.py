# merging dictionaries #

'''
The ** operator can be used to merge 2 or more dictionaries into a new dictionary. This is a concise way to combine dictionary contents. If duplicate keys exist, the value from the rightmost dictionary in the merge operation will overwrite previous values.
'''
print()

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4, "b":5}
dict3 = {"e":3, "b":1}

print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)
print()

merged_dict1 = {**dict1, **dict2, ** dict3}
print("merged_dict1 = {**dict1, **dict2, **dict3}")
print(merged_dict1)
print()

merged_dict2 = {**dict2, **dict3, **dict1}
print("merged_dict2 = {**dict2, **dict3, **dict1}")
print(merged_dict2)
print()

merged_dict3 = {**dict1, **dict2, **dict1}
print("merged_dict3 = {**dict1, **dict2, **dict1}")
print(merged_dict3)