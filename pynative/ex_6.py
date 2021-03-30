"""
Exercise 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
"""


def divisible_by_5(collection: list):
    return [num for num in collection if num % 5 == 0]


# website sol
def find_divisible(numberslist):
    print("Given list is ", numberslist)
    print("Divisible of 5 in a list")
    for num in numberslist:
        if num % 5 == 0:
            print(num)


numlist = [10, 20, 33, 46, 55]
find_divisible(numlist)

print(divisible_by_5([4, 5, 7, 10, 80]))
