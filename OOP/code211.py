class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def info(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")

class Student(Person):
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self.grade = grade
	def is_pass(self):
		if self.grade >= 50:
			print("Pass")
		else:
			print("Fail")

s1 = Student("Jane Doe", 25, 8)

s1.info()
print()

s1.is_pass()
