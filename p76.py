#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:05:35 2018

@author: fiction
p76


It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of 
at least two positive integers?

"""
def calc21(n,ls):
    """
    nをls=[3,2,1]などの数字の組み合わせで表す関数
    """
    if ls == [2,1]:
        return n//2+1
    cou=0
    maxi = n//ls[0]
    for i in range(0,maxi+1):
        cou += calc21(n-i*ls[0],ls[1:])
    return cou



lis = [x for x in range(1,100)]

lis.reverse()

print(calc21(100,lis))
        
        

        
        
    
    




