# OOP Exercise 5: Define a property that must have the same value for every class instance (object) - (Given Approach - 2) #

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

class Bus(Vehicle):
	pass

class Car(Vehicle):
	pass

a = Vehicle("Hilux", 180, 10)
b = Bus("Rosa", 120, 8)
c = Car("Camry", 220, 24)

for i in (a, b, c):
	print(i.color, "colored", i.name, "has a max speed of", i.max_speed, "and a mileage of", i.mileage)