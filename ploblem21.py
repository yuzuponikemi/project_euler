#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:22:38 2018

@author: fiction
ploblem21


Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable 
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

import time
start =time.time()
numsdic ={}
ans =0
for i in range(2,10001):
    
    divisors =[]
    for k in range(1,int(i**0.5)+1):
        if i%k == 0:
            if (k == i**0.5 or k == 1):
                divisors.append(k)
            else:    
                divisors.append(k)
                divisors.append(i/k)
    numsdic[i]=int(sum(divisors))
amicables = []   
for num in numsdic.keys():
    for val in numsdic.keys():
        if (num ==numsdic[val] and numsdic[num]==val and num!=val):
            ans = ans + num + val
            amicables.append((num,val))

ans = ans/2
elapsed = (time.time() - start)
print(numsdic)
print(ans)
print(elapsed)
print(amicables)

