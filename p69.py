#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:58:15 2018

@author: fiction
p69


Euler's Totient function, φ(n) [sometimes called the phi function],
 is used to determine the number of numbers less than n which are relatively prime to n. 
 For example, as 1, 2, 4, 5, 7, and 8, 
    are all less than nine and relatively prime to nine, φ(9)=6.
n 	RelativelyPrime 	φ(n) 	n/φ(n)
2 	1 	               1   	2
3 	1,2 	                2 	1.5
4 	1,3                  	2 	2
5 	1,2,3,4              	4 	1.25
6 	1,5                  	2 	3
7 	1,2,3,4,5,6          	6 	1.1666...
8 	1,3,5,7 	            4 	2
9 	1,2,4,5,7,8 	        6 	1.5
10 	1,3,7,9 	               4 	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

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


best = 0
ans=0
for n in range(6,1000000,2):
    print(n)
    if n in primes:continue
    nlist = [True for i in range(1,n)]
    for p in primes:
        if p>=n:break
        if n%p!=0:continue
        else:
            for s in range(p,n,p):
                nlist[s-1]=False
    phin = sum(nlist)
#    print(n,nlist)
    if n/phin > best:
        best = n/phin
        ans = n
print('end')
print(best)
print(ans)
    

#これは時間がかかるので　結局2*3*5*7*13*17で解いた