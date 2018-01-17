# -----------------------------------------------------------------------------
# Name:        Making Decisions
# Purpose:     Using If and elif to make a text game
#
# Author: Randy Hoang
# Date: 1/08/18
# -----------------------------------------------------------------------------
# Print out the initial question that starts the game
print "You enter a dark room with two doors. Do you go through door 1 or door 2"
# Asks the user which door do they choose to answer
door = raw_input("> ")
# If the user enters through door 1, proceed to print
if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
# Asks the user to choose between taking the cake or screaming at the bear
    bear = raw_input("> ")
# If the user enters the number 1, print
    if bear == "1":
        print "The bear eats your face off. Good job!"
# If the user enters number 2, print. Note: elif must be  elif and not else if
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
# If the user enters anything but a 1 or 2.  Print out this else statement
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

#If the they choose to go through door 2, print
elif door == "2":
    print "You stare into the endless abyss at Cthuhlu's retina."
    print "1. Blue berries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

# If the user enters 1 or 2 print this out
    insanity = raw_input("> ")
# THIS
    if insanity == "1" or insanity =="2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
#If the user did not enter a door number to walk through print this out (else)
else:
    print "You stumble around and fall on a knife and die. Good job!"
