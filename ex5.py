my_name = "Randy Hoang"
my_age = 24
#My height in foot and inches
my_height = "5 feet 8 inches"
#My weight in lbs
my_weight = 200
my_eyes = "Brown"
#Hopefully my teeth are white
my_teeth = "White"
my_hair = "Brown"

#Let's print out who we are talking about using a variable using %s meaning string
# using %s as a string and inputing which variable after % after the quotes
print "Let's talk about %s." % my_name

#print out how tall Randy is in feet and inches
print "He's %s tall." % my_height

#print out my weight using %d since it is a number and not a string
print "He's %d pounds heavy." % my_weight

#Let's print out a lie
print "Actually that's not too heavy."

#print out the color of his eyes and hair
print "He has %s eyes and %s hair" % (my_eyes, my_hair)

#print out the color of his teeth
print "He has %s teeth" % my_teeth

#adding values that doesn't make sense together, but doing for the sake of practice
print "If I add %d, %d, I get %d" % (my_age, my_weight, my_age + my_weight)
