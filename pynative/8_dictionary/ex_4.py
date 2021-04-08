

"""
Exercise 4: Initialize 8_dictionary with default values
Given:

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
Output:
{
    Kelly: {"designation": 'Application Developer', "salary": 8000}
    Emma: {"designation": 'Application Developer', "salary": 8000}
    John: {"designation": 'Application Developer', "salary": 8000}
}
"""
import json


def init_dic(keys: list, values: dict, indent=0):
    return json.dumps(dict.fromkeys(keys, values), indent=indent)


employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
print(init_dic(employees, defaults))