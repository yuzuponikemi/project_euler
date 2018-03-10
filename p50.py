#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:49:15 2018

@author: fiction
p50


The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?

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
        
now=0
count =0
best = 0
for ind,p in enumerate(primes):
    now = p
    print(p)
    for i in range(1,len(primes)-ind):
        now = now + primes[ind+i]
        if now>1000000:
            break
        if now in primes:
            count =i
            if count > best:
                best = count
                print("best "+str(best))
                ans = now
        
            

print(best,ans)
        