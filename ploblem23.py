#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:41:29 2018

@author: fiction
ploblem23


A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would 
be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be
 written as the sum of two abundant numbers. 
 However, this upper limit cannot be reduced any further by analysis e
 ven though it is known that the greatest number that cannot be expressed as 
 the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.

"""
abundants =[]

for i in range(2,28111):
    
    divisors =[]
    for k in range(1,int(i**0.5)+1):
        if i%k == 0:
            if (k == i**0.5 or k == 1):
                divisors.append(k)
            else:    
                divisors.append(k)
                divisors.append(i/k)
    if i < sum(divisors):
        abundants.append(i)
possibles = set()
for one in abundants:
    for two in abundants:
        possibles.add(one+two)

print(possibles)
positives = set(range(1,28124))

cannots = positives-possibles
ans = sum(cannots)
print(ans)
        
        
