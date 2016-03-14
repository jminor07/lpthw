# functions can return something


def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# guess: -4426. whoops forgot to add 35! to get the -4391
print "That becomes: ", what, "Can you do it by hand?"
# answer: -4391

# this is really much of a puzzle. We just have to recursively go
# through all the functions and do the math. Zed calls this "inside out".
# It Seems just like a recursive function to me...

# in other words we calculate divide() and return that number to multiply() we multiply
# and then return that number to subtract(). We then return subtract() to add() and
# we get our answer.
