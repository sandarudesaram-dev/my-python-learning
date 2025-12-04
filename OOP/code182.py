# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class (Approach 2) #

'''
Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
'''
print()

class Vehicle:
	def __init__(self, name, mileage, capacity):
		self.name = name
		self.mileage = mileage
		self.capacity = capacity

class Bus(Vehicle):
	pass

School_bus = Bus("School Volvo", 12, 50)

for i in (Vehicle, Bus):
	print("Is School_bus an instance of", i, ":", isinstance(School_bus, i))