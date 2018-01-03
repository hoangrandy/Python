#This program will copy a file and copy it to a different file.
#You will have to run this with two arguements e.g. python py17.py test.txt copy.txt
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#Tells the user that the program is going to copy file 1 to file 2
print "Copying from %s to %s" % (from_file, to_file)

#This opens the file and reads it
input = open(from_file)
indata = input.read()

#Tells the user how many bytes the first file is
print "The input file is %d bytes long" % len(indata)
#This will tell the user whether or not the first file exists
print "Does the output file exist? %r" % exists(to_file)
#This will ask for the user for input, if they would like to continue the copy
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#This will open the second file (or make) and copy indata (which is the first file contents)
output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

#This will close both files
output.close()
input.close()
