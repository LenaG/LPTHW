# defined variable with placeholders
formatter = "%r %r %r %r"

# printed variable with diff meaning for placeholder, numbers, strings, defined boolean, variable itself inserted into placeholder, and strings again with commas to make shorter lines of code
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
     'I had this thing.',
     'That you could type up right.', 
     "But it didn't sing." , 
     'So I said goodnight.'
)
