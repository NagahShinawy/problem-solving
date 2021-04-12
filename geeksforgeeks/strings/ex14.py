"""
Python | Maximum frequency character in String
Output :
The original string is : GeeksforGeeks
The maximum of all characters in GeeksforGeeks is : e
"""
from collections import Counter


def max_freq(text: str) -> int:
    chars = Counter(text)
    return sorted(chars, key=chars.get)[-1]


print(max_freq("GeeksforGeeks"))


class Number:

    def __init__(self, num):
        self.num = num

    def __gt__(self, other):
        if isinstance(other, Number):
            return self.num > other.num
        return self.num > other


x = Number(10)
y = Number(6)

print(x > 8)
print(x > 8.65)
print(x > 80.65)
print(x > y)