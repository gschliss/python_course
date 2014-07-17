#!/usr/bin/env python
# know_TAs.py
# run as: python know_TAs.py
# Author: Gavin Schlissel
# 2014_07_13
#
# List exercises: Get to know your TAs

l_tas = ['Mary' , 'Mark' , 'Luke' , 'Joseph'] # i forget the rest of them...

# ghetto way to print the list
print "The TAs are " , l_tas

# print "Accessing an elemenet that is out-of-bounds returns a run-time error" , l_tas[7]

print "Accessing a slice that extends beyond the end of a list returns as much of the slice as possible" , l_tas[2:6]

l_tas[3:1] = [1,2,3]
print "editing a slice in reverse works just fine, but the assignment goes in forwards " , l_tas
print "And you can't print in reverse " , l_tas[3:1]

# reset the list
l_tas = ['Mary' , 'Mark' , 'Luke' , 'Joseph'] # i forget the rest of them...
# add myself to the middle
l_tas[2:2] = ["Gavin"]
print l_tas
l_tas.insert(2, "Addison")
print l_tas

# doing it this way replaces everything indexed between 3 and 5 with a single item, Gavin
# so the list shrinks in this case.
l_tas[3:5] = ["Gavin"]
print l_tas

# Note this doesn't work, beause .insert can only handle single integer indicies
# l_tas.insert([2:5] , 'Addison')
# print l_tas


