# sorted() - function #

'''
~ The sorted() function in Python is used to return a new sorted list from the items in any iterable (like lists, tuples, dictionaries, sets, etc.), without modifying the original iterable.

~ Basic syntax:

sorted(iterable, *, key = None, reverse = False)

~ Parameters:
	> iterable: The sequence or collection you want to sort (e.g., list, tuple, string, set, dictionary).
	> key(optional): A function that serves as a key for short comparison (e.g., len, str.lower)
	> reverse(optional): A Boolean. If True, the sorted list is reversed (descending order)


~ The * in the sorted() function means:
	 From this point on, you must use the argument names (like key = or reverse = ) when calling the function.

~ The key parameter in the sorted() function is used to specify a fuction that tells Python how to sort the items. Instead of sorting items directly, Python will apply the key function to each item first, and then sort based on the result of that function.
'''
print()

numbers = (3, 1, 4, 1, 5)
print(sorted(numbers, reverse = True))
print()

fruits = ["banana", "apple", "cherry", "kiwi"]
print(sorted(fruits))
print(sorted(fruits, key = len))
print()

reports = (("Jacob", 56), ("Samuel", 87), ("Jane", 91), ("Malcom", 78))
print(sorted(reports))
print(sorted(reports, key = lambda info:info[1]))
print()

neighborhood = [("Squidward", "F", 60), ("Sandy", "A", 33), ("Patrick", "D", 36), ("Spongebob", "B", 20), ("Mr.Krabs", "C", 78)]
print(sorted(neighborhood))
print(sorted(neighborhood, key = lambda grade:grade[1]))
print(sorted(neighborhood, key = lambda mark:mark[2]))
print(sorted(neighborhood, key = lambda mark:mark[2], reverse = True))