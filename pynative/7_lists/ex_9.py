
"""
Exercise 9: Given a Python list, find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of a value
Given

list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:

list1 = [5, 10, 15, 200, 25, 50, 20]
"""


def find_and_replace(numbers: list, number):
    if number in numbers:
        index = numbers.index(number)
        numbers[index] = 200
        return numbers
    return numbers


print(find_and_replace([5, 10, 15, 20, 25, 50, 20], 20))

