#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:57:02 2018

@author: fiction
p62


The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations 
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""
cubes=[]
for i in range(0,100000):
    cubes.append(sorted(str(i**3)))

for ind,val in enumerate(cubes):
    count=0
    print(ind)
    for cube in cubes[ind+1:]:
        if cube==val:
            count+=1
    if count==4:
        print("ans")
        print(ind**3)
        break

    
    