"""
Exercise 11: Write a code to extract each digit from an integer, in the reverse order
If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

"""


def reverse_int(number: int) -> str:
    to_str = str(number)[::-1]
    result = ""
    for digit in to_str:
        if digit == to_str[0]:  # skip space for first item
            result += digit
            continue
        result = result + " " + digit
    return result


# better sol
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10

    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")


print(reverse_int(7536))
