"""
Exercise 1: Create a function that can accept two arguments name and age and print its value
"""


def info(name, age):
    print(f"Name is <{name}> with age <{age}>")


def info2(**kwargs):
    name = kwargs.get("name")
    age = kwargs.get("age")
    if name is not None and age is not None:
        print(f"Name is <{name}> with age <{age}>")
    else:
        print("Missing name or age")


info("John", 33)
info2(name="test", age=22)
