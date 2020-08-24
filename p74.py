#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:04:05 2018

@author: fiction
p74


The number 145 is well known for the property that the sum of the factorial of 
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of 
numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get 
stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest 
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly 
sixty non-repeating terms?

"""
def Kaijou(n):
    prod = 1
    for i in range(1,int(n)+1):
        prod = prod * i
    return prod

def sum_factorical(n):
    st = [int(x) for x in list(str(n))]
    ans=0
    for s in st:
        ans += Kaijou(s)
    return ans

count=0
for i in range(1,1000001):
    numls=[i]
    nex=i
    print(i)
    while True:
        nex = sum_factorical(nex)
        if nex in numls:
            break
        numls.append(nex)
    if len(numls)==60:
        count+=1
        
print('end')
print(count)#402