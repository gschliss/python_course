#!/usr/bin/env python
# list_of_lists.py
# run as: python list_of_lists.py
# Author: Gavin Schlissel
# 2014_07_14
#
# Make a list of lists, just to prove that we can

l_data = []

for i in range(3):
    l_data.append([])

# populate the data
idx = 0
num = [2,3,5,5,2,2,4,5,3,3,4,6]
for i in range(len(l_data)):
    for t in range(4):
        l_data[i].append(num[idx])
        idx += 1
print l_data

print '--------------'

l_data = [[],[],[]]
# populate the data
idx = 0
num = [2,3,5,5,2,2,4,5,3,3,4,6]
for i in range(len(l_data)):
    for t in range(4):
        l_data[i].append(num[idx])
        idx += 1
print l_data

print '--------------'
l_data = [[2,3,4,5],[2,2,4,5],[3,3,4,6]]
print l_data
