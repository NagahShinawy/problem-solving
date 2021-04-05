"""
Exercise 2: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
Given:

s1 = "Ault"
s2 = "Kelly"
Expected Output:

AuKellylt
"""


def inject_in_middle(original, append):
    index = len(original) // 2
    result = original[:index] + append + original[-index:]
    return result


print(inject_in_middle(original="Ault", append="Kelly"))
print(inject_in_middle(original="AultX", append="Kelly"))
print(inject_in_middle(original="AultXX", append="Kelly"))
