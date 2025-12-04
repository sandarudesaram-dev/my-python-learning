# Exercise 2 #

'''
Get the list of doctors as per the given specialty and salary
'''
print()

import mysql.connector

con = mysql.connector.connect(host = "localhost", user = "test", password = "123", database = "python_db")

myc = con.cursor()

myc.execute("SELECT Doctor_Id, Doctor_Name FROM Doctor WHERE Salary > 25000 AND Speciality = 'Gynecologist'")

records = myc.fetchall()

for record in records:
	print(record)