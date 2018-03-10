#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:37:29 2018

@author: fiction
p43


The number, 1406357289, is a 0 to 9 pandigital number because 
it is made up of each of the digits 0 to 9 in some order,
 but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

"""
from itertools import permutations
perm =["".join(x) for x in permutations("0123456789")]

anslist=[]
for per in perm:
    d234 = int(per[1:4])
    d345 = int(per[2:5])
    d456 = int(per[3:6])
    d567 = int(per[4:7])
    d678 = int(per[5:8])
    d789 = int(per[6:9])
    d8910 = int(per[7:10])
    if d234%2==0 and d345%3==0 and d456%5==0 and d567%7==0:
        if d678%11==0 and d789%13==0 and d8910%17==0:
            anslist.append(int(per))

print(sum(anslist))
