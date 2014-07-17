#!/usr/bin/env python
# dict_of_lists.py
# run as: python dict_of_lists.py
# Author: Gavin Schlissel
# 2014_07_14
#
# Make a dict of lists, just to prove that we can

d_data = {'Human':[] , 'Mouse':[] , 'Rat':[]}
d_data['Human'].append(5)
d_data['Human'].append(4)
d_data['Human'].append(6)
d_data['Human'].append(7)
d_data['Mouse'].append(8)
d_data['Mouse'].append(12)
d_data['Mouse'].append(11)
d_data['Mouse'].append(14)
d_data['Rat'].append(10)
d_data['Rat'].append(11)
d_data['Rat'].append(13)
d_data['Rat'].append(15)
print d_data

d_data = {'Human':[5,4,6,7] , 'Mouse':[8,12,11,14] , 'Rat':[10,11,13,15]}
print d_data
