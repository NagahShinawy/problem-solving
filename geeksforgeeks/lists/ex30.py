"""
iven a list of integers with duplicate elements in it. The task to generate another list, which contains only the duplicate elements. In simple words, the new list should contain the elements which appear more than one.

Examples :

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]


Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
"""


def find_repeated(numbers: list):
    repeated = []
    for num in numbers:
        if num not in repeated and numbers.count(num) > 1:
            repeated.append(num)
    return repeated


print(find_repeated([-1, 1, -1, 8]))
print(find_repeated([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))