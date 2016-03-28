# in this exercise we learn about the else if and else statement and how they relate to the if statement.

people = 25
cars = 42
trucks = 65


if cars > people:

    # if car > people is true then do this stuff

    print "We should take the cars."

elif cars < people:
    # if cars > people is false then check this
    # if cars < people then do this
    print "We should not take the cars."
else:
    # if neither are true then do this
    print "We can't decide."


if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright let's just take the trucks."
else:
    print "Fine, let's stay home then."


if cars > people or trucks < cars:
    print "More cars than people and trucks!"
