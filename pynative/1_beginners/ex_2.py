""""
Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number,
and In each iteration print the sum of the current number and previous number

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17


"""


def sum_of_2_numbers_1(limit: int):
    total = 0
    for i in range(limit):
        total += 2
        if i == 0:
            total = 0
        if i == 1:
            total = 1

        print(i, total)


def sum_of_2_numbers_2(limit: int):
    start = 0
    end = 0
    for i in range(limit):
        total = start + end
        start = i
        end = start + 1
        print(i, total)


# website solution
def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum, " Sum: ", sum)
        previousNum = i


# website solution
print("Printing current and previous number sum in a given range(10)")
# sumNum(10)

# sum_of_2_numbers_1(20)
sum_of_2_numbers_2(10)
