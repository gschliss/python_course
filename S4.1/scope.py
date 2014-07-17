#!/usr/bin/env python
# scope.py
# run as: python scope.py
# Author: Gavin Schlissel
# 2014_07_14
#
# function definition examples

def increment(x):
    x+=1

x = 5
print x
increment(x)
print x


def update(inp):
    inp[0]='x'

ip = ['a' , 'b' , 'c']
print ip
update(ip)
print ip


def update(inp):
    inp['x']='y'

ip = {'a':'A' , 'b':'B'}
print ip
update(ip)
print ip

## Functions CAN update lists and definiions without returning them, because
# the underlying implementation is a pointer


