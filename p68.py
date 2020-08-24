#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:57:26 2018

@author: fiction
p68
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, 
and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically
 lowest external node (4,3,2 in this example), each solution can be described uniquely. 
 For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
 There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; 
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements,
 it is possible to form 16- and 17-digit strings.
 What is the maximum 16-digit string for a "magic" 5-gon ring?
"""

from itertools import permutations
#numsdic={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'t':10}
perms = ["".join(p) for p in permutations('123456789')]


okls=[]
#10の位置を①に固定した場合（先端 16桁になるのはこの場合のみなのでこれだけで良い
for perm in perms:
    a = 10,int(perm[5]),int(perm[6])
    suma = sum(a)
    b = int(perm[1]),int(perm[6]),int(perm[7])
    if sum(b)!=suma:continue
    c = int(perm[2]),int(perm[7]),int(perm[8])
    if sum(c)!=suma:continue
    d = int(perm[3]),int(perm[8]),int(perm[0])
    if sum(d)!=suma:continue
    e = int(perm[4]),int(perm[0]),int(perm[5])
    if sum(e)!=suma:continue
    ls = [a,b,c,d,e]
    okls.append(ls)

print(okls)
    
    



#10の位置を⑩に固定した場合（五角形内部