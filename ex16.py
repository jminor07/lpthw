# reading and writing files

# close() -- closes the file. Similar to File->Save
# read() -- reads the contents of the file. You can assign the result to variable.
# readline() -- reads only one line of the file.
# truncate() -- Empties the file. Be careful if you care about the file.
# write('stuff') -- Writes "stuff" to the file.

from sys import argv

script, filename = argv

# warn the user the we're going to truncate the file with the name they gave us.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# give them a chance to abort the mission.
raw_input("?")

# opening the file as 'w' or write. This allows us to make changes to file.
print "Opening the file..."
target = open(filename, 'w')

# using the truncate() method to delete the file.
# there are presumably other arguments for truncate to not just erase the whole thing.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# getting user input to the then write out to the file.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# using the write() method to print to the file
# we can even put strings on a new line by writing the escape sequence "\n"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# importantly we close the file!
print "And finally, we close it."
target.close()


# it is redundant to user .truncate() when we opened the file with write privileges.
# this is because opening in write mode will overwrite the file.
