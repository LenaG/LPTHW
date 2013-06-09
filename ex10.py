# \ omits quotes right after it
print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

# \t = tab, indent
tabby_cat = "\tI'm tabbed in."
# \n = new line
import time 
import sys
persian_cat = "I'm split\non a line."
# \\ = prints one \
backslash_cat = "I'm \\ a \\ cat."

# """ = print all inside with all indents
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# pasha be crazy
while True:
 for i in ["/","-","|","\\","|"]:
     time.sleep(.3)   
     print "%s\r" % i,
     sys.stdout.flush()

