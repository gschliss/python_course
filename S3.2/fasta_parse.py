#!/usr/bin/env python
# fasta_parse.py
# run as: python fasta_parse.py
# Author: Gavin Schlissel
# 2014_07_14
#
# split a fasta file

s_file = 'fasta_ex.txt'
fh_fasta = open(s_file , 'r')
d_genes = {}

# requires the first line to be a gene name, start with >
while True:
    n = fh_fasta.readline()
    n = n.strip()
    if not n:
        break
    else:
        if n.startswith('>'):
            n = n.split('>')
            s_gene_name = ''.join(n[1:])
            d_genes[s_gene_name]=''
        else:
            d_genes[s_gene_name] = d_genes[s_gene_name] + n

for gene in sorted(d_genes):
    print gene , ' ' , d_genes[gene]
