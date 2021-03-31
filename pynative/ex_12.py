"""
Exercise 12: Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose that the taxable income is $45000 the income tax payable is

$10000*0% + $10000*10%  + $25000*20% = $6000
"""

income = 25000

if income <= 10000:
    income_tax_payable = 0

elif income <= 20000:
    base = income - 10000
    income_tax_payable = base * 10 / 100


else:
    first = 0
    _next = 10000
    remaining = income - 20000
    print(remaining)
    income_tax_payable = (first * 0) + (_next * 10 / 100) + (remaining * 20 / 100)


print("Income Tax Payable", income_tax_payable)
