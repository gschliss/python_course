#!/usr/bin/env python
# S2.1_exercises.py
# run as: python S2.1_exercises.py
# Author: Gavin Schlissel
# 2014_07_13
#
# List exercises

# concatenate two lists
l_1 = [1,2,3] + [4,5,6]

# print the list
print l_1
# print the list
print l_1[:] 
# print until the first element (print empty list)
print l_1[:0]
# print the third-from-the-end element
print l_1[-2]
# print from the third-from-end element to the last element
print l_1[-2:]
# notice print l_1[:1] gives a list, but print l_1[0] gives an int

# reverse the list
l_1.reverse()
print l_1

# sort the list low-to-high
l_1.sort()
print l_1

# find the index of the entry with value 4
idx = l_1.index(4)
print idx

# make a dictionary with entries a=1, b=2, and withdraw the value tagged by key 'b'
print {'a':1 , 'b':2}['b']

# make a dictionary with etnries x=1 , y=2, z=3
d_1 = {'x':1 , 'y':2 , 'z':3}
# add a new key 'w' with value 0
d_1['w'] = 0
# add the value corresponding to key 'x' to the value corresponding to key 'w' and print the result
print d_1['x'] + d_1['w']

# print the keys stored in dictionary d_1
print d_1.keys()

# print the values stored in dictory d_1 in the order of the corresponding keys
print d_1.values()

# print true if d_1 has value 'z'
print d_1.has_key('z')

