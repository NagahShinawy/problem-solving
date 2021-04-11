"""


"""


def find_odds(numbers):
    # using list comp
    return [num for num in numbers if num % 2 != 0]


def find_odds2(numbers):
    # using filter
    return list(filter(lambda num: num % 2 != 0, numbers))


print(find_odds([2, 7, 5, 64, 14]))
print(find_odds2([2, 7, 5, 64, 14]))