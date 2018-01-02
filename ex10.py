#The \t would give the line an indent
tabby_cat = "\tI'm tabbed %s." % "in"
#The \n would return and start on a new line
persian_cat = "I'm split \n %r" % "on a line"

#Typing in two backslash will only print out one backslash
backslash_cat = "I'm \\ a \\ cat."
#This will create a list using """ which puts everything in a string before the end """
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

#print out the variables!
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
