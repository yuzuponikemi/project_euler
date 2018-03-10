#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:39:15 2018

@author: fiction
p46
It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum 
of a prime and twice a square?
"""

def check(n):
    k = 1
    while n-2*k**2>1:
        out = False
        p = n-2*k**2
        if p==2:
            return True
        if p%2==0:
            return False
        for i in range(3,int(p**0.5)+1,2):
            if p%i==0:
                out = True
                break
        if out:
            k +=1
            continue
        else:
            return True
    return False
            
        
        
for i in range(9,100000,2):
    for k in range(3,i,2):
        if i%k==0:
            if not check(i):
                print(i)
                out = True
                break
    if out:
        break
                
            
            


    