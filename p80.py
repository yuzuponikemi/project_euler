#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:09:27 2018

@author: fiction
p80


It is well known that if the square root of a natural number is not an integer,
 then it is irrational. The decimal expansion of such square roots is infinite 
 without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., 
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, 
find the total of the digital sums of the first one hundred decimal digits 
for all the irrational square roots.

"""
import math

def p(m,alist):
    pm = 0
    if m == 0:return 0
    for k in range(m+1,1):
        pm += 10**(k-m-1) * alist[-k]
    return pm
    



def seekSQR(n):
    """
    find square root of n (0<n<99)
    """
    alist= []
    if math.sqrt(n) == int(math.sqrt(n)):
        return [0]
    else:
        for i in range(0,11):
            if i**2 > n:
                alist.append(i-1)
                break
        for m in range(0,-99,-1):
#            print(alist)
            pm = p(m,alist)
            pmm = 10 * pm + alist[-1]
#            print(pm,pmm)

            for i in range(0,11):
                if (20*pmm + i)*i > 10**(-2*(m-1))*n-100*pmm**2:
                    alist.append(i-1)
                    break
                if i == 10:
                    print('hey')
        return alist


ans = 0
for i in range(1,101):
    print(i)
    ans += sum(seekSQR(i))

print(ans)


