"""
Exercise 10: Change Brad’s salary to 8500 from a given Python 8_dictionary
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
Expected output:

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 8500}
}
"""
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 8500}
}


def update_salary(employee_name, salary):
    for emp in sampleDict.values():
        if emp.get("name") == employee_name:
            emp["salary"] = salary
    return sampleDict


print(update_salary("Brad", 90000))