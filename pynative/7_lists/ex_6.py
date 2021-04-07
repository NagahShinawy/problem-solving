"""
Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:

["Mike", "Emma", "Kelly", "Brad"]
"""


def remove_empty_string(strings):
    return [string for string in strings if string]


def remove_empty(strings):
    # just like above method , it checks item if True or False
    return list(filter(None, strings))


print(remove_empty_string(["Mike", "", "Emma", "Kelly", "", "Brad"]))
print(remove_empty(["Mike", "", "Emma", "Kelly", "", "Brad"]))