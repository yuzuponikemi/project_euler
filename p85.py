#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:05:06 2018

@author: fiction
p85


By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains 
eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.

"""

def rec(n,h):
    ans = 0
    num=0
    for k in range(1,n+1):
        ans += k
    for g in range(1,h+1):
        num += ans*g
    return num


anslist = []
nhlist = []
diflist = []
for n in range(1,1000):#よこ
    for h in range(1,1000):#たて
        bas1 = rec(n,h)
        if 2000000-bas1 <0:
            dif1 = abs(2000000-bas1)
            bas2 = rec(n,h-1)
            dif2 = abs(2000000-bas2)
            anslist.append(bas2)
            anslist.append(bas1)
            nhlist.append((n,h-1))
            nhlist.append(((n,h)))
            diflist.append(dif2)
            diflist.append(dif1)
            break

minm = sorted(diflist)[0]

print(anslist[diflist.index(minm)])
print(nhlist[diflist.index(minm)])


    




            
            
        
