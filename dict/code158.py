# Exercise 15: Get the key of a minimum value (My Approach) #

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

minimum = min(sample_dict.values())

for i in sample_dict:
	if (sample_dict[i] == minimum):
		print(f"Least scored subject:", i)