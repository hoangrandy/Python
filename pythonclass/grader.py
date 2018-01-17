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

# Prompts the user to input their grades
grade_input = True
grades = []
# A loop that asks the user to input their grades until they type end
while grade_input:
    user_input = input('Enter your grade here, then click return, '
                       'type "end" to finish: ')
# If the user types end, this will change grade_input to false thus breaking
    if user_input == 'end':
        grade_input = False
# If the user types a number, change it to a float
    else:
        final_grade = float(user_input)
        grades.append(final_grade)

total_grade = sum(grades)
number_grade = len(grades)
average_total = total_grade / number_grade
print(average_total)






