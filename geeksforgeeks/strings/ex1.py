"""
Given a string. the task is to check if the string is symmetrical and palindrome or not. A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears same when read forward or backward.

Example:

Input: khokho
Output:
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
"""


def palindrome(text):
    return text == text[::-1]


def symmetrical(text):
    if len(text) % 2 != 0:
        return False
    mid = len(text) // 2
    return text[:mid] == text[mid:]


if palindrome("amaama"):
    print("palindrome")


if symmetrical("khokho"):
    print("symmetrical")