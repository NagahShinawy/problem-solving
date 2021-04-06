from typing import Union

"""
Exercise 11: Reverse a given string
Given:

str1 = "PYnative"
Expected Output:

evitanYP
"""


def reverse(items: Union[list, str, tuple]):
    return items[::-1]


def reverse2(items: str) -> str:
    return "".join(reversed(items))


print(reverse([3, 5, 6]))
print(reverse("test"))


print(reverse2("test"))