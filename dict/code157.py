# Exercise 14: Rename key of a dictionary (My Approach) #

'''
Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
'''
print()

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

print("sample_dict:", sample_dict)

sample_dict['location'] = sample_dict['city']
del sample_dict['city']

print("After renaming key:", sample_dict)