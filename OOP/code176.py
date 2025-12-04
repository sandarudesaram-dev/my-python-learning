# OOP Exercise 5: Define a property that must have the same value for every class instance (object) - (Given Approach - 1) #

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

print(a.color, "colored", a.name, "has a max speed of", a.max_speed, "and a mileage of", a.mileage)

print(b.color, "colored", b.name, "has a max speed of", b.max_speed, "and a mileage of", b.mileage)

print(c.color, "colored", c.name, "has a max speed of", c.max_speed, "and a mile age of", c.mileage)