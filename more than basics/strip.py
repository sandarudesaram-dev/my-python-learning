# strip() method in Python #

'''
The strip() method in Python is a built-in string method used to remove leading and trailing characters from a string. It returns a new string with the characters removed, leaving the original string unchanged.

~ Syntax:

string.strip([chars])

~ Parameters:

- chars (optional): A string specifying the set of characters to be removed. If this argument is not provided, strip() will remove all leading and trailing whitespace characters (spaces, tabs, newlines, etc.) by default. The order of characters in chars does not matter.

~ How it works:

- Without chars argument: strip() identifies and removes any whitespace characters at the beginning and end of the string until it encounters a non-whitespace character.

- With chars argument: strip() identifies and removes any characters present in the chars string from the beginning and end of the target string, continuing until it encounters a character that is not in the chars set.
'''

# Examples #

# Removing default whitespace #
text1 = "   Hello, World!   "
cleaned_text1 = text1.strip()
print(f"'{cleaned_text1}'")		# Output: 'Hello, World!'

# Removing specific characters #
text2 = "---Python---"
cleaned_text2 = text2.strip('-')
print(f"'{cleaned_text2}'")		# Output: 'Python'

# Removing multiple specific characters #
text3 = "abccbaHelloabcba"
cleaned_text3 = text3.strip('abc')
print(f"'{cleaned_text3}'")		# Output: 'Hello'

# Characters within the string are not removed #
text4 = "  Hello  World  "
cleaned_text4 = text4.strip()
print(f"'{cleaned_text4}'")		# Output: 'Hello  World'