#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:48:17 2018

@author: fiction
p49


The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: 
    (i) each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""

primes=[]
for i in range(1001,10000,2):
    out = False
    for k in range(2,int(i**0.5 +1)):
        if i%k==0:
            out = True
            break
    if not out:
        primes.extend([i])


alr = []
pos=[]
for p in primes:
    count=0
    ls =[]
    a = sorted(list(str(p)))
    if a in alr:
        continue
    alr.append(a)
    if a == ['1','4','7','8']:
        continue
    for q in primes:
        if a == sorted(list(str(q))):
            ls.append(q)
    if len(ls)>=3:
        ls = sorted(ls)
        pos.append(ls)
        print(ls)
        if ls[0]/2+ls[2]/2==ls[1]:
            print("this")
            print(ls)
            break

for ls in pos:
    for ind,num in enumerate(ls):
        for i in range(ind+1,len(ls)):
            now = ls[i]-num
            if num + now*2 in ls:
                print((num,num+now,num+now*2))

    
        
    