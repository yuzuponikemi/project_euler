#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:49:34 2018

@author: fiction
p58


Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both 
diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral 
with side length 9 will be formed. If this process is continued, 
what is the side length of the square spiral for which the ratio of primes
 along both diagonals first falls below 10%?


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

diagonals=1
now=1
p=0
for ev in range(2,10000000,2):
    diagonals+=4
    for i in range(0,4):
        now += ev
        if now in primes:
            p+=1
        else:
            pri=True
            for k in range(2,int(now**0.5)+1):
                if now%k==0:
                    pri = False
                    break
            if pri:
                p+=1
    print(p/diagonals)
    if p/diagonals<0.1:
        print(ev+1)
        break
            
    
        

