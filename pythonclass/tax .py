# -----------------------------------------------------------------------------
# Name:        tax
# Purpose: To implement a simple sales tax calculator
#
# Author: Randy Hoang
# Date: 1/09/2018
# -----------------------------------------------------------------------------
"""
Sales tax calculator.

This program asks the user for the prices of 3 items, then would compute the
subtotal and sales tax then prints out the total.
"""
# Los Altos Hills tax of 9%
TAX = 9/100

# Prompts the user to enter the amount of the first item in $
item_one = input('Please type in the price of the first item in $: ')
# Prompts the user to enter the amount of the second item in $
item_two = input('Please type in the price of the second item in $: ')
# Prompts the user to enter the amount of the third item in $
item_three = input('Please type in the price of the third item in $: ')

# Create a variable that adds the prices of three items together as well as
# converts the input to floats
subtotal_cost = round(float(item_one),2) + round(float(item_two),2) \
                + round(float(item_three),2)

# Let's print out the subtotal
print('SUBTOTAL: ${}'.format(subtotal_cost))

sales_tax = subtotal_cost * TAX
print('SALES TAX: ${}'.format(sales_tax))

total = (subtotal_cost + sales_tax)
print('TOTAL: ${}'.format(total)) 

