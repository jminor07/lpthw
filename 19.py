# more work on functions.
# Zed shows us that variables created within functions
# are not available to us outside the function
# i.e. they go out of scope

# this is our cheese and crackers function that takes two arguments.
# interestingly we don't actually HAVE to return something.


def cheese_and_crackers(cheese_count, boxes_of_crackers):  # defining a function that takes two arguments
    print "You have %d cheeses!" % cheese_count  # print statement with one argument
    print "You have %d boxes of crackers!" % boxes_of_crackers  # # print statement with one argument
    print "Man that's enough for a party!"  # print statement
    print "Get a blanket. \n"  # print statement with escape sequence \n

# using the function in a pretty standard way of giving numbers directly
print "We can just give the function numbers directly."
cheese_and_crackers(20, 30)  # calling the function "cheese_and_crackers()"

# we can declare variables with numbers like this
print "OR, we can use variables from our script:"
amount_of_cheese = 10  # assigning the variable a value
amount_of_crackers = 50  # assigning the variable a value

# and then pass them onto our function.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # passing variables that hold values to the function

print "We can even do math inside too:"
# whoa, instead of having to manipulate the values outside the function
# we can just alter them within the function call.
# we can do math inside the function call that will first be evaluated before being passsed to the function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# we can use variables and numbers interchangeably
# we can call the function cheese_and_crackers and then combine both the variable and do math
# to it before passing it to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

# Zed said to make a function and then do 10 different things with it.


def check_if_odd(value):

    if value % 2 == 0 and value != 0:
        print "This number is even!"
    else:
        print "This number is odd!"

a = 0

check_if_odd(a)

check_if_odd(a + 2)

check_if_odd(a - 2)

check_if_odd(a + a)

check_if_odd(42)

check_if_odd(42 + 42)

check_if_odd(42**42)

check_if_odd(42 / 10)

check_if_odd(42 // 3)

check_if_odd(17)


