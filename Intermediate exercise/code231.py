# Exercise 10: Access the nested key increment from the following dictionary #

'''
Given:

emp_dict = {
	"company": {
		"employee": {
			"name": "Jess",
			"payable": {
				"salary": 9000,
				"increment": 12
			}
		}
	}
}
'''
print()

emp_dict = {
	"company": {
		"employee": {
			"name": "Jess",
			"payable": {
				"salary": 9000,
				"increment": 12
			}
		}
	}
}

print(f"emp_dict: {emp_dict}")
print()

accessed = emp_dict["company"]["employee"]["payable"]["increment"]
print(accessed)