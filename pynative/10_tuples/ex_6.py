"""
Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:

tuple2: (44, 55)
"""


def find_elements(items, *args):
    return tuple(element for element in args if element in items)


print(find_elements((11, 22, 33, 44, 55, 66), 44, 55))