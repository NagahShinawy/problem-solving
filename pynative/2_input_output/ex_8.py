"""
Exercise 8: Format the following data using a string.format() method.
Given:

totalMoney = 1000
quantity = 3
price = 450
Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars.
"""
totalmoney = 1000
quantity = 3
price = 450

# {'%.2f' % (price / 1)} = 450.00. means 2 digits after decimal
print(f"I have {totalmoney} dollars so I can buy {quantity} for {'%.2f' % (price / 1)}")

# another solution
quantity = 3
totalMoney = 1000
price = 450

# {2:.2f} ==> first2 means index of 'price' using format function
# second2 ==> means 2  digits after point
statement1 = "I have {1} dollars so I can buy {0} football for {0:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))
