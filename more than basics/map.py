# map() function #

'''
syntax: map(function, collection)

~ Applies a given function into all items in a collection.
'''
print()

# Example 1 #

def c_to_f(temp):
	return (temp * 9/5) + 32

celcius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
print("celcius_temps:", celcius_temps)

fahrenheit_temps = list(map(c_to_f, celcius_temps))
print("fahrenheit_temps:", fahrenheit_temps)

print()

# Example 2 #

celcius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
print("celcius_temps:", celcius_temps)

fahrenheit_temps = list(map(lambda temp: ((temp * 9/5) + 32), celcius_temps))
print("fahrenheit_temps:", fahrenheit_temps)