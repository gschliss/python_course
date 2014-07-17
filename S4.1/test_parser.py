#!/usr/bin/env python
# test_parser.py
# run as: python test_parser.py
# Author: Gavin Schlissel
# 2014_07_14
#
# split a fasta file

import sequence_tools

s_file = '/Users/gavinschlissel/Dropbox/Lab/JR_lab/\
python_course/PythonCourse/assignments/S5.1/test.fa.gz'
seq_dict = sequence_tools.parse_fasta_to_dict(s_file)

if seq_dict: # make sure seq_dict is not zero
#    print seq_dict
    print seq_dict['gene3']

else:
    print "############# ERROR ##############"
