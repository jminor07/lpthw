# from a talk "transforming code into beautiful code, idiomatic python"
# i thought he shows great pythonic ways of doing things. Especially coming from C/C++

# looping over a range of numbers
import itertools

# don't do this
for i in [0, 1, 2, 3, 4, 5]:
    print i ** 2

# don't do this either
for i in range(6):
    print i ** 2

# Do this!
# xrange() creates an iterator so you don't run into issues with large values.
# in python 3 xrange() -> range()
for i in xrange(6):
    print i ** 2

# looping over a collection

colors = ['red', 'green', 'blue', 'yellow']

# Do not do it this way. We aren't using C anymore!
for i in range(len(colors)):
    print colors[i]

for color in colors:
    print color

# how to loop backwards.
# but do not do this!
for i in range(len(colors) - 1, -1, -1):
    print colors[i]

# Do use reverse
for color in reversed(colors):
    print color

for i in range(len(colors)):
    print i, '-->', colors[i]

# can use enumerate without using indices.
# DO use enumerate!
for i, color in enumerate(colors):
    print i, '-->', colors[i]

# usually when your using indices directly your probably doing it wrong.


# how to loop over two collections at once?
names = ['Johnny', 'Griet', 'Tiger']
colors = ['blue', 'celeste', 'green', 'orange']

n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]

# this uses a lot of memory
for name, color in zip(names, colors):
    print name, '-->', color

# on modern processors it only matters if it's running on L1 cache.
# so now we can use izip
# for name, color in izip(names, colors):
#     print name, '-->', color

# looping in sorted order
for color in sorted(colors):
    print color

for color in sorted(colors, reverse=True):
    print color


# how to do a custom sort order
# the customary way

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0


print sorted(colors, cmp=compare_length)

# a more python way.
# gets only called once!
# this is bloody amazing.
# shorter and faster!
print sorted(colors, key=len)


# call a function until a sentinel value
# blocks = []
# while True:
#     block = f.read(32)
#     if block == '':
#         break
#     blocks.append(block)

# iter can two arguments.
# blocks = []
# for blocks in iter(partial(f.read, 32), ''):
#     blocks.append(block)
#
# many of the tools in python are made for iterables.


# distinguishing multiple exit points in loops.
# problem with this is that you need a flag.
# but this is slow and makes it less readable.
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == tgt:
            found = True
            break
    if not found:
        return -1
    return i


# there is a better way to do it!
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i


# dictionary skills
# mastering dictionaries is a fundamental python skill

# looping over dictionary keys.
d = {'Johny': 'celeste', 'Griet': 'Green', 'Tiger': 'Orange'}

for k in d:
    print k

# use this if you are mutating the dictionary.
# do not change while iterating something, bad things will happen.
for k in d.keys():
    if k.startswith('J'):
        del [k]

# more ways of doing this.
d = {k: d[k] for k in d if not k.startswith('J')}

print d

# looping over a dictionary keys and values

for k in d:
    print k, '-->', d[k]

# there's a better way.
for k, v in d.items():
    print k, '-->', v

# best way iteritems() is an iterator.
for k, v in d.iteritems():
    print k, '-->', v

# constructing a dictionary from pairs.
# can create with any iterator and join them into a dictionary.
names_and_colors = dict(itertools.izip(names, colors))

d = dict(enumerate(names))

# how to count with a dictionary
# a very simple and basic way of counting
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

# print d

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# print d
# now a regular dict but a default dict.
from collections import defaultdict

# the more modern way using defaultdict()
d = defaultdict(int)
for color in colors:
    d[color] += 1

# grouping with dictionaries -- Part I

names = ['Johnny', 'Griet', 'Tiger', 'Kevin', 'Cole', 'Rachel', 'Jared']

# this little snippet will group together by the length of the name.
# pretty nifty!
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []  # if the key isn't already in the dict then make an empty one.
    d[key].append(name)  # append the name to that key in the dict.

# there is an even better way to do this!
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

