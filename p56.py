#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:47:25 2018

@author: fiction
p56


A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?

"""

def sumdigits(n):
    ans = sum([int(x) for x in str(n)])
    return ans


best = 0
for a in range(2,100):
    for b in range(2,100):
        now = sumdigits(a**b)
        if now>best:
            best = now

print(best)