"""
Exercise 3: Accept number from user and calculate the sum of all number from 1 to a given number
For example, if user entered 10 the output should be 55
"""

number: int = int(input("Enter Number"))

total = 0
for i in range(number + 1):
    total += i

print(total)


def calc_sum(num):
    return sum(range(num + 1))


print(calc_sum(number))
