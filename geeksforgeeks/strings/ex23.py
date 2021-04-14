"""
Given a string str. The task is to check whether it is a binary string or not.

Examples:

Input: str = "01010101010"
Output: Yes

Input: str = "geeks101"
Output: No
"""


def is_text_binary(text):
    binary = ['0', '1']
    text = sorted(set(text))
    return binary == text


def is_text_binary2(text):
    return all(False for char in text if char not in '01')


print(is_text_binary("01010101010"))
print(is_text_binary2("01010101010"))
print(is_text_binary2("x1010101010"))
print(is_text_binary("x1010101010"))
