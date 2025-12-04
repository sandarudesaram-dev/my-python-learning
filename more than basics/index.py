# index() method #

'''
index() method in Python is a built-in function used to find the position (index) of the first occurrence of a specified element within a sequenece.This method is available for various sequence types including lists, tuples and strings.

The general syntax for index() method is:

sequence.index(element, [start], [end])

Parameters:

~ element: The item whose index you want to find. This parameter is required.

~ start (optional): The index position from which the search should begin. If omitted, the search starts from the beginning of the sequence (index 0).

~ end (optional): The index position where the search should end (exclusive). If omitted, the search continues to the end of the sequence.

Return value:

The index() method returns the lowest index at which the specified element is found.

Error Handling:

If the element is not found within the specified search range (or the entire sequence if start and end are not provided), the index() method raises a ValueError.
'''
print()

# Example #

Test = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

index = Test.index('q')
print("Test.index('q'):", index)

# Example #

Test = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

index = Test.index('o', 10)
print("Test.index('o', 10):", index)