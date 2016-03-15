# printing and more printing

# this is a slick way of printing a bunch of different things.
formatter = "%r %r %r %r"

# this is the equivalent to saying
# print "%r %r %r %r" % (1, 2, 3, 4)
# but this is different way of doing it because then we can reuse the formatter variable
print formatter % (1, 2, 3, 4)  # printing four arguments with 'formatter' variable

# since formatter is using %r we can print anything with it.
# all four arguments have to be within parenthesis and separated by a comma.
print formatter % ("one", "two", "three", "four")  # reusing formatter variable to print four arguments
# interesting that it doesn't print the actual bool values. Instead it just prints True and False.
print formatter % (True, False, False, True)  # since formatter is %r we don't have to worry about what we're printing
print formatter % (formatter, formatter, formatter, formatter)  # printing formatter variable as a string.
print formatter % (
    "I had this thing.",  # this is the first string to go with the first %r in the formatter variable
    "That you could type up right.",  # the second %r in formatter
    "But it didn't sing.",
    "So I said goodnight."
)

