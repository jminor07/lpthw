# symbol review

# and
# logical and
a = True and False

# as
# paired with-as
with x as y: pass

# assert
# ensure that something is true.
assert False, "error!"

# break
# stop the loop immediately
while True: break

# class
# create a class
# class Person(object)

# continue
# don't process more of the loop, do it again.
while True: continue

# def
# define a function
# def foo(): return "bar"

# del
# delete from a dictionary
# del X[Y]

# elif
# else if condition
# if: X; elif: Y; else: J

# else
# else condition
# if: X; elif: Y; else: J

# except
# if an exception happens do this
# except ValueError, e: print e

# exec
# run string as Python
# exec 'print "hello"'

# finally
# do this no matter what
# finally: pass

# for
# iterating over something
# for X in Y: pass

# from
# importing from a library
# import X from Y

# global
# define a global variable
# global X

# if
# if condition
# if: X; elif: Y; else: J

# import
# imoprt a library
# import os

# in
# used in conjunction of a for loop
# for X in Y: pass

# is
# tests for equality
# 1 is 1 == True

# lambda
# creates a small function
s = lambda y: y ** y; s(3)

# not
# logical not
# not True == False

# or
# logical or
# True or False == True

# pass
# this block is empty
# def empty(): pass

# print
# print the string
# print 'this string'

# raise
# raise an exception when things go wrong.
# raise ValueError("No")

# return
# exit the function with a return value
# def X(): return Y

# try
# try this block of code and it it doesn't work then go to to 'except' section
# try: pass

# while
# while loop
# while X: pass

# with
# with an expression as a variable do
# with X as Y: pass

# yield
# pause here and return to caller.
# def X(): yield Y; X().next()

# ****** Data Types ******

# True
# True boolean value

# False
# False boolean value

# None
# represents nothing

# string
# stores text

# numbers
# stores integers

# floats
# stores decimals

# lists
# stores an array

# dictionary
# stores keys=mapping

# ****** String Escape sequence ******

# \\ backslash
# \' single quote
# \" double quote
# \a Bell
# \b backspace
# \f form feed
# \n newline
# \r carriage
# \t tab
# \v vertical tab

# ********** String Formats

# %d
# Decimal integers (not floating point).
# "%d" % 45 == '45'

# %i Same as %d.
# "%i" % 45 == '45'


# %o
# Octal number.
# "%o" % 1000 == '1750'


# %u
# Unsigned decimal.
# "%u" % -1000 == '-1000'

# %x
# Hexadecimal lowercase.
# "%x" % 1000 == '3e8'

# %X
# Hexadecimal uppercase.
# "%X" % 1000 == '3E8'

# %e
# Exponential notation, lowercase 'e'.
# "%e" % 1000 == '1.000000e+03'

# %E
# Exponential notation, uppercase 'E'.
# "%E" % 1000 == '1.000000E+03'

# %f
# Floating point real number.
# "%f" % 10.34 == '10.340000'

# %F
# Same as %f.
# "%F" % 10.34 == '10.340000'

# %g
# Either %f or %e, whichever is shorter.
# "%g" % 10.34 == '10.34'

# %G
# Same as %g but uppercase.
# "%G" % 10.34 == '10.34'

# %c
# Character format.
# "%c" % 34 == '"'

# %r
# Repr format (debugging format).
# "%r" % int == "<type 'int'>"

# %s
# String format.
# "%s there" % 'hi' == 'hi there'

# %%
# A percent sign.
# "%g%%" % 10.34 == '10.34%'



# ************** Operators **************

# +
# Addition
# 2 + 4 == 6
# -
# Subtraction
# 2 - 4 == -2

# *
# Multiplication
# 2 * 4 == 8

# **
# Power of
# 2 ** 4 == 16

# /
# Division
# 2 / 4.0 == 0.5

# //
# Floor division
# 2 // 4.0 == 0.0

# %
# String interpolate or modulus
# 2 % 4 == 2

# <
# Less than
# 4 < 4 == False

# >
# Greater than
# 4 > 4 == False

# <=
# Less than equal
# 4 <= 4 == True

# >=
# Greater than equal
# 4 >= 4 == True

# ==
# Equal
# 4 == 5 == False

# !=
# Not equal
# 4 != 5 == True

# <>
# Not equal
# 4 <> 5 == True

# ( )
# Parenthesis
# len('hi') == 2

# [ ]
# List brackets
# [1,3,4]

# { }
# Dict curly braces
# {'x': 5, 'y': 10}

# @
# At (decorators)
# @classmethod

# ,
# Comma
# range(0, 10)

# :
# Colon
# def X():

# .
# Dot
# self.x = 10

# =
# Assign equal
# x = 10

# ;
# semi-colon
# print "hi"; print "there"

# +=
# Add and assign
# x = 1; x += 2

# -=
# Subtract and assign
# x = 1; x -= 2

# *=
# Multiply and assign
# x = 1; x *= 2

# /=
# Divide and assign
# x = 1; x /= 2

# //=
# Floor divide and assign
# x = 1; x //= 2

# %=
# Modulus assign
# x = 1; x %= 2
# **=
# Power assign
# x = 1; x **= 2
