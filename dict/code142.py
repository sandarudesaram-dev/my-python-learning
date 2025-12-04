# Exercise 6: Count Character Frequencies (Given Approach) #

'''
Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

Given: string1 = 'Jessa'
'''
print()

def count_char_frequencies(input_string):
	frequency_dict = {}
	for char in input_string:
		frequency_dict[char] = frequency_dict.get(char, 0) + 1
	return frequency_dict

string1 = 'Jessa'
print("string1:", string1)

res = count_char_frequencies(string1)
print("frequency_dict:", res)