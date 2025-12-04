# OOP Exercise 1: Create a Class with instance attributes (My Approach) #

'''
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''
print()

class Vehicle:
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage

	def info(self):
		return {
			"Max speed" : self.max_speed,
			"Mileage" : self.mileage
			}

v1 = Vehicle(230, 7000)
v2 = Vehicle(350, 15000)

print(v1.info())
print(v2.info())