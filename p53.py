#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 05:04:46 2018

@author: fiction
p53


There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = n!/(r!(n−r)!)
	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, 
are greater than one-million?

"""
def Kaijou(n):
    prod = 1
    for i in range(1,int(n)+1):
        prod = prod * i
    return prod


def combinator(n,r):
    ans = Kaijou(n)/Kaijou(r)/Kaijou(n-r)
    return ans

ok = 0
#for n in range(1,101):ミス数え間違い
#    if n%2==0:    
#        for r in range(1,int(n/2)):
#            if combinator(n,r)>1000000:
#                ok +=2
#        if combinator(n,n/2)>1000000:
#            ok +=1
#    else:
#        for r in range(1,int(n/2)):
#            if combinator(n,r)>1000000:
#                ok +=2

for n in range(1,101):
    for r in range(1,n+1):
        if combinator(n,r)>1000000:
            ok+=1

print("ans is")
print(ok)
            
    
