#!/usr/bin/env python
# parse_genes_to_dict.py
# Run as: python parse_genes_to_dict.py
# Author: Gavin Schlissel
# 2014_07_16
#
# Dependencies: gff_parse.py , re.py , numpy.py

import gff_parse
import re
import numpy

s_gff_file = 'e_coli_genes.gff'

# Convert gff file to list
l_lines = gff_parse.gff_to_list(s_gff_file)

# convert gff list to dictionary
d_coli_genes = gff_parse.gff_to_dict(l_lines)

# open operon file and do stuff to it
s_op_file = 'e_coli_operons.tab'
fh_operons = open(s_op_file , 'r')

# open output file to write
s_op_output = 'e_coli_operons.gff'
fh_output = open(s_op_output , 'w')

# Loop over lines
# Read a line of the operon file
s_line = fh_operons.readline().rstrip() # skip first line
l_gff_fields = ['seqname' , 'source' , 'feature' , 'start' , 'end',
                'score' , 'strand' , 'frame' , 'attr']
d_gff_line = {}
gff_parse.empty_dict_values(d_gff_line , l_gff_fields)

while True:
    s_line = fh_operons.readline().rstrip()
    if not s_line: break
    l_line = s_line.split('\t')
    if (l_line[6] != 'TRUE'):
        # if the current line is not an operon
        # flush the buffer
        if not gff_parse.is_empty(d_gff_line):
            gff_parse.flush_gff_buffer(d_gff_line , l_gff_fields, fh_output)
            # empty the buffer
            gff_parse.empty_dict_values(d_gff_line , l_gff_fields)
    else: # operon must be true in here, not clear if new or old operon
        # if the current line is an operon
        if not (re.search(l_line[0] , d_gff_line['attr']) or
                re.search(l_line[1] , d_gff_line['attr'])):
            # if the current line is a new operon
            # flush the buffer
            if not gff_parse.is_empty(d_gff_line):
                gff_parse.flush_gff_buffer(d_gff_line , l_gff_fields , fh_output)
                # empty the buffer
                gff_parse.empty_dict_values(d_gff_line , l_gff_fields)
            # repopulate the buffer with new data
            gff_parse.populate_constant_matter(d_gff_line , d_coli_genes)
            gff_parse.populate_variable_matter(d_gff_line , d_coli_genes , l_line)
        else:
            # if the current line continues the previous buffer
            # add to the buffer
            gff_parse.add_to_dict_entry(d_gff_line , d_coli_genes,l_line)

