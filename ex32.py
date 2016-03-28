# loops and lists!

the_count = [1, 2, 3, 4, 5]
fruit = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# we can iterate over a list in a for loop
for number in the_count:
    print "This is the count %d" % number

# we can go through a  mixed list.
# we use %r because we don't know what's in it.
for i in change:
    print "I got %r" % i

# we can also build an empty list.
elements = []

# we can use range() to count from 0 to 5
for i in range(0,6):
    print "Adding %d to the list" % i
    # append is a method of the list object. It just will just add the argument to the end
    elements.append(i)

for i in elements:
    print "Element was: %d" % i
    
