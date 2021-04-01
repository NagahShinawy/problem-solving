""""
Exercise 15: Use a loop to display elements from a given list that are present at even index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected output:

20 40 60 80 100
"""

for number in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100][0::2]:
    print(number, end=" ")
