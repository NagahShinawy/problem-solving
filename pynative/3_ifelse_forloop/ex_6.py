"""
Exercise 6: Given a number count the total number of digits in a number
For example, the number is 75869, so the output should be 5.
"""


def digits_len(number):
    return len(str(number))


def digits_len2(number):
    count = 0
    while number != 0:
        number = number // 10
        count += 1
    return count


print(digits_len(75869))
print(digits_len2(75869))
