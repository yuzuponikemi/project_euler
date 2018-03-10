#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:39:15 2018

@author: fiction
p47


The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?

"""

primes=[2]
for i in range(3,1000000,2):
    out = False
    for k in range(2,int(i**0.5 +1)):
        if i%k==0:
            out = True
            break
    if not out:
        primes.extend([i])
        
anslist=[]
now=0
for k in range(646,100000000):
    ans = k
    numdic={}
    for p in primes:
        if p > k:
            break
        suf =0
        while k%p==0:
            k = k/p
            suf +=1
        if suf>0:
            numdic[p]=suf
        if k==1:
            break
    if len(numdic.keys())==4:
        now +=1
        print(now)
        if now == 4:
            print(ans-3)
            break
    else:
        now = 0
    