#!/usr/bin/env python
# neighbors.py
# run as: python neighbors.py
# Author: Gavin Schlissel
# 2014_07_13
#
# List exercises: Get to know your neighbors

d_labs = {'Mary':'Ingolia' , 'Mark':'Unal' , 'Luke':'Brar' , 'Joseph':'Zoncu'}
print d_labs

# print Mary's lab value
print d_labs['Mary']

# This gives a run-time error, because Terry is not a key
# print d_labs['Terry']

# Add Terry to the dictionary and print the new dictionary
d_labs['Terry'] = 'Alber'
print d_labs

print("A major difference between lists and dictionaries is that dictionaries "+
      "add a value when you try to assign to a key that doesn't yet exist." + 
      " In a list, you can't assign to an index that doesn't exist.")


