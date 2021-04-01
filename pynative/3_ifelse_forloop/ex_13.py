"""
Exercise 13: Write a loop to find the factorial of any number
The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
"""


def calc_factorial(number):
    if number < 0:
        print("Factorial does not exits for neg numbers")
    elif number == 0:
        print("Factorial of 0 is 1")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"Factorial of <{number}> is <{factorial}>")


calc_factorial(5)
calc_factorial(0)
calc_factorial(1)
