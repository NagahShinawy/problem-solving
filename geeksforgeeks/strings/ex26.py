"""
The problem is quite simple. Given a string, we need to replace all commas with dots and all dots with the commas. This can be achieved in two popular ways.
Examples:

Input : 14, 625, 498.002
Output : 14.625.498, 002
"""


# Python code to replace, with . and vice-versa
def replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")


def replace2(str1):
    str1 = str1.replace(', ', '-')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('-', '.')
    return str1


string = "14, 625, 498.002"
print(replace(string))

# Driving Code
string = "14, 625, 498.002"
print(replace2(string))
