# Exercise 1: Perform Basic Set Operations #

'''
1. Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
2. Add Element: Add “grape” to the fruits set.
3. Remove Element: Remove “banana” from the fruits set.
4. Discard Element: Try to discard “mango” from the fruits set.
'''
print()

fruits = set(('apple', 'banana', 'mango', 'orange'))
print("After creating the set:", fruits)

fruits.add('grape')
print("After adding 'grape':", fruits)

fruits.remove('banana')
print("After removing 'banana':", fruits)

fruits.discard('mango')
print("After discarding 'mango':", fruits)