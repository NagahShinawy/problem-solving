"""
Exercise 1: Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
Given:

Case 1

str1 = "JDipa"
        JhonDipPeta
Output

Dip
"""
from math import ceil


def is_even(number):
    return True if number % 2 == 0 else False


def middle(string: str):
    division = len(string) // 3
    if len(string) > 9:
        index = division + 1
    else:
        index = division
    return string[index:-index]


print(middle("JhonDipPeta"))
print(middle("Jhon2DipPeta2"))
print(middle("JDipa"))
print(middle("666666Dip666666"))


def getMiddleThreeChars(sampleStr):
    middleIndex = int(len(sampleStr) / 2)
    print("Original String is", sampleStr)
    # keep difference is 3 ex 1:4
    middleThree = sampleStr[middleIndex - 1 : middleIndex + 2]
    print("Middle three chars are", middleThree)


# getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("JDipa")
