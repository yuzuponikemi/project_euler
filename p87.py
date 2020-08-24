#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:06:17 2018

@author: fiction
p87


The smallest number expressible as the sum of a prime square, prime cube, 
and prime fourth power is 28. In fact, there are exactly four numbers below fifty 
that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, 
prime cube, and prime fourth power?

"""

import math

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial): 
            input_list[s] = False
            
            
limit=50000000

input_list = sieve_of_erastosthenes(12000)
primes = [i for i, b in enumerate(input_list) if b == True]

p2s=[]
p3s=[]
p4s=[]
for p in primes:
    if p**4<limit:p4s.append(p)
    if p**3<limit:p3s.append(p)
    if p**2<limit:p2s.append(p)
    
    
    
oklist = []
i = 0

for p4 in p4s:
    print(i)
    num4 = p4**4
    for p3 in p3s:
        numa = num4+p3**3
        if numa > limit:break
        for p2 in p2s:
            num = numa+p2**2
            if num < limit:
                if num in oklist:
                    continue
                else:
                    oklist.append(num)
            else:break
    i += 1
print(len(oklist))
            