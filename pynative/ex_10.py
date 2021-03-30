"""
Exercise 10: Given a two list of numbers
create a new list such that new list should contain only
odd numbers from the first list and even numbers from the second list
Expected Output:

list1 =  [10, 20, 23, 11, 17]
list 2 = [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]
"""


def combine_odd_even(list1, list2):
    odds = list(filter(lambda num: num % 2 != 0, list1))
    evens = list(filter(lambda num: num % 2 == 0, list2))
    odds.extend(evens)
    return odds


def combine_odd_even_2(list1: list, list2: list):
    odds = [num for num in list1 if num % 2 != 0]
    evens = [num for num in list2 if num % 2 == 0]
    return odds + evens


numbers = combine_odd_even([10, 20, 23, 11, 17], [13, 43, 24, 36, 12])
print(numbers)
assert numbers == [23, 11, 17, 24, 36, 12]


numbers = combine_odd_even_2([10, 20, 23, 11, 17], [13, 43, 24, 36, 12])
print(numbers)
assert numbers == [23, 11, 17, 24, 36, 12]


# website sol
def mergeList(listOne, listTwo):
    print("First List ", listOne)
    print("Second List ", listTwo)
    thirdList = []

    for num in listOne:
        if num % 2 != 0:
            thirdList.append(num)
    for num in listTwo:
        if num % 2 == 0:
            thirdList.append(num)
    return thirdList


listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print("result List is", mergeList(listOne, listTwo))
