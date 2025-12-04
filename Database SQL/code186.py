# Question 1 (My Approach) #

'''
Fetch Hospital and Doctor Information using hospital Id and doctor Id #
'''
print()

import mysql.connector

con = mysql.connector.connect(host ="localhost", user = "test", password="123", database = "python_db")

myc = con.cursor()

myc.execute("SELECT * FROM Doctor WHERE Doctor_Id = 104")
res = myc.fetchall()

for i in res:
	print(i)

myc.execute("SELECT * FROM Hospital WHERE Hospital_Id = 1")
res = myc.fetchall()

for i in res:
	print(i)