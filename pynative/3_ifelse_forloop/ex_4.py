"""
Exercise 4: Print multiplication table of a given number

For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20
"""


def multiplication_table(number, end):
    for i in range(1, end + 1):
        print(number * i)


multiplication_table(3, 10)
