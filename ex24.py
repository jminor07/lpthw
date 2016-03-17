# An exercise to review what we've covered so far.

# we know about making an apostraphe with \'
# and about making a backslash with two \\
# and \n is a newline
# and \t is a tab (four spaces)
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# we can assign a string to a variable
# and we can make multiple lines with three doubles quotes
# inside three double quotes you can't even make comments because it doesn't recognize the '#'
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------"
print poem
print "-------------"

# we can do math and assign the result to a variable
five = 10 - 2 + 3 - 6
# we can print a variable as a string with %s
print "This should be five: %s" % five

# we can define a function that returns multiple variables.
# we can also create variables within the function because once we leave the function they will be erased.
def secret_formula(started):
    jelly_beans = started * 500
    # pycharm warns that var jars and crates are outside scope.
    # not sure if this is poor practice or not?
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates  # no pointers needed!

start_point = 10000
# how to return multiple things to variables!
beans, jars, crates = secret_formula(start_point)

print "with a starting point of: %d" % start_point
# pretty standard way of calling a function. assigning what it returned to vars and then printing those vars.
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# augmented statement instead of the way Zed does it.
start_point /= 10

# this is an interesting way of implementing the function
# we call the function and since we have a print statement with our three variables
# it makes we wonder if we could print what the function returns without
# having prior knowledge of how many vars it returns.
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

