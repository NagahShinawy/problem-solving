"""
Exercise 16: Display the cube of the number up to a given integer
Given:

input_number = 6

Expected output:

Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216
"""
limit = 6

for i in range(1, limit + 1):
    print(f"Current Number is : {i}  and the cube is {i ** 3}")
