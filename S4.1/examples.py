#!/usr/bin/env python
# examples.py
# run as: python examples.py
# Author: Gavin Schlissel
# 2014_07_14
#
# function definition examples

def hello(name):
    greeting = 'Hello, %s' % (name)
    return greeting

# functions do have access to the buffer
def hello_print(name):
    print 'Hello, %s' % (name)
    return None

print hello('gavin')
print hello_print('gavin')


import sys
l_cmdline = sys.argv
print l_cmdline

import math
x = 9
print math.log(9)

# useful, i expect
import collections
my_genera = ['Helicobacter', 'Escherichia', 'Lactobacillus', 'Lactobacillus', 'Oryza',
             'Wolbachia', 'Oryza', 'Rattus', 'Lactobacillus', 'Drosophila']
c = collections.Counter(my_genera)
print c



import collections

my_species_list = [('Helicobacter','pylori'), ('Escherichia','coli'),
              ('Lactobacillus', 'helveticus'), ('Lactobacillus', 'acidophilus'),
              ('Oryza', 'sativa'), ('Wolbachia', 'pipientis'), ('Oryza', 'glabberima'),
              ('Rattus', 'norvegicus'), ('Lactobacillus','casei'),
              ('Drosophila','melanogaster')]

d = collections.defaultdict(list)

for genus , species in my_species_list:
    d[genus].append(species)
print d

# import imports things like modules
# from MODULE import FUNCTION lets you use function without prefix
# from MODULE import * imports all functions (wildcards allowed in funciton import)



