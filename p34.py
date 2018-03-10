#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:19:48 2018

@author: fiction
p34


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


"""
Kaijou(9)
Out[23]: 362880
362880*8=2903040(7digit)
7digit ==>1000000is upperlimit
"""
def Kaijou(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod

def sumdigitsfactorical(n):
    digits=[Kaijou(int(x)) for x in str(n)]
    return sum(digits)
anslist=[]
for i in range(3,1000000):
    if i ==sumdigitsfactorical(i):
        anslist.append(i)

print(sum(anslist))

