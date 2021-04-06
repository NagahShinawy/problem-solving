"""
Exercise 6: Given two strings, s1 and s2,
create a mixed String using the following rules
Note: create a third-string made of the first char of s1
then the last char of s2, Next, the second char of s1
and second last char of s2, and so on.
Any leftover chars go at the end of the result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output:

AzbycX

"""


def mixed_strings(string1: str, string2: str) -> str:
    diff = abs(len(string1) - len(string2))
    mixed = ""
    if len(string1) <= len(string2):

        length = len(string1)
        rest = string2[:-diff][::-1]
    else:
        length = len(string2)
        rest = ""

    for i in range(length):
        mixed += string1[i] + string2[(i + 1) * -1]

    return mixed + rest


def mixString(s1, s2):
    s2 = s2[::-1]
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    length = lengthS1 if lengthS1 > lengthS2 else lengthS2
    resultString = ""
    for i in range(length):
        if i < lengthS1:
            resultString = resultString + s1[i]
        if i < lengthS2:
            resultString = resultString + s2[i]

    print(resultString)


s1 = "Abc"
s2 = "Xyz"
mixString(s1, s2)


print(mixed_strings("Xyz", "Abc"))
