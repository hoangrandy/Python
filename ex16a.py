from sys import argv

script, filename = argv

print "We are going to read %r" %filename
print "If you do not what to read this file, Hit CTRL-C (^C)"
print "If you wish to proceed, hit RETURN."

raw_input("?")

print "Opening the file"
txt = open(filename)

print txt.read()
print txt.close()
