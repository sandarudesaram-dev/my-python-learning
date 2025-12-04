# Exercise 16: Count Unique Words (Given Approach) #

'''
Write a code to count the number of unique words in the given a sentence.

Given: Sentence = "dog is a simple animal dogs is selfless animal"
'''
print()

Sentence = "dog is a simple animal dogs is selfless animal "
print("Sentence:", Sentence)

words = Sentence.lower().split()
print("list of words:", words)
print("unique words:", set(words))

unique = {}
for word in set(words):
	count = words.count(word)
	unique[word] = count

print("Unique count:", unique)
print("Number of unique words in the sentence:", len(set(words)))
