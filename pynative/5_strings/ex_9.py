import re


"""
Exercise 9: Given a string,
return the sum and average of the digits that appear in the string
, ignoring all other characters
Given:

str1 = "English = 78 Science = 83 Math = 68 History = 65"
Expected Outcome:

sum is 294
average is 73.5
gw: https://stg-identity.sehhaty.com7
"""


def find_numbers(text) -> list:
    return [int(num) for num in re.findall(r'\b\d+\b', text)]


numbers = find_numbers("English = 78 Science = 83 Math = 68 History = 65")

total = sum(numbers)
print(total)

print(total / len(numbers))

