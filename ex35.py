# importing exit() so we can use to close the program when the user wins
from sys import exit


def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    # check to make sure you have an actual number and not just a string of letters!
    if "0" in choice or "1" in choice:
        how_much = int(choice)  # casting choice as an integer
    else:
        # we can use a different function within a different function!
        dead("Man, learn to type a number.")

    # a comparison to see if their greedy or not.
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "the fat bear is in front of another door."
    print "How are you going to move the bear?"
    # initialized bear_moved to False meaning the bear is still in front of the door.
    # when the user moves the bear we flip the bool to True.
    bear_moved = False

    while True: # loop forever or until you hit the exit()

        # get user input
        choice = raw_input("> ")

        # a bunch of conditions to look for
        # looks like the way to win would be to enter "taunt bear" which will
        # set bear_moved to True. This will allow you to go through the door with "open door"
        # and then you'll be in the gold room.
        # pretty much anything else will kill you (calling the dead() func)
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He stares at you and you go insane."
    print "Do you flee for your life, or eat your head?"

    # get the user input as a string
    choice = raw_input("> ")

    # flee just sends you back to the beginning where you choose a door.
    # pretty neat way as a string comparison/search.
    # if the string flee is anywhere in the user input it evaluate as true.
    # although what happens if the user puts in "flee head" ? It would see flee because
    # that's the first condition...
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()


def dead(why):
    print why, "Great work!"
    # exiting the program because we died!
    exit(0)


def start():
    print "you are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take."

    choice = raw_input("> ")

    # check user input to put them in either the bear room or cthulhu room
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# begin the program
start()
