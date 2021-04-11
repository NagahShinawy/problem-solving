"""
Given a list, print the value obtained after multiplying all numbers in a list.
Examples:


Input :  list1 = [1, 2, 3]
Output : 6
Explanation: 1*2*3=6

Input : list1 = [3, 2, 4]
Output : 24
"""
import math
from functools import reduce


def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res


print(multiply([1, 2, 3]))

res = reduce(lambda x, y: x * y, [1, 2, 3])
print(res)

print(math.prod([1, 2, 3]))  # python >= 3.8
