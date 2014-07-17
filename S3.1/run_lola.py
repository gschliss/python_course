#!/usr/bin/env python
# run_lola.py
# run as: python run_lola.py
# Author: Gavin Schlissel
# 2014_07_14
#
# play with one of Python's funnier attributes...

run1 = [2,3,4,5]
run2 = [2,2,4,5]
run3 = [3,3,4,6]

l_data = [run1 , run2 , run3]

l_data[1][1]=6000 # THIS UPDATES THE ORIGINAL RUN2 VARIABLE!!!!
print l_data
print run2

# this de-references the run lists, and copies the contents
l_data = [run1[:] , run2[:] , run3[:]]

l_data[1][1] = 20
print run2
print l_data
