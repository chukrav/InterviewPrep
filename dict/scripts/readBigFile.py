import pandas as pd
import sys
import re

with open('huge_file.txt','r') as file:                                                                                                                                                                                                                                             
    for line in file:
        if 'Subfile:' in line:
            print(line, end='')
            
file.close()

# nums = [float(n) for n in line.split()]  # split - convert to float
#a = nm.zeros([2, 2], dtype = float)
#>>> print(a)
#[[0. 0.]
# [0. 0.]]
# a[:,1] = 2
#>>> a
#array([[0., 2.],
#       [0., 2.]])