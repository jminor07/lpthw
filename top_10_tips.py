# some neat tips and tricks in Python
# taken from: http://raymondtaught.me/the-python-way-10-tips/

# 1. list comprehensions

# most people would do create a list
bag = [1, 2, 3, 4, 5]
for i in range(len(bag)):
    bag[i] = bag[i] * 2

# but we can do it like this
# called list comprehensions
bag = [elem * 2 for elem in bag]

# 2. Iterating through a list

# avoid doing this!
bag = [1, 2, 3, 4, 5]
for i in range(len(bag)):
    print(bag[i])

# do this instead!
for i in bag:
    print(i)

# since we usually don't care about the index of the elements
# if we did just use enumerate.

bag = [1, 2, 3, 4, 5]
for index, element in enumerate(bag):
    print(index, element)
    # print(element)

# 3. Swapping Elements.

a = 5
b = 10

tmp = a
a = b
b = tmp

# but with python we can do this instead!
a = 5
b = 10
# swapping a and b
a, b = b, a

print a, b


# 4. initializing a list
bag = []
for _ in range(10):
    bag.append(0)

# but we can just multiply instead.
bag = [0] * 10

# raymond says to be mindful that creates
# a shallow copy if you're working with a list within a list

bag_of_bags = [[0]] * 5  # [[0], [0], [0], [0], [0]]
bag_of_bags[0][0] = 1  # [[1], [1], [1], [1], [1]]

bag_of_bags = [[0] for _ in range(5)]
# [[0], [0], [0], [0], [0]]

# this doesn't work...
# bag_of_bags = [[0] * 5]
# [[0, 0, 0, 0, 0]]

print bag_of_bags

bag_of_bags[0][0] = 1
# [[1], [0], [0], [0], [0]]



# 5. String building

# we could build a string like this
name = "Johnny"
age = 26
born_in = "Minneapolis, MN"
string = "Hello my name is " + name + "and I'm " + str(age) + " years old. I was born in " + born_in + "."
print(string)

# but it's way too messy. Should use .format() method instead.

name = "Johnny"
age = 26
born_in = "Minneapolis"
string = "Hello my name is {0} and I'm {1} years old. I was born in {2}.".format(name, age, born_in)
print(string)


# 6. Returning tuples.
# in python we can return multiple elements in a function.

def binary():
    return 0, 1

result = binary()
zero = result[0]
one = result[1]
# but this is unnecessary and SHOULD do this instead.


zero, one = binary()

# if you don't need the all of your elements returned then use and underscore _
zero, _ = binary()

# 7. Accessing Dicts
counter = {}
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
for i in bag:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for i in range(10):
    if i in counter:
        print("Count of {}: {}".format(i, counter[i]))
    else:
        print("Count of {} : {}".format(i, 0))


# the better way to do this is to use get()


counter = {}
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
for i in bag:
    counter[i] = counter.get(i, 0) + 1

for i in range(10):
    print("Count of {}: {}".format(i, counter.get(i, 0)))


# here's a simpler but costlier way
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
counter = dict([(num, bag.count(num)) for num in bag])

for i in range(10):
    print("Count of {}: {}".format(i, counter.get(i, 0)))

# there's also dictionary comprehensions.
counter = {num: bag.count(num) for num in bag}

# 8. Using Libraries.
# usually what you're trying to has probably been done.
# for example

from collections import Counter
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
counter = Counter(bag)

for i in range(10):
    print("Count of {}: {}".format(i, counter[i]))


# 9. Slicing through a list.
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for elem in bag[:5]:
    print(elem)

bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for elem in bag[-5:]:
    print(elem)

# not the best way to do it.
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, elem in enumerate(bag):
    if index % 2 == 0:
        print(elem)


# this is the way to get every other element.
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for elem in bag[::2]:
    print(elem)

# or equivalently for ranges
bag = list(range(0, 10, 2))
print(bag)

# 10. Tabs vs spaces
# mixing tabs and spaces in python will lead to a disaster.

