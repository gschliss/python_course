#!/usr/bin/env python
# ORF_finder.py
# run as: python ORF_finder.py
# Author: Gavin Schlissel
# 2014_07_14
#
# split a fasta file

import sequence_tools
import re

s_file = 'test.fa'
seq_dict = sequence_tools.parse_fasta_to_dict(s_file)

orf_dict = {}

for read in seq_dict.keys():
    m_orfs = re.search('ATG[ATGCN]*TA[AG]' , seq_dict[read])
    if m_orfs:
        if (m_orfs.end() - m_orfs.start()) % 3 == 0:
            orf_dict[read]=seq_dict[read][m_orfs.start():m_orfs.end()]
    m_orfs = re.search('ATG[ATGCN]*TGA' , seq_dict[read])
    if m_orfs:
        if (m_orfs.end() - m_orfs.start()) % 3 == 0:
            orf_dict[read]=seq_dict[read][m_orfs.start():m_orfs.end()]
print orf_dict
