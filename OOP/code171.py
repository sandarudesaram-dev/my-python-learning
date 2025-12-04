# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class (My Approach) #

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

	def info(self):
		print("Vehicle Name:", self.name, ", Speed:", self.max_speed, ", Mileage:", self.mileage)

class Bus(Vehicle):
	pass

v = Bus("Volvo", 180, 12)
v.info()