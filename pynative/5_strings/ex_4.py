from string import ascii_lowercase

"""
Exercise 4: Arrange string characters such that lowercase letters should come first
Given an input string with the combination of the lower and upper case arrange characters in such a way that
all lowercase letters should come first.

Given:

str1 = PyNaTive
Expected Output:

yaivePNT
"""


def rearrange_letters(string: str):
    lowers = ""
    uppers = ""
    for letter in string:
        if letter.islower():
            lowers += letter
        else:
            uppers += letter

    return lowers + uppers


def rearrange_letters2(string: str):
    lowers = ""
    uppers = ""
    for letter in string:
        if letter in ascii_lowercase:
            lowers += letter
        else:
            uppers += letter
    return lowers + uppers


assert rearrange_letters("PyNaTive") == "yaivePNT"
assert rearrange_letters2("PyNaTive") == "yaivePNT"
