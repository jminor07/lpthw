days = "mandaag dinsdag woensdag donderdag vrijdag zaterdag zondag"

# have to use three double quotes otherwise the line would be too long for PEP 8.
# the \n is the line break.
months = """januari \n februari \n maart \n april \n mei \n juni \n juli \n augustus \n september \n oktober
 november \n december \n"""

print "Here are the days(in Dutch):", days
print "Here are the months(in Dutch):", months

# we can print multiple lines using this method.
print """ There is something funny going on here.
 with the three double quotes.
 We'll be able to type as much as we like.
 Even four lines if we want five, or six.
 """
