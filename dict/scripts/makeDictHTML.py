#!/usr/bin/python3
import pandas as pd


full_name = "HP3_10-15.txt"
data = pd.read_csv(full_name,skiprows=1,sep='\t')
data = pd.read_csv(full_name,skiprows=1,sep='\t',usecols=[0,2],header=None)  # !!!!
#data.sort_values(["Team", "Name"], axis=0, ascending=True, inplace=True) 
data_s.sort_values(0, axis=0, ascending=True, inplace=True) 
data_s.to_csv('file.csv',encoding='utf-8-sig',sep='\t', header=None, index=None)
data_s.reset_index(drop=True) # Reset index after sorting ..........
print(data_s.to_html(index=None))
data_s.to_html('file.txt',encoding='utf-8-sig',index=None)

#df.loc[df['column_name'] == some_value]
data.loc[data[0] == 'wisp']

import collections
a = [1,2,3,2,1,5,6,5,5,5]
print([item for item, count in collections.Counter(a).items() if count > 1])
## [1, 2, 5]
print([item for item, count in collections.Counter(words).items() if count > 1])
data.loc[data[0] == 'wisp']

#pd.to_csv('lines.txt',
#        index=False,
#        header=False,
#        mode='a')

#If you really want to print line by line. (You should not).
#
#for i in range(len(df)):
#    df.loc[[i]].to_csv(output_csv_file,
#        index=False,
#        header=False,
#        mode='a')
df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
...                    'mask': ['red', 'purple'],
...                    'weapon': ['sai', 'bo staff']})
for i in range(len(df)):
    print(df.loc[[i]]).to_csv(index=None,header=None)

#>>> print(df.to_csv(sep=' '))
# name mask weapon
#0 Raphael red sai
#1 Donatello purple "bo staff"

#df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
#     index=['cobra', 'viper', 'sidewinder'],
#     columns=['max_speed', 'shield'])
#>>>df
#            max_speed  shield
#cobra               1       2
#viper               4       5
#sidewinder          7       8
#>>>dh = df.to_html(index=None,header=None)
#dh
#<table border="1" class="dataframe">  <tbody>    <tr>      <td>Raphael</td>      <td>red</td>      <td>sai</td>    </tr>\n    <tr>      <td>Donatello</td>      <td>purple</td>      <td>bo staff</td>    </tr>\n  </tbody></table>
#>>> [m.start() for m in re.finditer('\n', dh)]
#[36, 46, 55, 78, 97, 116, 126, 135, 160, 182, 206, 216, 227]
dh.replace('\n','').replace('</tr>', '</tr>\n')
#<table border="1" class="dataframe">  <tbody>    <tr>      <td>Raphael</td>      <td>red</td>      <td>sai</td>    </tr>\n    <tr>      <td>Donatello</td>      <td>purple</td>      <td>bo staff</td>    </tr>\n  </tbody></table>
#Replacer
import re
ind = [m.start() for m in re.finditer('\n', dh)]
for i in ind[2:-1]:
	dh = dh[:i] + '' + dh[i+1:]
	
<table border="1" class="dataframe">\n  <tbody>\n    <tr>      <td>Raphael</td>\n     <td>red</td>\n     <td>sai</td>\n   </tr>\n   <tr>\n     <td>Donatello</td>\n     <td>purple</td>\n      td>bo staff</td>\n    </t>\n  </tbod>\n</table>'

#How to Export Pandas DataFrame to JSON File
#https://datatofish.com/export-pandas-dataframe-json/
data = {'Product': ['Desktop Computer','Tablet','iPhone','Laptop'],
        'Price': [700,250,800,1200]
        }

df = DataFrame(data, columns= ['Product', 'Price'])
print(df.to_json(indent=1,orient='columns')) # Pretty format if indent=None not formatted
# orient options:
    # split
    # records
    # index
    # values
    # table
    # columns (the default format)
	
#Work with HTML - JSON ==============
pip install lxml
>>>url = 'HP3_10-15.html'
>>> dfs = pd.read_html(url)
>>> dfs
[                0                                                  1
0         abiding  постоянный; неизменный; прочный Syn: permanent...
1         altered  усовершенствованный, alter изменять; менять; в...
2    announcement  объявление, сообщение; извещение, уведомление ...
3         astound  изумлять, поражать Syn: pamaze, strike dumb [ ...
4          asylum  убежище, пристанище, прибежище приют (благотво...
..            ...                                                ...
157          wisp  пучок, жгут, клок худенький, хрупкий человек к...
158          womb  анат. матка лоно; поэт. мрак исток, начало; in...
159       worship  поклоняться, почитать благоговеть, боготворить...
160        wreath  венок, гирлянда завиток, кольцо (дыма) шотл. с...
161        wrench  тоска, боль мучить, причинять страдание, боль ...

[162 rows x 2 columns]]

