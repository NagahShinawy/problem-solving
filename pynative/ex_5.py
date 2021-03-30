""""
Exercise 5: Given a list of numbers, return True if first and last number of a list is same
"""
from typing import Union


# Union means group of data types
def is_eq_first_and_last(collection: Union[str, list, tuple]):
    if collection:
        return collection[0] == collection[-1]
    return False


print(is_eq_first_and_last((3, 5, 3)))
print(is_eq_first_and_last([3, 5, 3]))
print(is_eq_first_and_last("353"))
print(is_eq_first_and_last(True))  # invalid params
print(is_eq_first_and_last(0))  # invalid params

# website sol is the same
