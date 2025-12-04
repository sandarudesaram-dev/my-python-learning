# Exercise 9: Modify Nested Dictionary #

'''
In the below dictionary, change name to ‘Jessa’.

Given:

nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
'''
print()

nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print("nested_student_dict:", nested_student_dict)
nested_student_dict['class']['student']['name'] = "Jessa"
print("nested_student_dict['class']['student']['name']='Jessa' >>", nested_student_dict)