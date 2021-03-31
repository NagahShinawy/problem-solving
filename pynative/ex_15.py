"""
Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Expected output

Case 1:

base = 2
exponent = 5
2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
Case 2:

base = 5
exponent = 4
5 raises to the power of 4 is: 625
i.e. (5 *5 * 5 *5 = 625)
"""


def exponent(base: int, exp: int):
    return base ** exp


def exponent2(base, exp):
    return pow(base, exp)


def exponent3(base, exp):
    total = 1
    for _ in range(exp):
        total *= base

    return total


def exponent4(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)


print(exponent(3, 3))
print(exponent2(3, 3))
print(exponent3(3, 3))
exponent4(3, 3)
nums = range(0, 60)

# simple code of packing
print(*[num for num in nums if num % 5 == 0], sep="\n")
