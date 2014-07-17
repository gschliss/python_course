#!/usr/bin/env python

list_of_letters = ['a', 'a', 'b', 'c','c','c','d','e']
print 'ORIGINAL'
set_of_letters = set(list_of_letters)
print set_of_letters

print 'DISCARD'
set_of_letters.discard('q')
print set_of_letters

print 'REMOVE'
set_of_letters.remove('q')
print set_of_letters
