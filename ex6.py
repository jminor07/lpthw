# Exercise 6: Strings and Text

# I'm not quite sure why Zed teaches this and then teaches the .format() way later on.

# old binary joke because 2 in binary is 10. Meant to confuse people that thing 10 is in decimal and not in binary.
x = "There are %d types of people." % 10  # assigning a variable to an entire print statement.
binary = "binary"  # assigning variable to string with double quotes.
do_not = "don't"  # assigning variable to string with double quotes.
# assigning variable to entire print statement with variables
y = "Those who know %s and those who %s." % (binary, do_not)


print x  # once we do this we will actually do the print statement that we assigned to x
# using two arguments for the print statements. They must be enclosed in () an separated by a comma.
print y  # once we do this we will actually do the print statement that we assigned to x

# just a usual print statement with %r meaning print the variable x and y "no matter what"
print " I said: %r." % x  # we can embed two print statements together like this
print "I also said: '%s'." % y  # we can embed two print statements together like this

# setting hilarious to the bool value
hilarious = False  # assign variable to bool value False
joke_evaluation = "isn't that joke so funny?! %r"  # assigning variable to a string

# we are printing the string "isn't that joke so funny?! %r" and the variable hilarious will be what we put in
# for %r
print joke_evaluation % hilarious  # curious way of printing a string and then the bool value

w = "This is the left side of ..."  # assigning a variable to a string with double quotes
e = "a string with a right side."  # assigning a variable to a string with double quotes

# we can print a string on one line by creating them separately and then adding them in a print statement
print w + e  # we can concatenate a string easily with the addition operator.
