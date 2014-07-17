#!/usr/bin/env python
# examples.py
# run as: python examples.py
# Author: Gavin Schlissel
# 2014_07_14
#
# examples lecture 3.2

c_delim = ','
s_string = 'Hello, my name is, what?'

l_stringsplit = s_string.split(c_delim)

print l_stringsplit


c_delim = ' '
l_stringsplit = s_string.split(c_delim)
print l_stringsplit

l_stringsplit = list(s_string)
print l_stringsplit

s_string = "Written"
l_stringsplit = s_string.split('t')
print l_stringsplit

s_string = "    one     two  three four   five   "
l_stringsplit = s_string.split() #whitespace is the default splitting token
print l_stringsplit

# a way to split by a regex
import re
l_stringsplit = re.split("[ ]+" , s_string)
print l_stringsplit

s_string = 'Hello, my name is, what?'
l_stringpart = s_string.partition(',')
print type(l_stringpart)
print l_stringpart

l_stringpart = s_string.partition("name")
print l_stringpart

l_stringpart = s_string.partition('none')
print l_stringpart

broken = ['hu','m','pty',' du','mpty']
all_the_kings_horses = 'n~n*^'
all_the_kings_men = '>+0'
first_try = all_the_kings_horses.join(broken)
second_try = all_the_kings_men.join(broken)
print first_try
print second_try

print ''.join(broken)
print ' '.join(broken)
print 'X'.join(broken)


print 'abcd'.startswith('a')
print 'abcd'.endswith('a')
print 'abcd'.endswith('d')

# same thing with RE.
# note the re.match function only checks beginning of stiring
import re
print re.search('^a','abcd') # returns a matchObject, which i don't quite understand
print re.search('^a','abcd') != 0
print re.search('d$','abcd') != 0

print 'abcd'.find('^a') # find only matches literals
print 'abcd'.find('b') # returns the position of the literal,
# or -1 if it is not matched

print 'abacada'.find('a')  # only returns the lowest index

print 'JohnPaulRingoGeorge'.replace('John','Yoko')


blast_hit = 'ACTGTCAGTACGTAGCATCGAaaatCGATCGACTGAatacgatCG'
if ( blast_hit.isupper() ):
    pass
else:
    blast_hit = blast_hit.upper()
    print blast_hit

# This must not use ~ as an abbreviation for the home directory.
# I'm not clear what rules apply
s_filename = '/Users/gavinschlissel/Dropbox/Lab/JR_lab/python_course/\
PythonCourse/assignments/S3.2/example_text.txt'
fh = open(s_filename , 'r')

print fh.readline() # reads one line
#print fh.readlines() # reads the whole file, returns a list of lines

# .strip() gets rid of trailing whitespace, including trailing \n character
print fh.readline().strip()



fh.close()
