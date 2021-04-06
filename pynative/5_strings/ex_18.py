"""
Exercise 18: Replace each punctuation with # in the following string
Given:

str1 = '/*Jon is @developer & musician!!'
Expected Output:

##Jon is #developer # musician##
"""
from string import ascii_letters

ACCEPTED = ascii_letters + " "


def replace_with_hash(text):
    result = ""
    for char in text:
        if char in ACCEPTED:
            result += char
        else:
            result += "#"
    return result


print(replace_with_hash("/*Jon is @developer & musician!!"))

assert "##Jon is #developer # musician##" == replace_with_hash("/*Jon is @developer & musician!!")