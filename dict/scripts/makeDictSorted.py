#!/usr/bin/python3
import pandas as pd
import collections
import sys

# python makeDictSorted.py
# or add input filename: python makeDictSorted.py input.txt

if len(sys.argv) < 2:
    # full_name = "HP3_10-15.txt"
    full_name = 'file.txt'
else:
    full_name = sys.argv[1]

#full_name = "HP3_10-15.txt"
#data = pd.read_csv(full_name,skiprows=1,sep='\t')
#data = pd.read_csv(full_name,skiprows=1,sep='\t',usecols=[0,2],header=None)  # !!!!
data = pd.read_csv(full_name,skiprows=1,sep='\t',usecols=[0,1],header=None)  # !!!!
data.sort_values(0, axis=0, ascending=True, inplace=True)
data = data.reset_index(drop=True) # Reset index after sorting ..........
data.to_csv('file.txt',encoding='utf-8-sig',sep='\t', header=None, index=None)

words = data[0].to_list()
duplicates = [item for item, count in collections.Counter(words).items() if count > 1]

if len(duplicates) > 0:
    print("\nDuplicates detected:")
else:
    print("\nNo duplicates detected")

for item in duplicates:
    print(data.loc[data[0] == item])