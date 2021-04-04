"""
Exercise 9: Return the largest item from the given list
aList = [4, 6, 8, 24, 12, 2]
Expected Output:

24
"""
from typing import Union


def find_max(numbers: list) -> Union[int, float]:
    return max(numbers)


def find_max_number(numbers: list) -> Union[int, float]:
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(find_max_number([4, 6, 8, 24, 12, 2]))
print(find_max([4, 6, 8, 24, 12, 2]))
print(max(([4, 6, 8, 24, 12, 2])))
