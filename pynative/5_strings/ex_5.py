"""
Exercise 5: Count all lower case, upper case, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits,and symbols

Chars = 8
Digits = 3
Symbol = 4
"""


def count_chars(string: str):
    letters = 0
    digits = 0
    symbols = 0
    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return {"letters": letters, "digits": digits, "symbols": symbols}


print(count_chars("P@#yn26at^&i5ve"))
