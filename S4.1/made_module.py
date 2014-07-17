#!/usr/bin/env python
# make_module.py
# run as: python make_module.py
# Author: Gavin Schlissel
# 2014_07_14
#
# examples lecture 3.2

from S41asst1 import doubleme

print doubleme(6)

import S41asst1
print S41asst1.doubleme(7)
print S41asst1.multiplyme_list([3,6])

print 'hello'
