#!/usr/bin/env python
# indexing_example.py
# run as: python indexing_example.py
# Author: Gavin Schlissel
# 2014_07_06
#
# Demonstrate indexing sequences

# initilize input string
s_name = "Nathaniel I. Krefman"
s_middle_initial = s_name[10] # var[i] accesses the i'th-indexed position in var

# demonstrate slicing methods
s_first = s_name[0:9]
s_last = s_name[13:]

# print strings
print s_name
print s_last
print s_middle_initial
print s_first

# re-build Nathaniel's name
s_simple_name = s_first + ' ' + s_last
s_last_first = s_last + ', ' + s_first + ' ' + s_middle_initial + '.'

# print re-built strings
print s_simple_name
print s_last_first

# demonstrate string interpolation
print "%s, %s %s." % (s_last , s_first , s_middle_initial)

# What would happen if you would run the following line?
# print s_simple_name + 5

# Demonstrate casting between strings and numerical types
s_integer = '5'
s_float = '3.14'

print s_integer + s_float
print s_integer , s_float

i_integer = int(s_integer)
f_float = float(s_float)
print i_integer + f_float
print i_integer , f_float

# demonstrate mixed character-number interpolation
print "%s is %d years old" % (s_simple_name , i_integer)

# Notice what happens when I use a %d to reference a floating point number
print "%s is %f years old" % (s_simple_name , f_float)
print "%s is %d years old" % (s_simple_name , f_float)
print "%s is %f years old" % (s_simple_name , i_integer)

# some examples of padding 
print "%s is %.2f years old" % (s_simple_name , f_float)
print "%s is %05.f years old" % (s_simple_name , f_float)
print "%s is %05.2f years old" % (s_simple_name , f_float)

