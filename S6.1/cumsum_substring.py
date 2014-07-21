import re
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as ppt
import matplotlib as mp

input_string = 'ATGCATGCATGC'

gen = list(SeqIO.parse('/Users/gavinschlissel/Dropbox/Lab/JR_lab/python_course/PythonCourse/assignments/S1.1/yeast_genome_fastas/yeast_genome.fa' , 'fasta'))
seq = str(gen[0].seq)


a_hits = re.finditer('[CT]' , seq)
l_hits = [a.start() for a in a_hits]


print type(l_hits)

hits_diff = np.ediff1d(l_hits)

hist_diff = np.histogram(np.array(hits_diff))

ppt.hist(hits_diff,100)
ppt.show()
