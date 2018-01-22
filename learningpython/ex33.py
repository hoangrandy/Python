# -----------------------------------------------------------------------------
# Name:        While loops
# Purpose:     Practicing while loops
#
# Author: Randy Hoang
# Date: 1/21/2018
# -----------------------------------------------------------------------------
i = 0 # set i = 0

numbers = [] # Create an empty set under the variable numbers
while i < 6: # This run when i is less than 6, starting from 0
    print "At the top i is %d" % i # Print this if i is less than 6
    numbers.append(i) # Input the number into the set "numbers"

    i = i + 1 # Everytimes this runs add 1 to i
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers: # For all the numbers in the set, print them out
    print num
