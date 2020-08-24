#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:01:49 2018

@author: fiction
p71


Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
            highest common factor 

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 
5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 
in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

"""

from fractions import Fraction as Fr
#nume=3
#deno=1
#for n in range(1,1000001):
#    deno= deno*n
#    if n==7:continue
#    nume = nume*n
#for i in range(0,10000000000):
#    nume = nume-1
#    now = Fr(nume,deno)
#    if now.denominator<1000000:
#        print(now)
#        break
    

best = 1
for d in range(8,1000001):
    nu = int(3/7*d)
    dif = 3/7-nu/d
    if 0<dif<best:
        best=dif
        ans = Fr(nu,d)

print(ans)