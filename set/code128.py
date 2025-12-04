# Exercise 16.1 : Count Unique Words #

'''
Write a code to count the number of unique words in the given a sentence.

Given: Sentence = "dog is a simple animal dogs is selfless animal"
'''
print()

# 1 #

Sentence = "Dog is a simple animal dog is selfless animal "
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

print()

# 2 #

Sentence = "Dog is a simple animal dog is selfless animal "
print("Sentence:", Sentence)

words = Sentence.split()
print("list of words:", words)
print("unique words:", set(words))

unique = {}
for word in set(words):
	count = words.count(word)
	unique[word] = count

print("Unique count:", unique)
print("Number of unique words in the sentence:", len(set(words)))

print()

# 3 #

Sentence = "Dog is a simple animal dog is selfless animal "
print("Sentence:", Sentence)

words = Sentence.upper().split()
print("list of words:", words)
print("unique words:", set(words))

unique = {}
for word in set(words):
	count = words.count(word)
	unique[word] = count

print("Unique count:", unique)
print("Number of unique words in the sentence:", len(set(words)))

