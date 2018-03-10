#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:19:00 2018

@author: fiction
p33


The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
 find the value of the denominator.

"""
from fractions import Fraction

#def checkit(a,b):
#    seta = set()
#    setb = set()
#    seta.add(list(str(a)))
#    setb.add(list(str(b)))
#    ad = (seta - (seta&setb)).pop()
#    bd = (setb - (seta&setb)).pop()
#    if 

def checkit(a,b):
    lista = list(str(a))
    listb = list(str(b))
    if lista[0]==listb[1] and lista[1]!=listb[0] and int(listb[0])!=0:
        if int(lista[1])/int(listb[0])==a/b:
            return True
    if lista[1]==listb[0] and lista[0]!=listb[1] and int(listb[1])!=0:
        if int(lista[0])/int(listb[1])==a/b:
            return True
    return False

goods={}
for a in range(11,100):
    for b in range(a,100):
        if checkit(a,b):
            goods[a]=b
bunsi=1
bunbo=1
for key in goods:
    bunsi *= key
    bunbo *= goods[key]

ans = Fraction(bunsi,bunbo)    
print(ans)
        
