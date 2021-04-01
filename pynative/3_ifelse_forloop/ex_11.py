"""
Exercise 11: Write a program to display all prime numbers within a range

Note: A Prime Number is a whole number that cannot be made by multiplying other whole numbers

Examples:

6 is not a Prime Number because it can be made by 2×3 = 6
37 is a Prime Number because no other whole numbers multiply together to make it.
Given:

start = 25
end = 50
Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47
"""

start = 25
end = 50


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return number


for num in range(start, end + 1):
    if is_prime(num):
        print(num)
