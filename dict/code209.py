# Exercise 15: Get the key of a minimum value (Given Approach 1: code158) #

'''
Write a code to print the key of minimum value from the following dictionary.

Given:

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}
'''
print()

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}

print("sample_dict:", sample_dict)

minimum = min(sample_dict, key=sample_dict.get)

# 'key' is an optional parameter for min(), max(), sorted(). It expects a function that tells Python how to compare the items. That function is applied to each element before comparing. #

print("Least scored subject:", minimum)