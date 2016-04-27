# dictionaries are a way to map one thing to another.
# this maps apples->'i am apples'

mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

import mystuff

# we can then access the function in mystuff with the dot (.) operator.
# we use this all the time when we use numpy/scipy etc.
mystuff.apple()

# now we can access a variable too.
print mystuff.tangerine

mystuff['apple']  # get apple from dict
mystuff.apple()  # get apple from the module.
mystuff.tangerine  # same thing, it's just a variable


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class MyClass:
    

    def myPublicMethod(self):
        print 'public method'

    def __myPrivateMethod(self):
        print 'this is private!!'


obj = MyClass()
