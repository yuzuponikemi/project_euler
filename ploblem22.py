#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:40:33 2018

@author: fiction
ploblem22


Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capi = [x.upper() for x in alp]
alpdic = {alp:ind+1 for ind,alp in enumerate(capi)}
f = open('p022_names.txt')
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
data1=data1[1:-2]
names= data1.split('","')
namesdic = {}
sortednames = sorted(names)
for ind,name in enumerate(sortednames):
    sc=0
    score=0
    for moji in name:
        sc += alpdic[moji]
    score = sc*(ind+1)
    namesdic[name]=score

ans = sum(namesdic.values())
print(ans)

    
    

    



