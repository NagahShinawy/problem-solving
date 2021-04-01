"""
Exercise 8: Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def make_pyramids_number(n):
    for number in range(1, n + 1):
        for j in range(1, number + 1):
            print(number, end=" ")
        print()


make_pyramids_number(n=5)

# website sol
for num in range(10):
    for i in range(num):
        print(num, end=" ")  # print number
    # new line after each row to display pattern correctly
    print("\n")
