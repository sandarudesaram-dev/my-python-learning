# Exercise 14: Rename key of a dictionary (Given Approach) #

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

sample_dict['location'] = sample_dict.pop('city')
# pop() method in dict is used to remove a key and return its corresponding value #
print("After renaming key:", sample_dict)