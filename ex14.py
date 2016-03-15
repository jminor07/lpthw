# importing  the sys module or library.
# This allows us to get user input from the command line.
from sys import argv

# unpacks the script name and user name.
script, user_name = argv

# creates a string that we can later pass to raw_input()
prompt = '> '  # using the > as a prompt for the user.

print "Hi %s, I'm the %s script." % (user_name, script)  # using %s to print a string
print "I'd like to ask you a few questions."  # printing a string with double quotes
print "Do you like me %s?" % user_name  # printing using %s and a string.

# having the argument as the variable prompt is pretty nice.
likes = raw_input(prompt)  # passing the variable prompt (a string) to raw_input()

# getting user input again.
print "Where do you live %s?" % user_name  # posing a question to the user with %s
lives = raw_input(prompt) # using the prompt again to get user input

print "What kind of computer do you have?"  # posing a question to the user
computer = raw_input(prompt)  # using the prompt var as an argument for raw_input()


# using three double quotes to print multiple lines.
# we use %r because we're not sure what sort of input the user will give us.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. I hope it's warm there.
And you have a %r computer. Sweet.
""" % (likes, lives, computer)
# we can use %r or %s or whatever inside triple double quotes to print variables



