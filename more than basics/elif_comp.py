# Using elif in list comprehension #

'''
~ You cannot use elif keyword in the same way as you do in the if/elif/else block.

syntax: [expression_1 if condition_1 else expression_2 if condition_2 else expression_3 for item in iterable]

Explanation:

~ expression_1 if condition_1:
	This is the first condition. If condition_1 is true, expression_1 is evaluated and included in the new list.

~ else expression_2 if condition_2:
	If condition_1 is false, the program then checks condition_2. If condition_2 is true, expression_2 is included. This effectively acts as your elif.

~ else expression_3:
	If neither condition_1 nor condition_2 is true, expression_3 is the fallback value, similar to the else clause in a regular if/elif/else statement.
'''
print()

# Example 1 #

numbers = [1, 5, 10, 15, 20]
print("numbers:", numbers)

categories = ["Small" if (n < 5) else "Medium" if (n < 15) else "Large" for n in numbers]
print("categories:", categories)

print()

# Example 2 #

mix = [1, 4, 9872, 632, 367, 2398, -218, -7, 12, 32, -27]
print("mix:", mix)

categories = ["Super small" if (n < -100) else "Extra small" if (n < -10) else "Small" if (n < 0) else "Medium" if (n < 10) else "Large" if (n < 100) else "Extra Large" if (n < 1000) else "Super Large" for n in mix]
print("categories:", categories)
