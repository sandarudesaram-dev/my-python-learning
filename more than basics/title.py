# title() method in Python #

'''
The title() method in Python is a built-in string method used to convert a string into "title case". This means it capitalizes the first letter of each word in the string and converts all other letters to lowercase.

~ Syntax:

string.title()

~ Return Value:

The title() method returns a copy of the original string with the title case formatting applied. It does not modify the original string.

~ How it works:

The method identifies "words" based on non-alphabetic characters (like spaces, hypens, numbers, or symbols) acting as seperators. It then capitalizes the first letter of each identified word and converts the remaining letters within that word to lowercase.
'''

# Example #

text1 = "hello world"
print(text1.title())		# Output: Hello World #

text2 = "tHIs iS a TEST"
print(text2.title())		# Output: This Is A Test #

text3 = "python-programming 101"
print(text3.title())		# Output: Python-Programming 101 #

'''
~ Important Notes

o The title() method treats characters after numbers or symbols as the start of a new "word" and will capitalize the first letter following them.

o It doe snot handle special cases of title casing such as maintaining capitalization for acronyms or proper nouns that are not at the beginning of a "word" as defined by the method. For more advanced title casing rules, external libraries like titlecase might be necessary.
'''
