""""
Exercise 9: Reverse a given number and return true if it is the same as the original number
Expected Output:

original number 121
The original and reverse number is the same

original number 125
The original and reverse number is not same
"""
from typing import Union


def reverse_number(number: Union[int, str]) -> bool:
    number_as_str = str(number)
    new_number = number_as_str[::-1]
    return number_as_str == new_number


# website sol ( not follow PEP)
def reverseCheck(number):
    print("original number", number)
    originalNum = number
    reverseNum = 0
    while number > 0:
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if originalNum == reverseNum:
        return True
    else:
        return False


print("The original and reverse number is the same:", reverseCheck(121))

print(reverse_number("123"))
print(reverse_number("121"))
print(reverse_number(121))
print(reverse_number(123))
