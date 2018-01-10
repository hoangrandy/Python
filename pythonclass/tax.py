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
cost_one = float(item_one)

# Prompts the user to enter the amount of the second item in $
item_two = input('Please type in the price of the second item in $: ')
cost_two = float(item_two)

# Prompts the user to enter the amount of the third item in $
item_three = input('Please type in the price of the third item in $: ')
cost_three = float(item_three)


# Calculates the subtotal amount
subtotal_amount = cost_one + cost_two + cost_three

# Calculates the sales tax
salestax_amount = subtotal_amount * TAX

# Calculates the total price
total_amount = (subtotal_amount + salestax_amount)

# Making the output end with two decimal points
subtotal_cost = f'${subtotal_amount:.2f}'
salestax_cost = f'${salestax_amount:.2f}'
total_cost = f'${total_amount:.2f}'

# Making the output align to the right
subtotal_output = f'SUBTOTAL:{subtotal_cost:>8}'
salestax_output = f'SALES TAX:{salestax_cost:>7}'
total_output = f'TOTAL:{total_cost:>11}'

#print out the output
print(subtotal_output)
print(salestax_output)
print(total_output)