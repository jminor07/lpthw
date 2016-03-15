# Functions!

# this function is like a script with argv
# *args is like argv but for functions

# all of these functions do not return anything!


def print_two(*args):  # defining the function name "print_two" that takes one argument
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# We don't really need to do it that way
# instead of unpacking args like in "print_two()"
# we can just give them as arguments for the function.
def print_two_again(arg1, arg2):  # defining the function "print_two_again" that takes two variables.
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this can take one argument
def print_one(arg1):  # defining the function "print_one" that takes one variable
    print "arg1: %r" % arg1


# or we can take no arguments
def print_none():  # defining the function "print_none" that takes no arguments
    print "I have nothing."

print_two("Johnny", "Minor")  # passing the two variables to the function as strings.
print_two_again("Johnny", "Minor")  # passing two variables to the function as strings
print_one("First!")  # passing an argument to the function as a string
print_none()  # calling the function with no arguments

