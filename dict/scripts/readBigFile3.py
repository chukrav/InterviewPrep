import pandas as pd
import sys
import re
import numpy as np

#with open('small_file.txt','r') as file:                                                                                                                                                                                                                                             
#    for line in file:
#        if 'Subfile:' in line:
#            print(line)
#              
#file.close()

# nums = [float(n) for n in line.split()]  # split - convert to float
#a = nm.zeros([2, 2], dtype = float)
#>>> print(a)
#[[0. 0.]
# [0. 0.]]
# a[:,1] = 2
#>>> a
#array([[0., 2.],
#       [0., 2.]])

pattDataA = '(FLOAT)DataA'
pattDataB = '(FLOAT)DataB'

i = 0   # Row
j = 0   # Column
COLLECT_DATA = False
GET_ARRAY_SIZE = True
FILE_WIDTH = 200
FILE_HEIGHT = 0

dataA = np.array([])  # Empty array
dataB = np.array([])  # Empty array
data = np.array([])  # Empty array
wlA = np.array([])  # Empty array
wlB = np.array([])  # Empty array
wl = np.array([])  # Empty array

# data = np.zeros([FILE_HEIGHT, FILE_WIDTH], dtype=float)
# wl = np.zeros([FILE_HEIGHT,1],dtype=float)
last_subfile = ''

with open('small_file.txt','r') as file:
    for line in file:
        if 'Subfile:' in line:
            # print(line)
            last_subfile = line
        
        try:
            if COLLECT_DATA == True:
                nums = line.split()
                data[i,j] = float(nums[1])
                if wl[0,0] == 0.0:
                    wl[i,0] = float(nums[0])
                    
                i = i + 1
        except:
            COLLECT_DATA = False
            j = j+1
            if j > FILE_WIDTH:
                j = 0;
                data = np.zeros([FILE_HEIGHT, FILE_WIDTH], dtype=float)
                print('New file started')
            
        if 'Wavelength' in line:
            COLLECT_DATA = True
            i = 0
			if data.size == 0:
				vals = line.split()
				FILE_HEIGHT = int(vals[-1].split('pts')[0])
				data = np.zeros([FILE_HEIGHT,FILE_WIDTH],dtype=float)
				wl = np.zeros([FILE_HEIGHT,1],dtype=float)
				if dataA == 0:
					dataA = data
					wlA = wl
				elif dataB == 0:
					dataB = data;
					wlB = wl
				
			
		if pattDataA in line:
			data = dataA
			wl = wlA
			
		if if pattDataB in line:
			data = dataB
			wl = wlB
            
file.close()

print(np.shape(data))
print(np.shape(wl))
print(last_subfile)

print(data[:6,:])
print('----------------------')
print(data[-6:,:])
print('---------wl-----------')
print(wl[:6,:])
print(wl[-6:,:])

#import pandas as pd
#from openpyxl import load_workbook
#
#fn = r'C:\Temp\.data\doc.xlsx'
#
#df = pd.read_excel(fn, header=None)
#df2 = pd.DataFrame({'Data': [13, 24, 35, 46]})
#
#writer = pd.ExcelWriter(fn, engine='openpyxl')
#book = load_workbook(fn)
#writer.book = book
#writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
#
#df.to_excel(writer, sheet_name='Sheet1', header=None, index=False)
#df2.to_excel(writer, sheet_name='Sheet1', header=None, index=False,
#             startcol=7,startrow=6)
#
#writer.save()
#--------------------------------------
# # Create a Pandas dataframe from the data.
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1',startcol=7,startrow=6)

# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
# line: '  Wavelength [1.0, 6.0] (um) 1558pts'
# vals = line.split()
# int(vals[-1].split('pts')[0])  --> 1558 as int
# tdata = np.array([])  # Empty array
# tdata.size  # --> 0




