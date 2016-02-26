from sys import argv
# from os.path import exists

# reading in from the command line
script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# in_file = open(from_file)
# indata = in_file.read()

# read() will bring in everything just as we would expect and even accounts for the newline.
# indata = open(from_file).read()

# pretty cool that we can read the number of bytes using this len() function
# print "The input file is %d bytes long." % len(indata)

# exists() returns bool value on the string argument of the file name
# although Zed says we could comment this out.
# I think it's kinda nice t0 check if the file exists before just haphazardly writing out to it.
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, or CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# this might work to do it all in one line.
# open(to_file, 'w').write(indata)


# print "Alright all done."

# closing the files that we had opened.
# when we put everything into one line we don't have to open and then close the files. Very nice!
# out_file.close()
# in_file.close()

# As Zed says we could really put the entire script on a single line.
# It might not be the most readable code(at least for a novice like me), but it can be done.

open(to_file, 'w').write(open(from_file).read())


