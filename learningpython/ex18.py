# functions do three things: 
# 1) They name pieces of code the way variables name strings and numbers
# 2) They take arguments the way your scripts take argv
# 3) Using #1 and #2 they let you make your own "mini scripts" or "tiny commands"

# this one is like the scripts with argv - def creates the function
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" %arg1

# this one takes no arguments
def print_none():
    print " I got nothin'."

# Let's print them out!
print_two("Randy","Hoang")
print_two_again("Randy", "Hoang")
print_one ("First!")
print_none()
