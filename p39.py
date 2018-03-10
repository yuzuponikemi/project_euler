#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:23:54 2018

@author: fiction
p39

If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
ansdic={}

for p in range(4,1001):
    count=0
    for a in range(1,p//2):
        for b in range(1,p-a):
            c = p-a-b
            if a**2+b**2==c**2:
                count+=1
    ansdic[p]=count               
biggest =0
ans = 0
for key in ansdic.keys():
    if ansdic[key]>biggest:
        biggest = ansdic[key]
        ans = key
    