# This program is for practicing functions and understanding them
# This program will print the whole file then print out the first 3 lines

from sys import argv
#script and input_file for reading/printing files for later
script, input_file = argv

def print_all(f):
    print f.read()

# What seek does is pointing the reference to a specific location to the file
# 0: means your reference point is the beginning of the file
# 1: means your reference point is the current file position
# 2: means your reference point is the end of the file

def rewind(f):
    f.seek(0)

# f.readline() reads a single line from the file; a newline character (\n)
# is left at the end of the string, and is only omitted on the last line of the
# file if the line ends in newline.
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

#Assigning a variable to line_count
current_line = 1
#This prints out the first line
print_a_line(current_line, current_file)

#this add 1 to current_line which is 1, so this prints out the second line
current_line = current_line + 1
print_a_line(current_line, current_file)

#This adds 1 to current_line which is 2, so this prints out the third line
current_line = current_line + 1
print_a_line(current_line, current_file)
