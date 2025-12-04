# Exercise 6: Write all content of a file into a new file by skipping line number 5 (Approach 1) #

'''
Create a 'msg2.txt' file and add the below content to it.

Given 'msg1.txt' file:
	line1	
	line2
	line3
	line4
	line5
	line6
	line7
'''
print()

with open("msg1.txt", "r") as s, open("msg2.txt", "w") as d:
	content = s.readlines()
	for i in content:
		if (i != "line5\n"):
			d.write(i)