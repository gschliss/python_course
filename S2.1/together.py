#!/usr/bin/env python
# together.py
# run as: python together.py
# Author: Gavin Schlissel
# 2014_07_13
#
# List exercises: Pulling it all together

#initialize list to store sequence
protSeq = []
#open pdb file
f1 = open('2Q6H.pdb', 'r')
#loop over lines in file
for next in f1:
    #identify lines that contain sequences
    if next[:6] == 'SEQRES':
        #strip away white space and
        #convert line into list
        line = next.strip().split()
        #delete descriptor information
        #at beginning of each line
        del line[:4]
        #loop over amino acids in line
        for aa in line:
            #add to sequence list
            protSeq.append(aa)
#close file
f1.close()

# print protSeq
# print type(protSeq)

print "The protein contains %i residues." % (len(protSeq))

d_aas = {'ALA':0 , 'ARG':0 , 'ASN':0 , 'ASP':0 , 'CYS':0 , 'GLU':0 , 'GLN':0 ,
         'GLY':0 , 'HIS':0 , 'ILE':0 , 'LEU':0 , 'LYS':0 , 'MET':0 , 'PHE':0 , 
         'PRO':0 , 'SER':0 , 'THR':0 , 'TRP':0 , 'TYR':0 , 'VAL':0}
# print type(d_aas) # make sure you made a dictionary correctly!

# iterate over the protein sequence, and add one to the aa count for
# each aa encountered in the protein sequence
for res in protSeq:
    d_aas[res] += 1

# iterate over the alphabetically odered keys, and print each AA's 
# dictionary value
for keys in sorted(d_aas):
    print keys , d_aas[keys]

print "------------"

# The set approach prevents us having to explicitly list all of the amino acids to 
# count in the protein. An amino acid will only appear in the set if it appears in
# the protein.

s_aas = set(protSeq) # identify all unique aa's
d_aas = {}
# initialize the dictionary with all amino acids that occur in the protein
for res in s_aas:
    d_aas[res] = 0

for res in protSeq:
    d_aas[res] += 1

for res in sorted(d_aas):
    print res, " " , d_aas[res]

    

