#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:59:08 2018

@author: fiction
p52


It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.

"""

for num in range(1,100000000):
    digits = sorted(list(str(num)))
    out = False
    for i in range(2,7):
        if sorted(list(str(num*i)))!=digits:
            out = True
            break
    if out:
        continue
    print(num)
    break
        

