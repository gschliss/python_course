#!/usr/bin/env python
# asst.py
# run as: python asst.py
# Author: Gavin Schlissel
# 2014_07_14
#
# function definition examples

# User passes a numeric type
# function returns 2* user input
def doubleme(x):
    return x*2

# User pases two numeric types
# function returns their product
def multiplyme(x,y):
    return x*y

# User passes a list of numeric variables
# function returns the product of the first two entries
def multiplyme_list(xs):
    return xs[0] * xs[1]


'''
print doubleme(5)
print multiplyme(5,10)
print multiplyme_list([5,10])

def doubleme(x):
    print x*2
    return 0
def multiplyme(x,y):
    print x*y
    return 0
def multiplyme_list(xs):
    print xs[0] * xs[1]
    return 0

doubleme(5)
multiplyme(5,10)
multiplyme_list([5,10])
''
