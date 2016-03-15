name = 'Johnny Minor'  # assigning a variable to string
my_age = 26  # age is just a number anyways.
my_height = 71  # inches
my_weight = 190  # pounds
my_eyes = 'Brown'  # assigning a variable to string
my_teeth = 'whiteish'  # assigning a variable to string
my_hair = 'Black'  # assigning a variable to string

print "Lets talk about %s." % name  # printing variable with %s (string)
print "He's %d inches tall." % my_age  # printing variable with %d (int)
print "He's %d pounds heavy." % my_weight  # print variable with %d (int)
print "Actually that's not too heavy..."  # printing string with double quotes
print "He's got %s eyes and %s color hair." % (my_eyes, my_hair)  # printing two variables both %s
print "His teeth are usually %s depending on how much coffee and tea." % my_teeth # printing variable

# I'll try to get this right the first time.
print "If I add %d, %d, and %d then I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
# we can print multiple things by putting them all inside parenthesis separated by a comma.
# we can also do math within the print.
