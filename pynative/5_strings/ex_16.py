import re
"""
Exercise 16: Removal all the characters other than integers from a string
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510
"""


def keep_numbers(text):
    numbers = re.findall(r'\b\d+\b', text)
    return "".join(numbers)


def keep_numbers2(text: str):
    numbers = ""
    for char in text:
        if char.isdigit():
            numbers += char
    return numbers


str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)

print(keep_numbers('I am 25 years and 10 months old'))
print(keep_numbers2('I am 25 years and 10 months old'))