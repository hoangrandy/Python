
#Defining variables
x = "There are %d types of people" %10
binary = 'binary'
do_not = "don't"
y = "Those who do know %s and those who %s" % (binary, do_not)

#printing out the variables
print x
print y

#print I said There are 10 types of people
print "I said: %s" % x
#print out y using the string variable
print "I also said: '%r'." % y

#defining variables hildarious and joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke funny? %r"

print joke_evaluation % hilarious

#Define w and e variables
w = "This is the left side of..."
e = "a string with a right side."

#This will print out w and e, e right after w
print w + e
