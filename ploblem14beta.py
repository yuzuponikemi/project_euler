#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 02:22:10 2018

@author: fiction
"""

import time
 
start = time.time()
 
def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count
 
max = [0,0]
for i in range(1000000):
    c = collatz(i)
    if c > max[0]:
        max[0] = c
        max[1] = i
 
elapsed = (time.time() - start)
print(max[1],max[0],elapsed)