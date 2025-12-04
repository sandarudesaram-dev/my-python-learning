# Preparing required data for the exercises #

import mysql.connector

con_i = mysql.connector.connect(host = "localhost", user = "test", password = "123")

myc_i = con_i.cursor()

myc_i.execute("CREATE DATABASE python_db")

con = mysql.connector.connect(host = "localhost", user = "test", password = "123", database = "python_db")

myc = con.cursor()

myc.execute("CREATE TABLE Hospital (Hospital_Id INT, Hospital_Name VARCHAR(20), Bed_Count INT)")

myc.execute("ALTER TABLE Hospital ADD PRIMARY KEY(Hospital_Id)")

qry1 = "INSERT INTO Hospital VALUES(%s, %s, %s)"
val1 =  [
	 (1, "Mayo Clinic", 200),
	 (2, "Cleveland Clinic", 400),
	 (3, "Johns Hopkins", 1000),
	 (4, "UCLA Medical Center", 1500)
	]

myc.executemany(qry1, val1)
con.commit()

myc.execute("CREATE TABLE Doctor (Doctor_Id INT, Doctor_Name VARCHAR(40), Hospital_Id INT, Joining_Date DATE, Speciality VARCHAR(20), Salary INT, Experience INT)")

myc.execute("ALTER TABLE Doctor ADD PRIMARY KEY(Doctor_Id)")

qry2 = "INSERT INTO Doctor VALUES (%s, %s, %s, %s, %s, %s, %s)"
val2 =  [
	 (101, "David", 1, "2005-02-10", "Pediatric", 40000, None),
	 (102, "Michael", 1, "2018-07-23", "Oncologist", 20000, None),
	 (103, "Susan", 2, "2016-05-19", "Gynecologist", 25000, None),
	 (104, "Robert", 2, "2017-12-28", "Pediatric", 28000, None),
	 (105, "Linda", 3, "2004-06-04", "Gynecologist", 42000, None),
	 (106, "William", 3, "2014-09-11", "Dermatologist", 30000, None),
	 (107, "Richard", 4, "2014-08-21", "Gynecologist", 32000, None),
	 (108, "Karen", 4, "2011-10-17", "Radiologist", 30000, None)
	]

myc.executemany(qry2, val2)
con.commit()