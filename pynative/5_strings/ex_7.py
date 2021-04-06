"""
Exercise 7: String characters balance Test
We’ll assume that a String s1 and s2 is balanced
if all the chars in the s1 are there in s2.
characters’ position doesn’t matter.

Given:

Case 1:

s1 = "Yn"
s2 = "PYnative"
Expected Output:

True
Case 2:

s1 = "Ynf"
s2 = "PYnative"
Expected Output:

False


s1 = "PYnative"
s2 = "Ynf"
"""


def swap(string1, string2):
    if len(string1) <= len(string2):
        first = string1
        second = string2
    else:
        first = string2
        second = string1
    return first, second


def count_matches(string1: str, string2: str):
    first, second = swap(string1, string2)
    is_match: bool = True
    counts = 0
    for char in first:
        if char not in second:
            is_match = False
            break
        else:
            counts += second.count(char)

    if is_match:
        return {"match": is_match, "counts": counts}
    return is_match


def stringBalanceCheck(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)


print(count_matches("Yn", "PYnative"))
print(count_matches("Ynf", "PYnative"))
print(count_matches("PYnative", "Yn"))
