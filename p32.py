#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:18:04 2018

@author: fiction
p32


We shall say that an n-digit number is pandigital if it makes use of all 
the digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure 
to only include it once in your sum.

"""
from itertools import permutations

 
perms = ["".join(p) for p in permutations('123456789')]
ansset=set()
for perm in perms:
    for kakeru in range(1,8):
        for equ in range(kakeru+1,9):
            a = int(perm[:kakeru])
            b = int(perm[kakeru:equ])
            c = int(perm[equ:])
            if a*b==c:
                ansset.add(c)

print(sum(ansset))

                
            
            
            



        
        

    
#def pandigitalcheck(s):
#    numlist = range(1,10)
#    for num in s:
#        if int(num) in numlist:
#            numlist.remove(int(num))
#    if numlist == []:
#        return True
#    else:
#        return False