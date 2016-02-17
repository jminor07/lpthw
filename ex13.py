from sys import argv  # this is an import statement. 'argv' is the argument variable.

# this "unpacks" argv to four variables.
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


# Zed says these things are called modules and will refer to them as that from here on out.
# They're also called libraries. such as the C++ standard library <stdlib>

# we have to run this program from the command line with three additional arguments! Zed uses the example:
# "$ python ex13.py first 2nd 3rd"

# when we try to run the script with too few arguments Python complains:
# "ValueError: need more than 3 values to unpack"
# It seems this error is because it needs four command line arguments when I only supplied three.

# we want to try this out with raw_input() too

favorite_animal = raw_input("please enter the name of your favorite animal:")

# the correct answer is always a tiger. We can entertain the user for a moment like it's not.
print "your {0} favorite animal is a {1}".format(first, "Tiger")

print "Ok, I was joking before. Your {0} favorite animal is a {1}".format(first, favorite_animal)

# Zed says to remember that modules give us features.
# also remember that we can run scripts in ipython with "run ex13.py" 
