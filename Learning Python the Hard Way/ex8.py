#Assigns 4 variables to formatter
formatter = "%r %r %r %r"
#This will print out numbers 1-4
print formatter % (1, 2, 3, 4)
#This will print out the strings one - four
print formatter % ('one', 'two', 'three', 'four')
#%r will print out whatever is on the right as long as it is in the right format
print formatter % (True, False, False, True)
#This will print out 4time "formatter"
print formatter % (formatter, formatter, formatter, formatter)
#This will print out 4 phrases
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing",
    "So I said goodnight."
)
