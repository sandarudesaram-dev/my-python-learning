# pow() function in Python #

'''
The pow() function in Python is a built-in function used to calculate the power of a number. It can take 2 or 3 arguments:

1. Two-argument form: pow(base, exp)

- This form calculates base raised to the power of exp (equivalent to base ** exp).
'''

# Example #

result = pow(2, 3)	# 2 raised to the power 3, which is 8
print(result)

'''
2. Three-argument form: pow(base, exp, mod)

- This form calculates (base ** exp) % mod, which is the remainder of base raised to the power of exp divided by mod.
- This is particularly useful for modular exponentiation and is computed more efficiently than calculating base ** exp and then taking the modulus.
- When using the three-argument form, base, exp, and mod must be of integer types, and exp must be non-negative.
'''

# Example #

result = pow(10, 2, 9)	  # (10 ** 2) % 9, which is (100) % 9 = 1
print(result)

'''
Key differences and considerations:

- pow() vs. operator'**':
The pow(base, exp) function is equivalent to the base ** exp operator for simple exponentiation. However, pow() offers the advantage of modular exponentiation with its optional third argument, which the ** operator does not support.

- Return type:
The pow() function generally returns an integer if both base and exp are integers and the result is an integer, If exp is negative, or if any argument is a float, the result will be a float.

- math.pow():
Python also has a pow() function within the math module (math.pow(x, y)). This version always returns a float, even if the result is a whole number. The built-in pow() is generally preffered unless you specifically need the float-returning behavior of math.pow().
'''