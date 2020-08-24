#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:00:26 2018

@author: fiction
p70


Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n 
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and 
the ratio n/φ(n) produces a minimum.


m, n を互いに素な自然数とすると、φ(mn) = φ(m)φ(n) が成り立つ。
これをオイラーの関数は（互いに素な数の積に関して）乗法的であると言う。
これらのことからさらに、任意の自然数 n における値を知ることができる。
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
        

phi=[]
best = 1.9
for n in range(7,10000000):
    lis = prime_factorization(n)
    phin = n
    for pr , suf in lis:
        phin = phin * (pr - 1)/pr
    phin = int(phin)
    nlis = list(str(n))
    phinlis = list(str(phin))
    nlis.sort()
    phinlis.sort()
    if nlis == phinlis:
        ratio = n/phin
        print(n,ratio)
        if ratio < best:
            ans = n
            best = ratio

    

print(ans)