# the best way!
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# is dictionary popitem() atomic?
# it's atomic. (?)
print '*' * 10
# print names_and_colors
while names_and_colors:
    key, value = names_and_colors.popitem()
    print key, '-->', value

# linking dictionaries.
defaults = {'color': 'red', 'user': 'guest'}

# can use ChainMap in python 3
# fast and beautiful
# d = ChainMap(command_line_args, os.environ, defaults)

# keywords and names are better than iterates because thats how humans read!
# clarify function calls with keyword arguments.

# twitter_search('@obama', False, 20, True)

# replace obscure arguments with keyword arguments
# twitter_search('@obama', retweets=False, numtweets=20, popular=True)

# clarify multiple return values with named tuples
# example: doctest.testmod()
# returns (0, 4)

# doctest.testmod()
# returns this which is much easier to read!
# TestResults(failed=0, attempted=4)


p = 'Johnny', 'Minor', 27, 'python@gmail.com'

# this is how you would usually do it in any other language.
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

fname, lname, age, email = p


# updating multiple state variables.

# raymond hates this code.
# this is too low level.
def fibonacci(n):
    x = 0
    y = 0
    for i in range(n):
        print x
        t = y
        y = x + y
        x = t


# can instead use tuple unpack and packing.
# this is incredibly slick.
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y

        # another example in sci comp


# simultaneous state updates.

# dont do this!
# tmp_x = x + dx * t
# tmp_y = y + dy * t
# tmp_dx = influence(m, x, y, dy, partial='x')
# tmp_dy = influence(m, x, y, dy, partial='y')
# x = tmp_x
# y = tmp_y
# dx = tmp_dx
# dy = tmp_dy

# do do this! because we dont' get burned/ have to worry about copying over data!
# x, y, dx, dy = (x + dx *t, y + dy *t, influence(m, x, y, dy, partial='x'), influence(m, x, y, dy, partial='y') )

# efficiency - just don't move things around!

# concatenating strings
# do not do this
s = names[0]
for name in names[1:]:
    s += ', ' + name
print s

# this is the best way to do it and is much faster.
print ', '.join(names)

del names[0]
names.pop(0)
names.insert(0, 'Saar')

from collections import deque

# the correct data structure is a deque
names = deque(['Johnny', 'Griet', 'Tiger'])

del names[0]
names.popleft()
names.appendleft('Saar')

# print names

# decorators and context managers.
# helps separate business logic from administrative logic
# clean, beautiful tools for factoring code and improving code reuse
# good naming is essential
# Spiderman rule: with great power, comes great responsibility!

# using decorators to factor-out administrative logic

# def web_lookup(url, saved={}):
#     if url in saved:
#         return saved[url]
#     page = urllib.urlopen(url).read()
#     saved[url] = page
#     return page
#
# @cache
# def web_lookup(url):
#     return urllib.urlopen(url).read()

# how to open and close files
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()

# this is the new and cool way to do it.
with open('data.txt') as f:
    data = f.read()

import threading

# how to use locks
# make a lock
lock = threading.Lock()

# old way to use a lock
lock.acquire()
try:
    print 'Critical section 1'
    print 'Critical section 2'
finally:
    lock.release()


# new way to use a lock
with lock:
    print 'Critical section 1'
    print 'Critical section 2'

# factor out temporary contexts
# try:
#     os.remove('somefile.tmp')
# except OSError:
#     pass

# here's a better way to do it.
# with ignored(OSError):
#     os.remove('somefile.tmp')


# factor out temporary contexts
# with open('help.txt', 'w') as f:
#     oldstout = sys.stdout
#     sys.stdout = f
#     try:
#         help(pow)
#     finally:
#         sys.stdout = oldstout
#
# with open('help.txt', 'w') as f:
#     with redirect_stdout(f):
#         help(pow)


# concise expressive one-liners
# two conflicting rules:
# 1. don't put too much on one line.
# 2. Don't break atoms of thought into subatomic particles.

# Raymond's rule:
# One logical line of code equals of one sentence in English.

# list comprehensions and generator expressions.

result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print sum(result)

# using list comprehension
print sum([i**2 for i in xrange(10)])



