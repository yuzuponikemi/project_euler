#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:21:27 2018

@author: fiction
p36


The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, 
may not include leading zeros.)

"""
def tenstobinary(n):
    """ 0<n<1000000"""
    table=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
    table = table[::-1]
    binary=[]
    for ind,val in enumerate(table):
        if n//val==1:
            binary.append("1")
            n -= val
        else:
            if binary != []:
                binary.append("0")
    return "".join(binary)
 

palindromics=[]       
for i in range(1,1000000):
    st = str(i)
    rev =st[::-1]
    if st==rev:
        palindromics.append(i)
        
ans = 0
for pal in palindromics:
    binary = tenstobinary(pal)
    reverse = binary[::-1]
    if binary == reverse:
        ans += pal

print(ans)