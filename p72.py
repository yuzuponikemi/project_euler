#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:02:30 2018

@author: fiction
p72


Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 
5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

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
            

input_list = sieve_of_erastosthenes(1000000)
primes = [i for i, b in enumerate(input_list) if b == True]


def prime_factorization(num):
    """
    [(p,e),,,]の形で素因数と指数のリストを返す
    """
    ls = []
    sqrt = math.sqrt(num)
    now = num
    for p in primes:
        suf = 0
        if p > sqrt:break
        while True:
            if now%p==0:
                now = now/p
                suf +=1
            else:
                break
        if suf != 0:ls.append((p,suf))
    if now != 1:ls.append((int(now),1))
    return(ls)
        

#count = 0
#ans=0
#for n in range(2,1000001):
#    if n%10000==0:print(n)
##    if n in primes:
##        count+= n-1
##        continue
#    ls = prime_factorization(n)
#
#    for pr,suf in ls:
#
#    count += sum(tls)
#    
#
#print('end')
#print(count)
    

count=0

for n in range(2,1000001):
    lis = prime_factorization(n)
    phin = n
    for pr , suf in lis:
        phin = phin * (pr - 1)/pr
    count += phin

    

print(count)