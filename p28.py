#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:47:09 2018

@author: fiction
p28
Starting with the number 1 and moving to the right in a clockwise direction
 a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

"""
"""
diagonals =　[1,3,5,7,9,13,17,21,25,31,37]
adds =[2,2,2,2,4,4,4,4,6,6,6,6,8,1000]
"""
evens = list(range(2,1001,2))
adds=[]
for even in evens:
    for i in range(0,4):
        adds.append(even)

sums = 1
now=1
for add in adds:
    now = now + add
    sums += now
print(sums)