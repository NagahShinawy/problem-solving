"""
Given a string in Python. The task is to check whether the string has at least one letter(character) and one number.
Return “True” if the given string full fill above condition else return “False” (without quotes).
Examples:

Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False
"""


def is_anumber_aletter_exist(text: str) -> bool:
    number_flag = False
    letter_flag = False

    for char in text:
        if char.isdigit():
            number_flag = True

        if char.isalpha():
            letter_flag = True

    return number_flag and letter_flag
