# -----------------------------------------------------------------------------
# Name:        Exercise 33 extra credit
# Purpose:     Making the exercise with a forloop
#
# Author: Randy Hoang
# Date:   1/21/2018
# -----------------------------------------------------------------------------

i = 0  # set variable i to 0
numbers = [] #create an empty set

for i in range(6): # For loop
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
