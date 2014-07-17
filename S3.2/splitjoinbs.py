#!/usr/bin/env python
# splitjoinbs.py
# run as: python splitjoinbs.py
# Author: Gavin Schlissel
# 2014_07_14
#
# split drills

s_ex = 'Sarah AishaEllahi Jeremy\n'
s_ex = s_ex.split()
print s_ex
s_ex[0:3] = ['Diana' , 'DebbieThurtle' , 'Chris']
print s_ex
s_ex=['\t'.join(s_ex)]
print s_ex

s_ex = 'Sara,Aisha,James'
s_ex = s_ex.split(',')
for i in range(len(s_ex)):
    s_ex[i] = s_ex[i].upper()
s_ex = ['\t'.join(s_ex)]
s_ex[0] = s_ex[0] + '\t'
print s_ex

s_names = 'Aisha,Sarah,James,Mel,Courney,Chris'
l_names = s_names.split(',')

outfile = 'name_combos.txt'
fh = open(outfile , 'w')

for i in range(len(l_names)):
    for j in range(len(l_names)):
        if j == i:
            continue
        else:
            fh.write(l_names[i] + ' ' + l_names[j] + '\n')

fh.close()

rev_outfile = 'name_combos_reverse.txt'
fh = open(outfile , 'r')
rev_fh = open(rev_outfile , 'w')

infile = fh.readlines()
rev_fh.writelines(reversed(infile))

fh.close()
rev_fh.close()
