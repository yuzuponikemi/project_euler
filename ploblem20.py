#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:35:36 2018

@author: fiction
ploblem20


n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
def Kaijou(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod

def Sumdigits(n):
    digits=[int(x) for x in str(n)]
    return sum(digits)

print(Sumdigits(Kaijou(100)))

