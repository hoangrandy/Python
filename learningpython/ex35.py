# -----------------------------------------------------------------------------
# Name:        Two doors game
# Purpose:     Practicing with branches and functions
#
# Author:      Randy Hoang
# Date:        1/23/2018
# -----------------------------------------------------------------------------
from sys import exit # This import the exit function which quits the program

def gold_room(): # Create the room gold room within gold_room() function
    print "This room is full of  gold. How much do you take"

    next = raw_input("> ") # Asks user for the amount of gold they would want
    how_much = int(next) # Makes the input an integer
    if how_much < 49:
        print "You grabbed", how_much, "gold pieces"
    else: # If user doesn't type in a valid command they die
        dead("Man, learn to type a number.")

    if how_much < 50: # User wins if they choose a number under 50
        print "Nice, you're not greedy, you win"
        exit(0) # Added an exit function to exit the game

    else: # If user types anything else, they die
        dead("You greedy bastard!")

def bear_room(): # Creates the function bear room
    print "There is a bear here"
    print "The bear has a bunch of honey"
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then pimp slaps your face off.")
        elif next == "taunt bear" and not bear_moved: # If user taunts bear
        # will move
            print "The bear has moved from the door. You can go through now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved: # taunt bear again, die
            dead("The bear gets pissed off and chews your crotch off.")
        elif next == "open door" and bear_moved: #only works if bear moved
            gold_room()
        else:
            print " I got no idea what that means."

def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start() #this brings you back to the first room
    elif "head" in next: # If the user typed anything with head they die
        dead("Well that was tasty!")
    else: cthulu_room()

def dead(why):
    print why, "Good Job!" # This function makes the user dies string + goodjob
    exit(0) # Exits program

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
