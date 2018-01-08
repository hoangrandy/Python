#This program is for practicing functions and calling them 

#This function will add inputs a and b and returns the answer
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

#This function will subtract a and b and returns the answer
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
#This function will multiple inputs a and b and return the answer
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

#This fuction will divide inputs a and b and return the answer
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

#This declaring variables using functions, so age is = 30 + 5 = 35.  returns 35
age = add(30, 5)
#Height = 78 - 4 = 74.  Height returns 74s
height = subtract(78, 4)
#Weight = 90 * 2 = 180.  Weight returns 180
weight = multiply(90, 2)
#IQ returns 50
iq = divide(100, 2)

#This will print out the variables in which we already declared its values using
#variables
print "Age: %d, Height: %d, Weight %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, let's type it anyways
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
