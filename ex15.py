# this exercise is on reading in from files.
# importing the sys module to get
from sys import argv

# we want to get user input for the filename that they want to read in.
# this will make the script more flexible since we haven't "hard coded" the filename in.
script, filename = argv

# we have to open the file "filename"
txt = open(filename)


print "Here's your file %r:" % filename  # printing the filename
print txt.read()  # just read the entire file with no options.

# we could also get user input this way to get user input from the user.
print "Type the filename again:"
file_again = raw_input("> ")

# opening the file again and assigning it to variable txt_again
txt_again = open(file_again)

# using the method of .read() to get the lines from the file.
print txt_again.read()

# it's best practice to close the files when we're done with them!
txt.close()
txt_again.close()

