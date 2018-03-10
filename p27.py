#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:45:19 2018

@author: fiction
p27
Euler discovered the remarkable quadratic formula:

n**2+n+41

It turns out that the formula will produce 40 primes 
for the consecutive integer values 0≤n≤39
. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41,
 and certainly when n=41,41^2+41+41

is clearly divisible by 41.

The incredible formula n^2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number 
of primes for consecutive values of n, starting with n=0.
"""

longest=0
bests=(0,0)

for a in range(-1000,1000):
    for b in range(-1000,1001):
        out=False
        long=0
        for n in range(0,10000):
            prod=n**2+a*n+b
            if prod <2:
                out =True
                break
            for k in range(2,int(prod**0.5)+1):
                if prod%k == 0:
                    out=True
            long+=1
            if long>longest:
                longest=long
                bests =(a,b)
                print(longest)
            if out:
                break

                
    
                        
