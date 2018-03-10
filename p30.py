#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 01:58:40 2018

@author: fiction
pl30


Surprisingly there are only three numbers that can be written as 
the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as 
the sum of fifth powers of their digits.

"""
def fifthpowerdigits(n):
    digits = [int(x) for x in list(str(n))]
    ret=0
    for dig in digits:
        ret += dig**5
    return ret

    
yes=[]
for i in range(2,9**5*5):
    if i == fifthpowerdigits(i):
        yes.append(i)
    
print(sum(yes))
