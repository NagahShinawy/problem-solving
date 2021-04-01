""""
Exercise 12: Display Fibonacci series up to 10 terms
Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34
"""

limit = 10
start, end = 0, 1
for _ in range(limit):
    print(start, end="  ")
    temp = start + end
    # update values
    start = end
    end = temp
