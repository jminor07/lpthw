# we take a test to correct some code


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):  # missing colon
    """Prints the first word after popping it off."""
    word = words.pop(0)  # lol pop not poop
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)  # missed closing parenthesis
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# misspelled "explanation"

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6  # should be -6 not -5
print "This should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000  # tried to use forward slash for division and not backslash!
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# it's = not == !!!!
beans, jars, crates = secret_formula(start_point)  # hyphen instead of an under score

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

# changed to an augmented statement
start_point /= 10

print "We can also do that this way:"
# missed and parenthesis and a 'i' in start_point
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

# misspelled good
# used weight instead of wait
# don't give it an escape sequence in the string 
sentence = "All good things come to those who wait."

# we are actually using ex26 and not ex25 but we don't use access the functions this way since
# we're not in the command line!
words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)  # period in front of print
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words  # missed a 't' in print

# forgot the 'f' in the function
print_first_and_last(sentence)

# misspelled the function name and the argument
print_first_and_last_sorted(sentence)  # you can't indent whenever you like


# I probably missed something but that seems to be a