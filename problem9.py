#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:35:51 2018

@author: yusukeikemi

problem9
a + b + c = 1000
find(a,b,c) that fulfil a^2+b^2=c^2
"""

for a in range(1,999):
    rest = 1000 - a
    for b in range(1,rest):
        c = rest -b
        if a**2+b**2 == c**2:
            g,h,i = a,b,c

answer = g*h*i
print("answer is "+str(answer))

