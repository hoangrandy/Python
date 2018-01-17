# -----------------------------------------------------------------------------
# Name:     Grader
# Purpose:  This program will calculate the user's final grade in class based
#           on the average of the user's inputs
#
# Author:   Randy Hoang
# Date:     1/16/18
# -----------------------------------------------------------------------------
"""
Calculating the final grade in class

This program will calculate the user's final grade by finding the average
of all the user's grades and print it
"""


grade_input = True # Prompts the user to input their grades
grades = [] # Creates an empty table that holds the grades
# A loop that asks the user to input their grades until they type end
while grade_input:
    user_input = input('Enter your grade here, then click return, '
                       'type "end" to finish: ')
# If the user types end, this will change grade_input to false thus breaking
    if user_input == 'end':
        grade_input = False
    else: # If the user types a number, change it to a float
        final_grade = float(user_input)
        grades.append(final_grade) # Insert the input into the string


total_grade = sum(grades) # Take the grades list and add the values
number_grade = len(grades) # Takes the number of inputs and store them here
average_total = total_grade / number_grade # Total / number of inputs
print('Course Average: ',average_total)

if average_total < 60 and average_total > 0:
    print('Letter Grade: F')
elif average_total >= 60 and average_total < 70:
    print('Letter Grade: D')
elif average_total >= 70 and average_total < 80:
    print('Letter Grade: C')
elif average_total >= 80 and average_total < 90:
    print('Letter Grade: B')
else:
    print ('Letter Grade: A')






