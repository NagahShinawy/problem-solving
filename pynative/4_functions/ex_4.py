"""
Exercise 4: Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both.
If the salary is missing in the function call assign default value 9000 to salary
Given:

showEmployee("Ben", 9000)
showEmployee("Ben")
Expected output:

Employee Ben salary is: 9000
Employee Ben salary is: 9000
"""


def show_employee(name, salary=9000):
    print(f"Employee <{name}> salary is: <{salary}>")


show_employee("Ben", 8000)
show_employee("Ben")
