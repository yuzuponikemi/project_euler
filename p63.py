#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:58:27 2018

@author: fiction
p63


The 5-digit number, 16807=7^5, is also a fifth power. Similarly, 
the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

count=0

for n in range(1,10000):
    for t in range(1,10000):
        now = t**n
        if len(str(now))==n:
            count+=1
        if len(str(now))>n:
            break
        
print(count)