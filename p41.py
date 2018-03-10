#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:37:17 2018

@author: fiction
p41


We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

from itertools import permutations
now =""
perms=[]
for n in range(1,10):
    now = now + str(n)
    perms.extend(["".join(p) for p in permutations(now)])



for i in perms[::-1]:
    i = int(i)
    out = False
    for k in range(2,int(i**0.5 +1)):
        if i%k==0:
            out = True
            break
    if not out:
        print(i)
        break