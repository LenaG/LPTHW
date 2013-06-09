# defining variable x with string, inside string interpolating the number 10 into place holder
x = "There are %d types of people." % 10
# defining variable with string
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s' ." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

name = raw_input("what's your name?")
print "Hey %s , what's your name?" %name
