#import package
from sys import argv

script, user_name = argv
#Set up prompt as >
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

#asking the user if they like me or not
print "Do you like me %s" % user_name
likes = raw_input(prompt)

#Asking user where do they live
print "Where do you live %s" %user_name
lives = raw_input (prompt)

#Asking what kind of computer does user have
print "What kind of computer do you have?"
computer = raw_input(prompt)


#This will print out the results of the questions
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)
