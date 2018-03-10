#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:37:24 2018

@author: fiction
p42


The nth term of the sequence of triangle numbers is given by, 
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text 
file containing nearly two-thousand common English words, 
how many are triangle words?

"""
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capi = [x.upper() for x in alp]
alpdic = {alp:ind+1 for ind,alp in enumerate(capi)}
f = open('p042_words.txt')
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
data1=data1[1:-2]
words= data1.split('","')

tris = [i*(i+1)/2 for i in range(0,100)]

ans=0
for ind,name in enumerate(words):
    sc=0
    for moji in name:
        sc += alpdic[moji]
    if sc in tris:
        ans +=1
    


print(ans)