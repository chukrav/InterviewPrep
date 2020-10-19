#!/usr/bin/python3

# python writeBigFile.py

import pandas as pd
import sys

def readHEADER(full_name):
    fd = open(full_name, "r")
    HEADER = []
    for line in fd:
        HEADER.append(line)
    fd.close()
    return HEADER

HEADER = []

try:
    if len(sys.argv) < 2:
        HEADER = readHEADER("HEADER.txt")
    else:
        full_name = sys.argv[1]
        HEADER = readHEADER(full_name)
except:
    print("Header text was not found. Used default HEADER")
    HEADER = ['<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',
    '<html xmlns="http://www.w3.org/1999/xhtml">',
    '<head>',
    '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">',
    '<title>3.3 Harry Potter and the prisoner of Azkaban. Pt-s. 10-15</title>',
    '<link rel="stylesheet" type="text/css" href="style2.css">',
    '<script src="makeNavBar.js"></script>',
    '<script>window.onload = function() {fillNavBar();}</script></head>',
    '<body>',
    '<h3>3.3 Harry Potter and the prisoner of Azkaban. Pt-s. 10-15</h3>',
    '<p>17:30 Saturday, December 08, 2018</p><br>',
    '<div id="main">',
    '   <!--<span class="navbar" onclick="openNav()">&#9776; open</span>-->',
    '    <span class="navbar" style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; open</span>',
    '</div>',
    '<div id="i01"></div>',
    '<table border="1">']
    # 'Wavelength (um)'



FOOTER = ['</table>', '</body>', '</html>']

full_name = 'smallNew_file.txt'

#fd = open(full_name,"w",encoding="utf-8")
fd = open(full_name,"w")

wl_patt = 'Wavelength (um)'
pattDataA = '(FLOAT)DataA'
pattDataB = '(FLOAT)DataB'
RANGE_A = 1000
RANGE_B = 1500

#LEN = 100000
#LEN = 20000
LEN = 100
for j in range(LEN):
    print(".", end='')

    fd.write("\nSubfile: %d\n" % j)
    for line in HEADER:
         fd.write("%s\n" % line)
    fd.write("\n%s\n" % pattDataA)
    fd.write("\n%s pts%d\n" % (wl_patt, RANGE_A))

    # INRANGE = 1000
    for i in range(RANGE_A):
        #print("<tr><td>%s</td><td>%s</td></tr>\n" % (data.loc[i,0], data.loc[i,1]))
        fd.write("%2.6f %2.6f\n" % (i, 1))
        
    fd.write("\n%s\n" % pattDataB)
    fd.write("\n%s #%d\n" % (wl_patt, RANGE_B))
    # INRANGE = 1500
    for i in range(RANGE_B):
        #print("<tr><td>%s</td><td>%s</td></tr>\n" % (data.loc[i,0], data.loc[i,1]))
        fd.write("%2.6f %2.6f\n" % (i, 2))



fd.close()  







