# Exercise 3 (Approach 1)#

'''
Get a list of doctors from a given hospital
'''
print()

import mysql.connector

con = mysql.connector.connect(host = "localhost", user = "test", password = "123", database = "python_db")

myc = con.cursor()

myc.execute("SELECT Doctor_Name, Speciality FROM Doctor WHERE Hospital_Id = 4")

records = myc.fetchall()

myc.execute("SELECT Hospital_Name FROM Hospital WHERE Hospital_Id = 4")

name = myc.fetchall()

print(f"List of doctors from Hospital: {name[0][0]}")
for record in records:
	print(record)