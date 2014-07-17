#!/usr/bin/env python
# gene_finder.py
# run as: python gene_finder.py
# Author: Gavin Schlissel
# 2014_07_10
#
# Identify a start codon in a 6bp user input

# accept user input
while 1:
    s_input = raw_input("Input a string of ATGCN that is 6 basepairs long ")
    if len(s_input) != 6:
        s_input = raw_input("That last one wasn't 6bp long. Please enter a string that is 6bp long ")
    else:
        break

# check to see if there is an ORF in any frame, 
# and oputput the position of the start codon if one is found
b_ORF_found = 0
for offset in range(4):
    if s_input[(0+offset):(3+offset)] == "ATG":
        print "There is an ORF starting at position # %i (1-indexed)" % (offset + 1)
        b_ORF_found += 1

# return if there is no ORF
if not b_ORF_found:
    print -1
