# Exercise 12: Delete a list of keys from a dictionary (Given Approach 1) #

'''
Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
'''
print()

sample_dict = {
	"name": "Kelly",
	"age": 25,
	"salary": 8000,
	"city": "New York"
}

print("sample_dict:", sample_dict)

keys = ["name", "salary"]

for k in keys:
	sample_dict.pop(k)

print("After deleting a list of keys:", sample_dict)