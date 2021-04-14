"""
Python | Frequency of numbers in String

"""
import re


def count_numbers(text: str) -> int:
    numbers = re.findall(r"\d+", text)
    return len(numbers)


print(count_numbers("geeks4feeks is No. 1 4 geeks"))
print(count_numbers("geeks4feeks is No. 19 46 geeks"))
print(count_numbers("geeks45feeks"))
