"""
Exercise 7: Assign a different name to function and call it through the new name
Below is the function displayStudent(name, age). Assign a new name showStudent(name, age) to it and call through the new nam
"""


def display_student(name, age):
    print("Name is {} with age {}".format(name, age))


show_student = display_student

show_student("John", 30)
