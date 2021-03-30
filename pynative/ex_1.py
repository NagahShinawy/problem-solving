""""
Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum
Given 1:

number1 = 20
number2 = 30
Expected Output:

The result is 600
Given 2:

number1 = 40
number2 = 30
Expected Output:

The result is 70
"""


def product_or_sum(num1: int, num2: int):
    """

    :param num1:
    :param num2:
    :return: sum of num1 + num2 if product > 1000 else num1 * num2
    """
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    return product


# website solution
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2


def website_solution():
    # first condition
    result = multiplication_or_sum(20, 30)
    print("The result is", result)

    # Second condition
    result = multiplication_or_sum(40, 30)
    print("The result is", result)


website_solution()
print(product_or_sum(num1=20, num2=50))  # my solution
