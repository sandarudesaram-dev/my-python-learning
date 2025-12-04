# OOP Exercise 9: Check object is a subclass of a particular class #

'''
Given:

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

Write a code to check the following

1. Dog is a subclass of Animal? –> True
2. Animal is a subclass of Dog? –> False
3. Cat is a subclass of Animal? –> False
4. Puppy is a subclass of Animal –> True
5. Dog is a subclass of Dog –> True
'''
print()

class Animal:
	pass

class Dog(Animal):
	pass

class Puppy(Dog):
	pass

class Cat:
	pass

print("Dog is a subclass of Animal?", issubclass(Dog, Animal))
print("Animal is a subclass of Dog?", issubclass(Animal, Dog))
print("Cat is a subclass of Animal?", issubclass(Cat, Animal))
print("Puppy is a subclass of Animal?", issubclass(Puppy, Animal))
print("Dog is a subclass of Dog?", issubclass(Dog, Dog))