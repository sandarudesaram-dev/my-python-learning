# OOP Exercise 1: Create a Class with instance attributes (Given Approach) #

'''
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''
print()

class Vehicle:
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage

v1 = Vehicle(230, 7000)
v2 = Vehicle(350, 15000)

print('Max speed:', v1.max_speed, ',', 'Mileage:', v1.mileage)
print('Max speed:', v2.max_speed, ',', 'Mileage:', v2.mileage)