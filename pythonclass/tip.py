# ---------------------------------------------------------------------------
# Name:       tip
# Purpose:    tip calculator
#
# Author:     Randy Hoang
# Date:       1/08/2018
#-----------------------------------------------------------------------------
"""
Tip calculator assuming a 20% tip rate

Prompt the user for the cost of their meal.
Print the tip amount and the total cost
"""

TIP_RATE = 20 / 100                 # The tip rate constant

user_input = input('Please enter the cost of the meal in $: ')
cost = float(user_input)            # Convert the input string to a number

tip_amount = TIP_RATE * cost        # Calculates the tip amount
total_amount = tip_amount + cost    # The total cost of the meal

tip = f'${tip_amount:.2f}'  # Formatted string for tip prefixed with the $ sign
total = f'${total_amount:.2f}'    # Formatted string for total prefixed with $

tip_output = f'Tip Amount:{tip:>8}'      #Tip output string - right aligned
total_output = f'Total Cost:{total:>8}'  #Total output string - right aligned

print(tip_output)
print(total_output)