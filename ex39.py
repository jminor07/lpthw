# dictionaries!!
# the lovely data structure of dictionaries.

stuff = {'name': 'Johnny', 'age': 27, 'height': 60}

print stuff['name']

print stuff['age']

print stuff['height']

# adding an entry to the dictionary
stuff['city'] = "Pullman"
print stuff['city']

# but we don't need to just use strings. For example.
stuff[1] = "Wow"
stuff[2] = "Neato"

# no need for the single quotes.
print stuff[1]

# can also use double quotes just the same.
print stuff["city"]

# we can also delete things from our dictionary using del
del stuff['city']
del stuff[1]
del stuff[2]

print stuff

# ********** now for the actual part of the program ***************
# maps state name to abbreviation

states = {
    'Oregon': 'OR',
    # 'Florida': 'FL',
    'California': 'CA',
    'Washington': 'WA',
    'Minnesota': 'MN'
}

# creates a basic set of states and some cities in them.
cities = {'WA': 'Seattle', 'MN': 'Minneapolis', 'OR': 'Portland', 'NY': 'New York'}

# adding some cities.
# pycharm recognizes this is silly and wants to put everything together!
cities['CA'] = 'Sacramento'
cities['MI'] = 'Detroit'

# print some cities.

# print out some cities.
# this is a nifty way to print dashes.
print '-' * 25
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '*' * 10
print "Washington's abbreviation is: ", states['Washington']
print "Minnesota's abbreviation is: ", states['Minnesota']

# we can nest some dicts within dicts.
print "$$" * 10
print "Washington has: ", cities[states['Washington']]  # SWEEET
print "Minnesota has: ", cities[states['Minnesota']]

# print every state abbreviation
print "~" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# can safely get an abbreviation by state that might not be there.
state = states.get('Texas')

# a tricky comparison.
if not state:
    print "sorry, no Texas."

# get a city with a default value.
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


