#!/usr/bin/env python
# split_drills.py
# run as: python split_drills.py
# Author: Gavin Schlissel
# 2014_07_14
#
# split drills

s_ex = "Humpty Dumpty sat on a wall"
print s_ex.split()

s_ex = "Humpty Dumpty had a great fall"
print s_ex.split(' great ')

s_ex = "All the King's horses"
print s_ex.rsplit('s',2)

s_ex = "And all the king's men"
print s_ex.split('l')

s_ex = "Couldn't put humpty together again"
print [(s_ex.rsplit(' ',1)[1])]

