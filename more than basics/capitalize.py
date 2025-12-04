# capitalize() method in Python #

'''
The capitalize() method in Python is a built-in string method that converts the first character of a string to uppercase and all subsequent characters to lowercase. It does not modify the original string but returns a new string with the capitalization applied.

~ Syntax:

string.capitalize()

~ Parameters:

The capitalize() method does not take any parameters.

~ Return Value:

It returns a new string where the first character is uppercase and all other characters are lowercase.
'''

# Example #

text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)				# Output: Hello world

sentence = "PYTHON is AWESOME!"
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence)			# Output: Python is awesome!

'''
~ Note:

If the first character of the string is not an alphabet (e.g., a number, special character, or space), it will not be converted to uppercase, but any subsequent alphabetic characters will still be converted to lowercase.
'''