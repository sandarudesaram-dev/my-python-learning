# Exercise 3 (Approach 2) #

'''
Get a list of doctors from a given hospital
'''
print()

import mysql.connector

x = 2 # Hospital_Id #

con = mysql.connector.connect(host = "localhost", user = "test", password = "123", database = "python_db")

myc = con.cursor()

myc.execute("SELECT Doctor_Name, Speciality FROM Doctor WHERE Hospital_Id = %s", (x,))

records = myc.fetchall()

myc.execute("SELECT Hospital_Name FROM Hospital WHERE Hospital_Id = %s", (x,))

name = myc.fetchall()

print(f"List of doctors from Hospital: {name[0][0]}")
for record in records:
	print(record)