#!/usr/bin/env python
# fasta_parser.py
# run as: python fasta_parser.py
# Author: Gavin Schlissel
# 2014_07_10
#
# parse a fasta file into a dictionary

d_seqs = {}
l_keys = []
l_vals = []

i_num_seen = 0

# accept up to a thousand lines of fasta
while i_num_seen < 1000:
    s_input = raw_input("Input a fasta line ")
    # if user inputs nothing, stop the loop and print what's been entered
    if len(s_input) == 0:
        break
    # If the user starts a new fasta entry, store the new key
    elif s_input[0] == '>':
        i_num_seen += 1
        if i_num_seen > 6: # This controls how many sequences the script wants to see
            break
        l_keys.append(s_input[1:])
    else
        if i_num_seen == 0:
            continue
        # handle making new entires in the 'values' list
        elif i_num_seen > len(l_vals):
            l_vals.append(s_input)
        # add to a value list for entries that span multiple inputs
        else:
            l_vals[(i_num_seen-1)] = str(l_vals[(i_num_seen-1)]) + s_input

for i , k in enumerate(l_keys):
    d_seqs[k] = l_vals[i]

print "You entered the sequences: "
for k , v in d_seqs.items():
    print k , "\t" , v

