# swapcase() method in Python #

'''
The swapcase() method in Python is a built-in string method that returns the copy of the string with the case of all alphabetic characters swapped. Lowercase letters are converted to uppercase, and the uppercase letters are converted to lowercase. Non-alphabetic characters (numebers, symbols, spaces) remain unchanged.

~ Here's how it works:

o Call swapcase() on a string: You invoke the method directly on a string object.
o Returns a new string: The swapcase() method does not modify the original string; instead, it returns a new string with the cases swapped.
'''

# Example #

my_string = "Hello World 123!"
swapped_string = my_string.swapcase()
print(swapped_string)			# Output: hELLO wORLD 123!