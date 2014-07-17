#!/usr/bin/env python
# rev_comp.py
# run as: python rev_comp.py
# Author: Gavin Schlissel
# 2014_07_14
#
# function definition examples

import re

# Take an input string and return the reverse-complement of that string
# as a string.
# Depends on the module re
def reverse_complement(input):
    input = input.upper()
    input = re.sub('[^ATGCN]','N',input) # replace any non ATGCN characters with N
    input = list(input)
    input.reverse()
    input = ''.join(input)
    input = re.sub('A' , 't' , input)
    input = re.sub('T' , 'a' , input)
    input = re.sub('G' , 'c' , input)
    input = re.sub('C' , 'g' , input)
    input = input.upper()
    return input

out = reverse_complement('atcgactaccataggga412tcaEND')
print out

