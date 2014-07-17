#!/usr/bin/env python
# hello_norcal.py
# run as: ./hello_norcal.py
# Author: Gavin Schlissel , gschliss@gmail.com
# 
# Demonstrate variable types
#

s = 'hella world' # string type
i = 42 # integer type
f = 3.14159 # floating-point type

# print the variables, and their types separated by blank lines
print s
print "The varible s is of type" , type(s) , "\n"

print i
print "The variable i is of type" , type(i) , "\n"

print f
print "The variable f is of type" , type(f) , "\n"


# swap the value of variablese in s and i and print the new values of the variables and their types
foo = s
s = i
i = foo

print s
print "The varible s is of type" , type(s) , "\n"

print i
print "The variable i is of type" , type(i) , "\n"

