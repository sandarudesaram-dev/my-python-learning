# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class (Given Approach) #

'''
Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
'''
print()

class Vehicle:
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

class Bus(Vehicle):
	pass

v = Bus("Volvo", 180, 12)
print("Vehicle Name:", v.name, ", Speed:", v.max_speed, ", Mileage:", v.mileage)