# more practice on what we've done so far.

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')  # we can use the method split() to break on a space (i.e. the ' ' argument)
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)  # apparently there is already a function to sort?


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)  # pop from the top of the stack!
    return word


def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_first_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


def print_test():
    """This is a test"""


# for some reason this does not work on my machine. It refuses to print anything in my terminal. :/
