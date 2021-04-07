

"""
Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:


[5, 15, 25, 50]
"""


def remove_occurrence(items, item):
    return list(filter(lambda x: x != item, items))


def remove_occurrence2(items, item):
    return [value for value in items if value != item]


def remove_occurrence3(items, item):
    items[:] = [value for value in items if value != item]
    return items


def remove_occurrence4(items, item):
    # using generator expression
    items[:] = (value for value in items if value != item)
    return items


print(remove_occurrence([5, 20, 15, 20, 25, 50, 20], 20))
print(remove_occurrence2([5, 20, 15, 20, 25, 50, 20], 20))
print(remove_occurrence3([5, 20, 15, 20, 25, 50, 20], 20))
print(remove_occurrence4([5, 20, 15, 20, 25, 50, 20], 20))