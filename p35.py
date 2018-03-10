#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:20:17 2018

@author: fiction
p35
The number, 197, is called a circular prime because all rotations of the digits:
    197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

#まず素数をリストアップ
primes=[2]
for i in range(3,1000000,2):
    out = False
    for k in range(2,int(i**0.5 +1)):
        if i%k==0:
            out = True
            break
    if not out:
        primes.extend([i])
        
ansset=set((2,3,5,7))
for prime in primes:
    dame = False
    s = str(prime)
    ss = s*2
    digi = len(s)
    checklist=[]
    for i in range(1,digi):
        checklist.append(int(ss[i:i+digi]))
    for rot in checklist:
        if rot not in primes:
            dame = True
            break
    if not dame:
        for rot in checklist:
            ansset.add(rot)
            
print(len(ansset))
    