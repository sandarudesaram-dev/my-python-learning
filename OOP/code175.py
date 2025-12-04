# OOP Exercise 5: Define a property that must have the same value for every class instance (object) - (My Approach) #

'''
Define a class attribute "color" with a default value white. i.e., Every Vehicle should be white.

Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
'''
print()

class Vehicle:

	color = "White"

	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def info(self):
		print(self.color, "colored", self.name, "has a max speed of", self.max_speed, "and mileage of", self.mileage)

class Bus(Vehicle):
	pass

class Car(Vehicle):
	pass

a = Vehicle("Hilux", 180, 10)
b = Bus("Rosa", 120, 8)
c = Car("Camry", 220, 24)

a.info()
b.info()
c.info()