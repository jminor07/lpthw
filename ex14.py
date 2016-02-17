# importing  the sys module or library.
# This allows us to get user input from the command line.
from sys import argv

# unpacks the script name and user name.
script, user_name = argv

# creates a string that we can later pass to raw_input()
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name

# having the argument as the variable prompt is pretty nice.
likes = raw_input(prompt)

# getting user input again.
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)


# using three double quotes to print multiple lines.
# we use %r because we're not sure what sort of input the user will give us.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. I hope it's warm there.
And you have a %r computer. Sweet.
""" % (likes, lives, computer)



