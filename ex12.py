# prompting the user
# you can put a string inside the raw_input() function!

# a simple example goes like this.
y = raw_input("Name? ")

# this is really nice and we can rewrite ex11.py by implementing this new knowledge. Very slick.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# just for fun/practice.
print "So you're {0} old, {1} tall and {2} heavy." .format(age, height, weight)

# Zed says to check out "pydoc raw input" in terminal.
# It looks like it's just some documentation on the raw_input() function.

# from the documentation on pydoc:
# "The pydoc module automatically generates documentation from Python modules."

