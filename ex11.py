# Asking questions, or how to get user input


# print "How old are you?",  # we put a comma here so the print doesn't go to the next line.
# age = raw_input()  # eat your heart out scanf()!
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh.",
# weight = raw_input()
#
# print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# we can get some user input ourselves!

print "enter two numbers between 0 and 100 that you would like to multiply."
temp1, temp2 = raw_input().split()

# casting as a float to be able to do the comparison
temp1 = float(temp1)
temp2 = float(temp2)

# if the variables were assigned then x1 and x2 will have changed.
x1 = -1
x2 = -1

# we'll first check if temp1 and temp2 are between 0 and 100.
# if they are we'll assign them to the variables to do calculations.
# this is a really slick comparison.
if 0 <= temp1 <= 100:
    x1 = temp1
else:
    print"The first value you entered is invalid."


if 0 <= temp2 <= 100:
    x2 = temp2
else:
    print"The second value you entered is invalid."


# if the temp variables were never assigned then we can't do the calculation.
# pycharm wanted to factor the comparison to this demorgan law. This seemingly gives the same behavior.
# I'm not sure if this would be considered more readable.
if not (not (x1 != -1) or not (x2 != -1)):
# if x1 != -1 and x2 != -1:
    # finally we will do the calculation.
    z = x1 * x2

    print 'The result of {0} * {1} = {2}'.format(x1, x2, z)

