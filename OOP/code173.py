# OOP Exercise 4: Class Inheritance (My Approach) #

'''
Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return {
		"Vehicle" : self.name,
		"Seating capacity" : capacity
		}
'''
print()

class Vehicle:
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self, capacity):
		return {
			"Vehicle" : self.name,
			"Seating capcity" : capacity
			}

class Bus(Vehicle):
	def seating_capacity(self, capacity = 50):
		return {
			"Vehicle":self.name,
			"Seating Capacity": capacity
			}

my_Bus = Bus("TATA", 120, 10)
print(my_Bus.seating_capacity())

my_Car = Vehicle("BMW", 280, 26)
print(my_Car.seating_capacity(5))