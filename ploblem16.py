#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:06:33 2018

@author: fiction
ploblem16


2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

"""

def Sumdigits(n):
    digits=[int(x) for x in str(n)]
    return sum(digits)

print(Sumdigits(2**1000))

    