# zip() function #

# This function takes 2 or more iterables (like list, dict, string), aggregates them in a tuple and returns it #

print()

# Example: 1 #

names = ["Jane", "Doe", "Jason"]
comps = ["Apple", "Tesla", "Nvidia"]

info = list(zip(names, comps))
print(info)
print()

# Example: 2 #

names = ["Jane", "Doe", "Jason"]
comps = ["Apple", "Tesla", "Nvidia"]
salary = [20000, 45000, 34000]

details = zip(names, comps, salary)

for (i, j, k) in details:
	print(i, j, k)
print()

# Example: 3 #

row1 = [1, 2, 3, "+"]
row2 = [4, 5, 6, "-"]
row3 = [7, 8, 9, "*"]
row4 = [0, ".", "=", "/"]

num_pad = zip(row1, row2, row3, row4)

for (i, j, k, l) in num_pad:
	print(i, j, k, l)
print()

# Example: 4 #

names = ["Jane", "Doe", "Jason"]
comps = ["Apple", "Tesla", "Nvidia"]
salary = [20000, 45000, 34000]

details = zip(names, comps, salary)

for i in details:
	print(i)
print()

# Example: 5 #

r1 = ["X", "O", "O"]
r2 = ["O", "X", "O"]
r3 = ["O", "O", "X"]

pattern = zip(r1, r2, r3)

for (i, j, k) in pattern:
	print(i, j, k)
print()

# Example: 5 #

r1 = ["X", "O", "O"]
r2 = ["O", "X", "O"]
r3 = ["O", "O", "X"]

pattern = zip(r1, r2, r3)

for (i, j, k) in pattern:
	print(i + j + k)
print()
