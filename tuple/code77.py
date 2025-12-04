# Exercise 8: Swap two tuples in Python #

'''
Given:
	tuple1 = (11, 22)
	tuple2 = (99, 88)
'''
print()
print("Before swapping,")

tuple1 = (11, 22)
tuple2 = (99, 88)

print("tuple1:", tuple1)
print("tuple2:", tuple2)

print()
print("After swapping,")

tuple1, tuple2 = tuple2, tuple1

print("tuple1:", tuple1)
print("tuple2:", tuple2)