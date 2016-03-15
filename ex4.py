cars = 100  # assigning variable
space_in_car = 4.0  # float because of the decimal point
drivers = 30  # assigning variable
passengers = 90  # assigning variable
cars_not_driven = cars - drivers  # subtracting variables
cars_driven = drivers  # assigning variable to other variable
carpool_capacity = cars_driven * space_in_car  # multiplying variables as if they were numbers
average_passengers_per_car = passengers / cars_driven  # dividing variables


print "There are", cars, "cars available."  # we can put a variable between two statements in
# double quotes
print "There are only", drivers, "drivers available."  # we can put a variable between two statements in
# double quotes
print "There will be", cars_not_driven, "empty cars today."  # we can put a variable between two statements in
# double quotes
print "We can transport", carpool_capacity, "people today."  # we can put a variable between two statements in
# double quotes
print "We have", passengers, "to carpool today."  # we can put a variable between two statements in
# double quotes
print "We need to put about", average_passengers_per_car, "in each car."  # we can put a variable between two statements in
# double quotes

# study drill question:
# you get this error because the variable "car_pool_capacity" was never defined.
# Zed probably forgot the assignment operator.
