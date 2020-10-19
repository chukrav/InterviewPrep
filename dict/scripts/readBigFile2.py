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

i = 0   # Row
j = 0   # Column
COLLECT_DATA = False
FILE_WIDTH = 200
FILE_HEIGHT = 1000

data = np.zeros([FILE_HEIGHT, FILE_WIDTH], dtype=float)
wl = np.zeros([FILE_HEIGHT,1],dtype=float)
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
# >>> import pandas as pd
# >>> import numpy as np
# >>> import xlsxwriter
# >>> arr = np.random.rand(1000,500)
# >>> df = pd.DataFrame(arr)
# >>> writer = pd.ExcelWriter('pandas_simple2.xlsx', engine='xlsxwriter')
# >>> df.to_excel(writer, sheet_name='Sheet1')
# >>> writer.save()
# >>> writer = pd.ExcelWriter('pandas_simple2.xlsx', engine='xlsxwriter')
# >>> df.to_excel(writer, sheet_name='Sheet1',,startcol=3,startrow=3)
  # File "<stdin>", line 1
    # df.to_excel(writer, sheet_name='Sheet1',,startcol=3,startrow=3)
                                            # ^
# SyntaxError: invalid syntax
# >>> df.to_excel(writer, sheet_name='Sheet1',startcol=3,startrow=3)
# >>> writer.save()




