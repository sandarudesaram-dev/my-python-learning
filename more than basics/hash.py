# hash() function in Python #

'''
The built-in hash() function in Python returns the hash value of an object. This hash value is an integer that uniquely represents the object's data, provided the object is hashable.

Key characteristics and uses of hash():

~ Hashable Objects: Only immutable objects (like numbers, strings, and tuples containing only hashable elements) can be hashed. Mutable objects (like lists and dictionaries) cannot be hashed because their content can change, which would lead to an inconsistent hash value.

~ Role in Data Structures: hash() is fundamental to the efficient operation of hash-based data structures like dictionaries and sets. It allows for quick lookups and comparisons by mapping keys to specific locations (buckets) within these structures.

~ Syntax: The syntax is straightforward: hash(object).

~ Custom Hashng: You can define custom hash behavior for your own classes by implementing the __hash__ method within the class. This method should return an integer hash value based on the object's immutable attributes. You should also implement the __eq__ method to define how instances of your class are compared for equality.

~ Hash Collisions: While hash functions aim to produce unique values, it's possible for different objects to generate the same hash value (a "hash collision"). Hash-based data structures are designed to handle these collisions, though excessive collisions can degrade performance.

~ Security Considerations: For security-sensitive applications like password storage, the hashlib module should be used instead of the built-in hash() function, as haslib provides secure cryptographic hash algorithms.
'''

# Example #

# Hashing immutable built-in types #
print(hash(123))		
print(hash("hello"))
print(hash((1, 2, 3)))

# Attempting to hash a mutable type (will raise a TypeError) #
try:
	print(hash([1, 2, 3]))
except TypeError as e:
	print(f"Error: {e}")

# Custom class with __hash__ and __eq__ #
class MyObject:
	def __init__(self, value):
		self.value = value
	def __eq__(self, other):
		return isinstance(other, MyObject) and self.value == other.value
	def __hash__(self):
		return hash(self.value)

obj1 = MyObject(10)
obj2 = MyObject(10)
print(hash(obj1))
print(hash(obj2))