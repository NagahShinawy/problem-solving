"""
Exercise 1: Print First 10 natural numbers using while loop
Expected output:

0
1
2
3
4
5
6
7
8
9
10
"""


def counter(start: int, end: int):
    if start > end:
        start, end = end, start
    while start <= end:
        print(start)
        start += 1


counter(10, 1)
