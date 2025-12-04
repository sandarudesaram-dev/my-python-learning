# split() method in Python #

print()

'''
In Python, the split() method is a built-in string method used to divide a string into a list of substrings.Its behavior can be customized based on the arguments provided.
'''

# Example 1 - Splittting by whitespaces (default) #

sentence = "Python is a versatile language"
print("sentence:", sentence)
words = sentence.split(" ")
print("words:", words)
print()

# Example 2 - Splitting by a specific seperator #

data = "Name, Age, Location"
print("data:", data)
columns = data.split(",")
print("columns:", columns)
print()

# Example 3 - Limiting the number of splits (maxsplit) #

log_entry = "2025-08-03 INFO User logged in"
print("log_entry:", log_entry)
parts = log_entry.split(" ", 2)
print("parts:", parts)