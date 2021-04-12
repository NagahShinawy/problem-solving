"""
Remove all duplicates from a given string in Python
Difficulty Level : Easy
Last Updated : 22 Nov, 2020
We are given a string and we need to remove all duplicates from it? What will be the output if the order of character matters?
Examples:

Input : geeksforgeeks
Output : efgkos
"""


def remove_duplicates(text: str) -> str:
    res = ""
    for char in text:
        if char not in res:
            res += char

    return res


def remove_duplicates2(text: str) -> str:
    return "".join(set(text))


print(remove_duplicates("geeksforgeeks"))
print(remove_duplicates2("geeksforgeeks"))
