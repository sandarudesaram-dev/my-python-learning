# enumerate() function in Python #

'''
The enumerate() function in Python is a built-in function that adds a counter to an iterable, allowing you to access both the index and the value of each item during iteration. It returns an enumerate object, which can then be used in a for loop to unpack the index and the corresponding element.

Here's how enumerate() works:
'''

# Basic usage #

my_list = ['apple', 'banana', 'cherry']

for index, item in enumerate(my_list):
	print(f"Index: {index}, Item: {item}")

# Output #

# Index: 0, Item: apple
# Index: 1, Item: banana
# Index: 2, Item: cherry

print()

# Starting index #

# By default, enumerate() starts counting from 0. You can specify a different starting index using the start parameter:

my_list = ['apple', 'banana', 'cherry']

for index, item in enumerate(my_list, start=1):
	print(f"Index: {index}, Item: {item}")

# Output #

# Index: 1, Item: apple
# Index: 2, Item: banana
# Index: 3, Item: cherry

'''
~ Key Benefits:

- Readability: Simplifies code by eliminating the need to manually manage an index counter.
- Efficiency: More Pythonic and often more efficient than manually tracking indices.
- Flexibility: Works with any iterable, including lists, tuples, strings, and custom iterators.

~ When to use enumerate():

- When you need to access both the index and the value of elements while iterating through a sequence.
- When performing operations that depend on the position of an item in a list (e.g., treating the first or last item differently).
'''
