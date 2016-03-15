# learning about esacpe sequences in python.
# Zed uses the example: "I "understand" joe."  to illustrate the problem.
# the problem being that python will complain because you have double quotes inside double quotes.

# He also uses two more examples:
"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

# now for the actual program/exercise

tabby_cat = "\t I'm tabbed in"  # the \t is a tab(i.e. four spaces) escape sequence
persian_cat = "I'm split \n on a line."  # \n is the newline escape sequence
backslash_cat = "I'm \\ a \\ cat."  # the double backslash equates to one backslash.

# apparently you can't have comments inside three double quotes.
# line 21 shows that we can actually put two different printed lines on one line of code by using \n
fat_cat = """
I'll do a list:
\t* Cat food
\t* Salmon
\t* Catnip\n\t* Grass
"""

print tabby_cat  # printing out the variables
print persian_cat  # printing out the variables
print backslash_cat  # printing out the variables
print fat_cat  # printing out the variables

# Zed shows us this fun code to try out:
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
#
# while True: means run forever. Well, my IDE doesn't like to run that snippet.(Thanks Zed!!)
# However, it makes a pretty spinning backslash when you run it in the terminal.

# Zed shows us some other escape sequences:
# here we are using all the escape sequences that Zed showed us.
print """
We can use \\ this and \' and \"
or even \a and one of these: \b, \f, \n
\N{johnny}, \r, \t. Or \u0000 and \U00000000,
or how about a vertical tab? \v or octal value
\ooo or a hex value
"""
# I guess my machine does't have some of these escape sequences and python wouldn't even run with \xhh.
