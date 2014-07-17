#!/usr/bin/env python
# control_flow_examples.py
# run as: python control_flow_examples.py
# Author: Gavin Schlissel
# 2014_07_10
#
# Examples from control flow lecture

#
f_checking_balance = 20.
s_to_eat = 'Nothing'

if f_checking_balance < 10:
    s_to_eat = "Ramen"
    print "If activated"
elif f_checking_balance > 10:
    s_to_eat = "Good ramen"
    print "Elseif activated"
else:
    s_to_eat = "pizza"
    "Else activated"
print "Tonight you are eating %s" % (s_to_eat)


if 10 == 9 or 10 == 10:
    print "Pipe doesnt work"

if 10 == 10 and 9 == 9:
    print "Ampersand doesnt works"

l_ex = ['One' , 'Two' , 'Three' , 'Four']
for ind in l_ex:
    print ind

# note range is zero-indexed
for ind in range(4):
    print ind , l_ex[ind]

# note there is NOT a method to add vectors as there is in R (or scalars to vectors)
l_ex = range(4)
for ind in range(4):
    l_ex[ind] = l_ex[ind]+ind*10
print l_ex



a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
a[0] = 'X'
print a
 
b = a
print b
 
b[1] = 'Y'
print b, "is the value of b"
print a, "is the value of a" # this reallllllly shouldn't be right. this seems like a major python bug.
# This means that there are two names pointing to the same data structure. it also reveals something
# about how the list type is implemented. it is likely a linked list, not continuous in memory.

# b = a
# change b, changes a

# Still with the enumerate function, the x variable is only in the loope scope
print l_ex
for ind , x in enumerate(l_ex):
    print x
    l_ex[ind] = l_ex[ind] + 10
    print x
    print l_ex[ind]
    print
print ind # the loop variables continue to exist after the loop is done!!

print "-------"

stop_case = 10;
while stop_case:
    print stop_case
    stop_case -= 1
    if stop_case == 5:
        break

print "-------"

x = 10
while x >= 0:
    x-=1
    if x % 2 == 0:
        continue
    print x,
print

for y in range(50):
    x = y - 1
    while x > 1:
        if y % x == 0:
            print y , "is not prime"
            break
        x -= 1
        if x == 1:
            print y , "is prime"

a = range(10)
b = []
for aval in a:
    b.append(aval+1)
print b

## LIST COMPREHENSION, THIS WILL BE VERY USEFUL
print [i + 10 for i in a]
a = [i + 10 for i in a]
print a

if "":
    print "empty string is true"
if []:
    print "empty list is true"
if {}:
    print "empty dict is true"
if [[]]:
    print "empty empty list is true"
if 0:
    print "zero is true"
if [0]:
    print "zero in a list is true"
print [0][0] # returns 0
print [1][0] # returns 1
if [0][0]:
    print "2-d 0's are true"
