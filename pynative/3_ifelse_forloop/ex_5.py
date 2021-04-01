"""
Exercise 5: Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
Expected output:

15
55
75
150
"""
numbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
divisible_by_five = []
for num in numbers:
    if num > 150:
        break
    if num % 5 == 0:
        divisible_by_five.append(num)

print(divisible_by_five)
