"""
Exercise 12: Find the last position of a substring “Emma” in a given string
Given:


str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:

Last occurrence of Emma starts at index 43
"""


def find_last_occurrence(text: str, subtext: str) -> int:
    return text.rfind(subtext)


print(find_last_occurrence("Emma is a data scientist who knows Python. Emma works at google.", "Emma"))