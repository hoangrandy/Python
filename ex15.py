from sys import argv

script, filename = argv

#This opens an already existing file if you do python ex15.py (filename)
txt = open(filename)

#This will print out the filename
print "Here's your file %r:" % filename


#This will print out whatever is in the file
print txt.read()

#Using file_again and a self input if you type in the file name again it will open the file again
print "I'll also ask you to type it again:"
file_again = raw_input("> ")

#This opens the file again
txt_again = open(file_again)
#This prints out the contents of the file
print txt_again.read()
