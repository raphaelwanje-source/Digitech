student = {
    "name": "Ali",
    "age": 17,
    "grade": "B",
}

# update the student's grade "A"
student["grade"] = "A"
print(student)


# retrieve value 
print(student.get("age"))

# return student
get = {
    "student": lambda: student
}
print(get["student"]())