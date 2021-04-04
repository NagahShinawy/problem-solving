"""
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Expected Output:


[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
"""


def evens(start: int, end: int) -> list:
    return [num for num in range(start, end + 1) if num % 2 == 0]


def evens_or_odds(start: int, end: int, is_eves: bool) -> list:
    if not is_eves:
        start += 1
    return [num for num in range(start, end + 1, 2)]


print(evens(4, 30))
print(evens_or_odds(4, 30, True))
print(evens_or_odds(4, 30, False))
