#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:06:04 2018

@author: fiction
ploblem15

Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""

def Kaijou(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod

answer = int(Kaijou(40)/Kaijou(20)/Kaijou(20))

print(answer)