"""

Exercise 8: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]

Expected output:

50
40
30
20
10
"""


def reverse_numbers(numbers):
    return numbers[::-1]


def reverse_numbers2(numbers):
    reverse = []
    for i in range(len(numbers), 0, -1):
        reverse.append(numbers[i - 1])
    return reverse


print(reverse_numbers(numbers=[10, 20, 30, 40, 50]))
print(reverse_numbers2(numbers=[10, 20, 30, 40, 50]))
