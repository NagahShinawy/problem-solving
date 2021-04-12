"""
Given the string, the task is to capitalise the first and last character of each word in a string.

Examples:

Input: hello world
Output: HellO WorlD

Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS
"""


def first_last_as_upper(text: str) -> str:
    if len(text) == 1:
        return text[0].upper()
    if len(text) > 1:
        return text[0].upper() + text[1:-1] + text[-1].upper()
    return ""


print(first_last_as_upper("john"))
print(first_last_as_upper("test"))
print(first_last_as_upper(""))
print(first_last_as_upper("a"))
print(first_last_as_upper("ab"))
