# -----------------------------------------------------------------------------
# Name:        If-Statements
# Purpose:     Practicing If statements
#
# Author: Randy Hoang
# Date: 1/16/2018
# -----------------------------------------------------------------------------
# Assigning values to variables people, cats, and dogs
people = 20
cats = 30
dogs = 15

# If the number of people is less than cats then print
if people < cats:
    print "Too many cats! The world is doomed!"
# If the number of people is more than cats then print
if people > cats:
    print "Not many cats! The world is saved!"
# If the number of people is less than dogs then print
if people < dogs:
    print "The world is drooled on!"
# If the number of people is more than dogs then print
if people > dogs:
    print "The world is dry!"

# Add 5 to the number of dogs in the given variable 15 + 5 = 20
dogs += 5
# If the number of people is greater than the new value of dogs then PRINT
if people >= dogs:
    print "People are greater than equal to dogs."
# If the number of people is less than or equal to the new value of dogs, PRINT
if people <= dogs:
    print "People are less than equal to dogs."
# If the number of people is equal to the number of dogs, then PRINT
if people == dogs:
    print "People are dogs."
