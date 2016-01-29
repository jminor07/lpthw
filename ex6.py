# Exercise 6: Strings and Text

# I'm not quite sure why Zed teaches this and then teaches the .format() way later on.

# old binary joke because 2 in binary is 10. Meant to confuse people that thing 10 is in decimal and not in binary.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
# using two arguments for the print statements. They must be enclosed in () an separated by a comma.
print y

# just a usual print statement with %r meaning print the variable x and y "no matter what"
print " I said: %r." % x
print "I also said: '%s'." % y

# setting hilarious to the
hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

# we are printing the string "isn't that joke so funny?! %r" and the variable hilarious will be what we put in
# for %r
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

# we can print a string on one line by creating them separately and then adding them in a print statement
print w + e