#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:06:07 2018

@author: fiction
p77


It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes 
in over five thousand different ways?

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
            

input_list = sieve_of_erastosthenes(1200)
primes = [i for i, b in enumerate(input_list) if b == True]





def calc32(n,ls):
    """
    nをls=[3,2]などの素数の組み合わせで表す関数
    """
    if ls == [3,2]:
        if n == 1:
            return 0
        else:
            return n//6+1
    cou=0
    maxi = n//ls[0]
    for i in range(0,maxi+1):
        cou += calc32(n-i*ls[0],ls[1:])
    return cou


primes.reverse()

for i in range(20,10000):
    for p in primes:
        if p <= i:
            ls = primes[primes.index(p):]
            break
    if calc32(i,ls) > 5000:
        print('ans is',i)
        break
    