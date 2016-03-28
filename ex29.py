# we are introduced to the if statement

people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! the world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people > dogs:
    print "The world is dry!"

# augmented addition
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."

# the if statement says that if the thing is true True then enter the if statement and do what's inside it.
# the code needs to be indented to tell python that the code is part of the if statement. i.e. Syntax
# if it isn't indented python complains!
# yes we can put other boolean expressions in an if statement
# if we change the values of people, cats and dogs then we get different behaviour