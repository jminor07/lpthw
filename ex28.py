# the logical expressions are called "boolean" which is named after George Bool.
# We'll guess what the answer should be and then run it to confirm our answer

# Guess: True
print True and True
# Answer: True

# False
print False and True
# False

# False
print 1 == 1 and 2 == 1
# False

# True
print "test" == "test"
# True

# True equiv to True or True
print 1 == 1 or 2 != 1
# True

# True
print True and 1 == 1
# True

# False
print False and 0 != 0
# False

# True
print True or 1 == 1
# True

# False the two strings are not equal. Hopefully python string comparison knows this too.
print "test" == "testing"
# False, indeed Python is smart

# False
print 1 != 0 and 2 == 1
# 2 is not equal to 1 so it's False

# True
print "test" != "testing"
# True

# False
print "test" == 1
# False

# True -- not(False) is True
print not (True and False)
# True

# False -- not(True) is False
print not ( 1 == 1 and 0 != 1)
# False

# I'd guess True...
print not (10 == 1 or 1000 == 1000)
# False
# from truth table: not(False or True) == False

# False because True or False = True and then not(True) = False
print not (1 != 10 or 3 == 4)
# False!

# Zed needs to stop being so hard on himself.
# not everyone can be a cool guy.
# True
print not ("testing" == "testing" and "Zed" == "Cool Guy")
# True

# uffdah!
# True and True = True
print 1 == 1 and (not ("testing" == 1 or 1 == 0))
# True

# False
print "chunky" == "bacon" and (not ( 3 == 4 or 3 == 3))
# False

# False
print 3 == 3 and (not ("testing" == "testing" or "Pytchon" == "Fun"))
# False
