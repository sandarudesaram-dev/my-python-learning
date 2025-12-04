# Question 1 (Given Approach) #

'''
Fetch Hospital and Doctor Information using hospital Id and doctor Id #
'''
print()

import mysql.connector

con = mysql.connector.connect(host ="localhost", user = "test", password="123", database = "python_db")

myc = con.cursor()

myc.execute("SELECT * FROM Doctor WHERE Doctor_Id = 104")
records = myc.fetchall()

for record in records:
	print(f"Doctor_Id = {record[0]}")
	print(f"Doctor_Name = {record[1]}")
	print(f"Hospital_Id = {record[2]}")
	print(f"Joining_Date = {record[3]}")
	print(f"Speciality = {record[4]}")
	print(f"Salary = {record[5]}")
	print(f"Experience = {record[6]}")

myc.execute("SELECT * FROM Hospital WHERE Hospital_Id = 1")
records = myc.fetchall()

print()

for record in records:
	print(f"Hospital_Id = {record[0]}")
	print(f"Hospital_Name = {record[1]}")
	print(f"Bed_Count = {record[2]}")