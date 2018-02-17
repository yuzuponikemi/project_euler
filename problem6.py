#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:09:07 2018

@author: yusukeikemi
problem6
sum square difference
"""

number = range(1,101)
ans1 = 0
ans2 = 0
sums = 0
for i in number:
    ans1 += i**2
for k in number:
    sums = sums + k
ans2 = sums**2

answer = abs(ans1-ans2)

print("answer is " + str(answer))
