# functions can return something


def add(a, b):  # defining the function add that take two arguments and returns the sum
    print "ADDING %d + %d" % (a, b)  # letting the user know what we're doing
    return a + b  # returning the sum so it can be assigned to a variable


def subtract(a, b):  # defining the function subtract that takes two arguments and returns the difference
    print "SUBTRACTING %d - %d" % (a, b)  # letting the user know what we're doing
    return a - b  # returning the difference so it can be assigned to a variable.


def multiply(a, b):  # defining the function multiply that takes two arguments and returns the product
    print "MULTIPLYING %d * %d" % (a, b)  # letting the user know what we're doing
    return a * b  # returning the difference so it can be assigned


def divide(a, b):  # defining the function divide that takes two arguments and returns the quotient
    print "DIVIDING %d / %d" % (a, b)  # letting the user know what we're doing
    return a / b  # returning the quotient so it can be assigned.


print "Let's do some math with just functions!"  # printing a string with double quotes.

age = add(30, 5)  # calling the function add and assigning what it returns to the variable age
height = subtract(78, 4)  # calling the function subtract and assigning it to the height var
weight = multiply(90, 2)  # calling multiply and assigning it to weight
iq = divide(100, 2)  # calling divide and assigning it to iq


# print statement with four arguments that we assign with the variables.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."


# we are putting functions within functions within functions within functions.
# we have to keep going deeper until we finally hit an actual return statement
# then we can go back out to get the answer that we want
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
