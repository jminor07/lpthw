# import to use argv. argv allows us to get user input from command line
from sys import argv

# "unpacking" our arguments from command line
script, input_file = argv


def print_all(f):
    print f.read()

# The method seek() sets the file's current position at the offset.
# The whence argument is optional and defaults to 0, which means absolute file positioning,
# other values are 1 which means seek
# relative to the current position and 2 means seek relative to the file's end.
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline()


# we open the input file
current_file = open(input_file)

print "First let's print the whole file:\n"

# using our print all function we can just pass our current_file and print everything.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# with the seek() method is seems that we are starting at the top again.
rewind(current_file)

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

# couldn't resist
for i in range(1, 4):
    print_a_line(i, current_file)

