"""
Exercise 10: Remove duplicate from a list and create a tuple and find the minimum and maximum number

Given:

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
Expected Outcome:

unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99
"""
from typing import Union


def remove_duplicates(items: Union[list, tuple]) -> list:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


numbers = [87, 45, 41, 65, 94, 41, 99, 94]

unique = remove_duplicates(numbers)

print(unique)

unique = tuple([87, 45, 41, 65, 94, 41, 99, 94])
print(remove_duplicates(unique))
print(max(unique))
print(min(unique))