#!/usr/bin/env python
# rome.py
# run as: python rome.py
# Author: Gavin Schlissel
# 2014_07_10
#
# rewrite the code in good python

# L = [1,2,4,8,16,32,64]
L = []
for i in range(7):
    L.append(2**i)
print L

L = [2 ** i for i in range(7)]
print L

x = 5
 
found = i = 0
#while not found and i < len(L):
#    #check if 2 to the power
#    #of x is in the list
#    if 2 ** x == L[i]:
#        found = 1
#    else:
#        i = i+1
#if found:
#    print 'at index', i
#else:
#    print x, 'not found'

print "--------"

# no loop at all!
if 2**x in L:
    idx = L.index(2**x)
    print "At index ", idx
else:
    print x , "not found"

print "-------"

found = i = 0
for i,val in enumerate(L):
    if 2**x == val:
        print "At index " , i
        found = 1
if not found:
    print x , "not found"


print "-------"
found = i = 0
while not found and i < len(L):
    if 2**x == L[i]:
        print "At index" , i
        break
    else:
        i+=1
else:
    print x , "not found"
