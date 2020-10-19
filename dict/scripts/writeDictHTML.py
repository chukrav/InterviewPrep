#!/usr/bin/python3

# python writeDictHTML.py

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



FOOTER = ['</table>', '</body>', '</html>']



fd = open("outHtml.html","w",encoding="utf-8")

for line in HEADER:
     fd.write("%s\n" % line)
     
full_name = 'file.txt'
#data = pd.read_csv(full_name,skiprows=1,sep='\t',usecols=[0,2],header=None)  # !!!!
data = pd.read_csv(full_name,skiprows=1,sep='\t',header=None)  # !!!!

for i in range(len(data)):
    #print("<tr><td>%s</td><td>%s</td></tr>\n" % (data.loc[i,0], data.loc[i,1]))
    fd.write("<tr><td>%s</td><td>%s</td></tr>\n" % (data.loc[i,0], data.loc[i,1]))

for line in FOOTER:
     fd.write("%s\n" % line)

fd.close()  







