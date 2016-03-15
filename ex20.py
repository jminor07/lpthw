# import to use argv. argv allows us to get user input from command line
from sys import argv

# "unpacking" our arguments from command line
script, input_file = argv


def print_all(f):  # defining the function "print_all" that takes one argument and returns nothing
    print f.read()  # printing everything in the file "f"

# The method seek() sets the file's current position at the offset.
# The whence argument is optional and defaults to 0, which means absolute file positioning,
# other values are 1 which means seek
# relative to the current position and 2 means seek relative to the file's end.


def rewind(f):  # defining the function "rewind" that takes one argument f and returns nothing
    f.seek(0)


def print_a_line(line_count, f):  # defining the function "print_a_line" that takes two arguments
    print line_count, f.readline()  # printing the two arguments


# we open the input file
current_file = open(input_file)

print "First let's print the whole file:\n"  # printing a string with double quotes and using \n to a newline.

# using our print all function we can just pass our current_file and print everything.
print_all(current_file)   # calling the "print_all" function with current_file as argument

print "Now let's rewind, kind of like a tape."  # printing a string with double quotes.

# with the seek() method is seems that we are starting at the top again.
rewind(current_file)  # calling the "rewind" function with current_file as argument

print "Let's print three lines:"

# of course we could use a for loop, but I don't think Zed has shown it.
# current_line = 1
# print_a_line(current_line, current_file)
#
# # use the += operator because it's nicer.
# current_line += 1
# print_a_line(current_line, current_file)
#
# current_line += 1
# print_a_line(current_line, current_file)

# This gives the same result as Zed's code but is more compact.
# we iterate over i from 1 to the first integer less than 4 (i.e. 3) 
for i in range(1, 4):
    print_a_line(i, current_file)

