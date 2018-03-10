#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:25:12 2018

@author: fiction
p40


An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, 
find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

"""

nums =""
for i in range(1,500000):
    nums=nums+str(i)
ans =1
dns =[]
tens = [1,10,100,1000,10000,100000,1000000]
for ten in tens:
    ans = ans * int(nums[ten-1])
    dns.append(int(nums[ten-1]))
nums =""
print(ans)
    