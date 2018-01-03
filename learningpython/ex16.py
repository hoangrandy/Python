from sys import argv

script, filename = argv

#Ask the user if they want to delete the file or not
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit return."

raw_input("?")

#opens the file and w lets it write over the file
print "Opening the file..."
target = open(filename, 'w')

#truncates the file
print "Truncated the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#Asks user to input 3 lines to be written in the doc
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"
#this writes the lines that was inputed
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#this closes the file
print "And finally, we close it."
target.close()
