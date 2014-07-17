#!/usr/bin/env python
# math_examples.py
# run as: python string_examples.py
# Author: Gavin Schlissel
# 2014_07_06
# 
# Demonstrate basic string operations

# initialize string variables
s_challenge = 'Hello , "world," if that is your real name'
s_answer = "That's World to you, buddy"

print s_challenge
print s_answer

# Display the same output using a different approach
s_compact = '''Hello , "world," if that is your real name
That's World to you, buddy'''

print s_compact


# Demonsrate escape characters in strings

s_1 = 'some\thing is missing'
print s_1
s_2 = 'somethi/ng is broken'
print s_2
s_3 = '''something that will drive you b\an\an\as'''
print s_3
s_4 = r'\a solu\tio\n'
print s_4
s_5 = '\\another solu\\tio\\n'
print s_5

