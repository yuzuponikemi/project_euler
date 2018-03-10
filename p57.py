#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:48:38 2018

@author: fiction
p57


It is possible to show that the square root of two can be expressed as 
an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
1393/985, is the first example where the number of digits in the numerator 
exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator 
with more digits than denominator?

"""
import sys
sys.setrecursionlimit(10000)
from fractions import Fraction as Fr
#>>> Fraction(16, -10)
# |  self.denominator =分母
# |  
# |  self.numerator=分子


def n_expansion(n):
    if n==1:
         return Fr(1,2)
    else:
        return 1/(2+n_expansion(n-1))
    
count=0    
for n in range(1,1001):
    now = n_expansion(n)+1
    if len(str(now.numerator))>len(str(now.denominator)):
        count+=1

print(count)
        


