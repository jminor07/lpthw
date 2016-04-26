# doing things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# Will split on an empty character ' ' into array
stuff = ten_things.split(' ')

# creating a new list of strings.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # popping off the stack and storing in temp var next_one
    # as we would expect pop() is a destructive function. Once it is popped off the array(stack) then it is gone.
    # so we need to be careful to copy to a temp var! 
    next_one = more_stuff.pop()

    # we then use append to put what we popped off onto the stuff array.
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# python is 0 based index so stuff[1] gets the the second element
print stuff[1]
# we can start from the end of the list using the negative
print stuff[-1]
# we can pop off the last element of the array.
print stuff.pop()
# print stuff.pop()
# can put an array together using join() and remove the double quotes
print ' '.join(stuff)
# slicing the 4th and 5th element and putting a '#' in between them.
print '#'.join(stuff[3:5])


