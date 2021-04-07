"""
Exercise 1: Given two lists create a third list by picking an odd-index element from the first list and even index elements from the second.

Given:

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""

from typing import Union


def mixed_items(collection1: Union[list, tuple, str], collection2: Union[list, tuple, str]):
    evens = [item for item in collection1[1::2]]
    odds = [item for item in collection2[::2]]
    return evens + odds


coll1 = [3, 6, 9, 12, 15, 18, 21]
coll2 = [4, 8, 12, 16, 20, 24, 28]
print(mixed_items(collection1=coll1, collection2=coll2))