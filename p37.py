#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:22:14 2018

@author: fiction
p37


The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

#primes=[2]
#for i in range(3,1000000,2):
#    out = False
#    for k in range(2,int(i**0.5 +1)):
#        if i%k==0:
#            out = True
#            break
#    if not out:
#        primes.extend([i])
#
#
#anslist=[]
#for prime in primes[4:]:
#    if len(anslist)==11:
#        break
#    cuts = []
#    spr = str(prime)
#    digi = len(spr)
#    for i in range(0,digi-1):
#        cuts.append(int(spr[:-(i+1)]))
#        cuts.append(int(spr[i+1:]))
#    ok = True
#    for cut in cuts:
#        if cut not in primes:
#            ok = False
#    if ok :
#        anslist.append(prime)
#        print(anslist)
#
#print(sum(anslist))

        
primes=[2]
anslist=[]
for i in range(3,10000000000,2):
    out = False
    for k in range(2,int(i**0.5 +1)):
        if i%k==0:
            out = True
            break
    if not out:
        primes.extend([i])
        prime=i
        if len(anslist)==11:
            break
        cuts = []
        spr = str(prime)
        digi = len(spr)
        if digi==1:
            continue
        for i in range(0,digi-1):
            cuts.append(int(spr[:-(i+1)]))
            cuts.append(int(spr[i+1:]))
        ok = True
        for cut in cuts:
            if cut not in primes:
                ok = False
        if ok :
            anslist.append(prime)
            print(anslist)