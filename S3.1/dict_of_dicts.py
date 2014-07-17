#!/usr/bin/env python
# dict_of_dicts.py
# run as: python dict_of_dicts.py
# Author: Gavin Schlissel
# 2014_07_14
#
# Make a dictionary of dictionaries, just to prove that we can

d_genes = {
    'd_humanGenes' : {
        "Tallness":"AATAGCAG",
        "Smartness":"TGACGCA"},
    'd_mouseGenes' : {
        "Fuzziness":"ATCGATCG",
        "BeadyEyes":"GTACGTAC"},
    'd_ratGenes' : {
        "Fuzziness":"GGATCCC",
        "BiggerThanMouse":"AAAAGGGAAA"}
    }

# print the human gene names
print d_genes['d_humanGenes'].keys()

# print the sequence of the fuzziness genes
print d_genes['d_mouseGenes']['Fuzziness']
print d_genes['d_ratGenes']['Fuzziness']

# Or another way, without manually telling which organism to look in
print '-------- alternative approach --------'
for i in range(len(d_genes.keys())):
    if 'Fuzziness' in d_genes[d_genes.keys()[i]].keys():
        print d_genes[d_genes.keys()[i]]['Fuzziness']

print '----------'
print 'The third nucleotide of the human tallness gene is %s' % (
    d_genes['d_humanGenes']['Tallness'][2])
