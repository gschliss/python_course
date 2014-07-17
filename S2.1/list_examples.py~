#!/usr/bin/env python
# list_examples.py
# run as: python list_examples.py
# Author: Gavin Schlissel
# 2014_07_10
#
# Demonstrate basic list operations


l_one = ['a' , 'b' , 'c']
l_two = ['d' , 'e' , 'f']


print l_one
print l_two
print l_one + l_two
l_one.append(l_two[0]) # notice this operation updates the value of the calling object l_one
print l_one
l_one.extend(l_two) # notice this operation updates the value of the calling object l_one
print l_one
l_one.insert(3 , 'NULL')
print l_one
l_one[3] = "not_null"
print l_one

del l_one[3]
print l_one
l_one.pop()
print l_one

# This may be less memory efficient than the del method, 
# depending on how the del method is implemented
l_one = l_one[:-2] 
print l_one

l_one = 4*[0]
print l_one

l_one[0] = 0
l_one[1] = 1
l_one[2] = 2
l_one[3] = 3
print l_one

l_one.reverse()
print l_one

l_two = sorted(l_one)
print l_two

l_one.sort()
print l_one

print "Length = " , len(l_one)
print "Max = " , max(l_one)
print "Min = " , min(l_one)

for x in l_one: print x

idx = l_one.index(0)
print idx

print "-------------------"

t_SNP = ("chrII" , "378445")
print type(t_SNP)

for i in t_SNP: print i

# Doesn't work with tuples
# t_SNP[0] = '1'

# Coerce to a list to let us edit it
t_SNP = list(t_SNP)
t_SNP[0] = 'FOO'
print t_SNP

print "------------------"

names = {"Gavin" : "Schlissel" , "Brian" : "Castellano" , "Elijah" : "Mena" , "Addison" : "Wright"}
print names
print names['Gavin']
# print names['Schlissel'] # Note you can't lookup by value, only by key

names['Kelsey'] = "Van Dalfsen"
print names

names.update({"Sean" : "Higgins"})
print names

del names['Kelsey']
print names

names['Sean'] = 'foo-bar'
print names

# Notice this does NOT slice at 0, it adds a key-value pair with key 0, value "poop"
names[0] = 'poop'
print names
del names[0]

print names.keys()
print names.values()

if 'Gavin' in names: print names['Gavin'] 
else: print "There's no Gavin"
if 'Kelsey' in names: print names['Kelsey'] 
else: print "There's no Kelsey"

