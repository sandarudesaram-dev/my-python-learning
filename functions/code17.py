# Exercise 2: Create a function with variable length of arguments #

def myFun(*args):	# * tells Python to collect all extra positional arguments into a tuple #
	for arg in args:
		print(arg)

myFun(1, 2, 3)
myFun("Hello", "Sandaru")
myFun("Maths is Fun")
myFun(1.414, 1.732)
myFun("Hello", 3.14, True)
