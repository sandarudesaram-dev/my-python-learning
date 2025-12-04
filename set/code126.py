# Exercise 16: Count Unique Words (My Approach) #

'''
Write a code to count the number of unique words in the given a sentence.

Given: Sentence = "dog is a simple animal dogs is selfless animal"
'''
print()

Sentence = "dog is a simple animal dogs is selfless animal "
print("Sentence:", Sentence)

list = []
j = ''
for i in Sentence:
	j += str(i)
	if i == ' ':
		list.append(j)
		j = ''
print("list of words:", list)
print("unique words:", set(list))

unique = {}
for word in set(list):
	count = list.count(word)
	unique[word] = count

print("Unique count:", unique)
print("Number of unique words in the sentence:", len(set(list)))

# loop execution #

'''
list = []
j = ''

i = 'd', 'o', 'g', ' ', 'i', 's', ' ', 'a', ' ', 's', 'i', 'm', 'p', 'l', 'e', ' ', 'a', 'n', 'i', 'm', 'a', 'l', ' ', 'd', 'o', 'g', 's', ' ', 'i', 's', ' ', 's', 'e', 'l', 'f', 'l', 'e', 's', 's', ' ', 'a', 'n', 'i', 'm', 'a', 'l', ' '

i = 'd'
	j = '' + 'd' = 'd'
	if i('d') == ' ' - False

i = 'o'
	j = 'd' + 'o' = 'do'
	if i('o') == ' ' - False

i = 'g'
	j = 'do' + 'g' = 'dog'
	if i('g') == ' ' - False

i = ' '
	j = 'dog' + ' ' = 'dog '
	if i(' ') == ' ' - True
		list = ['dog ']
		j = ''

i = 'i'
	j = '' + 'i' = 'i'
	if i('i') == ' ' - False

i = 's'
	j = 'i' + 's' = 'is'
	if i('s') == ' ' - False

i = ' '
	j = 'is' + ' ' = 'is '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ']
		j = ''

i = 'a'
	j = '' + 'a' = 'a'
	if i('a') == ' ' - False

i = ' '
	j = 'a' + ' ' = 'a '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ']
		j = ''

i = 's'
	j = '' + 's' = 's'
	if i('s') == ' ' - False

i = 'i'
	j = 's' + 'i' = 'si'
	if i('i') == ' ' - False

i = 'm'
	j = 'si' + 'm' = 'sim'
	if i('m') == ' ' - False

i = 'p'
	j = 'sim' + 'p' = 'simp'
	if i('p') == ' ' - False 

i = 'l'
	j = 'simp' + 'l' = 'simpl'
	if i('l') == ' ' - False

i = 'e'
	j = 'simpl' + 'e' = 'simple'
	if i('e') == ' ' - False

i = ' '
	j = 'simple' + ' ' = 'simple '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ', 'simple ']
		j = ''

i = 'a'
	j = '' + 'a' = 'a'
	if i('a') == ' ' - False

i = 'n'
	j = 'a' + 'n' = 'an'
	if i('n') == ' ' - False

i = 'i'
	j = 'an' + 'i' = 'ani'
	if i('i') == ' ' - False

i = 'm'
	j = 'ani' + 'm' = 'anim'
	if i('m') == ' ' - False

i = 'a'
	j = 'anim' + 'a' = 'anima'
	if i('a') == ' ' - False

i = 'l'
	j = 'anima' + 'l' = 'animal'
	if i('l') == ' ' - False

i = ' '
	j = 'animal' + ' ' = 'animal '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ', 'simple ', 'animal ']
		j = ''

i = 'd'
	j = '' + 'd' = 'd'
	if i('d') == ' ' - False

i = 'o'
	j = 'd' + 'o' = 'do'
	if i('o') == ' ' - False

i = 'g'
	j = 'do' + g' = 'dog'
	if i('g') == ' ' - False

i = 's'
	j = 'dog' + 's' = 'dogs'
	if i('s') == ' ' - False

i = ' '
	j = 'dogs' + ' ' = 'dogs '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ', 'simple ', 'animal ', 'dogs']
		j = ''

i = 'i'
	j = '' + 'i' = 'i'
	if i('i') == ' ' - False

i = 's'
	j = 'i' + 's' = 'is'
	if i('s') == ' ' - False

i = ' '
	j = 'is' + ' ' = 'is '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ', 'simple ', 'animal ', 'dogs ', 'is ']
		j = ''

i  = 's'
	j = '' + 's' = 's'
	if i('s') == ' ' - False

i = 'e'
	j = 's' + 'e' = 'se'
	if i('e') == ' ' - False

i = 'l'
	j = 'se' + 'l' = 'sel'
	if i('l') == ' ' - False

i = 'f'
	j = 'sel' + 'f' = 'self'
	if i('f') == ' ' - False

i = 'l'
	j = 'self' + 'l' = 'selfl'
	if i('l') == ' ' - False

i 'e'
	j = 'selfl' + 'e' = selfle
	if i('e') == ' ' - False

i = 's'
	j = 'selfle' + 's' = 'selfles'
	if i('s') == ' ' - False

i = 's'
	j = 'selfles' + 's' = 'selfless'
	if i('s') == ' ' - False

i = ' '
	j = 'selfless' + ' ' = 'selfless '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ', 'simple ', 'animal', 'dogs', 'is ', 'selfless ']
		j = ''

i = 'a'
	j = '' + 'a' = 'a'
	if i('a') == ' ' - False

i = 'n'
	j = 'a' + 'n' = 'an'
	if i('n') == ' ' - False

i = 'i'
	j =  'an' + 'i' = 'ani'
	if i('i') == ' ' - False

i = 'm'
	j = 'ani' + 'm' = 'anim'
	if i('m') == ' ' - False

i = 'a'
	j = 'anim' + 'a' = 'anima'
	if i('a') == ' ' - False

i = 'l'
	j = 'anima' + 'l' = 'animal'
	if i('l') == ' ' - False

i = ' '
	j = 'animal' + ' ' = 'animal '
	if i(' ') == ' ' - True
		list = ['dog ', 'is ', 'a ', 'simple ', 'animal ', 'dogs ', 'is ', 'selfless ', 'animal ']
		j = ''


list = ['dog ', 'is ', 'a ', 'simple ', 'animal ', 'dogs ', 'is ', 'selfless ', 'animal ']

set(list) = {'dog ', 'is ', 'a ', 'simple ', 'animal ', 'dogs ', 'selfless '}
'''