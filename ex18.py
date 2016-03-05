# Functions!

# this function is like a script with argv
# *args is like argv but for functions
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# We don't really need to do it that way
# instead of unpacking args like in "print_two()"
# we can just give them as arguments for the function.
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this can take one argument
def print_one(arg1):
    print "arg1: %r" % arg1


# or we can take no arguments
def print_none():
    print "I have nothing."

print_two("Johnny", "Minor")
print_two_again("Johnny", "Minor")
print_one("First!")
print_none()

