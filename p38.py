#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:22:57 2018

@author: fiction
p38


Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
 giving the pandigital, 918273645, 
 which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

#number must be started with 9

#nines = [91,92,93,94,95,96,97,98,912,913,914,915,916,917,,,,921,,,]
ing = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nines=[]
for i in range(91,99):
    nines.append(i)
for i in range(1,9):
    for k in range(1,9):
        if i != k:
            now = int(900 + i *10 + k)
            nines.append(now)
for i in range(1,9):
    for k in range(1,9):
        for j in range(1,9):
            if i != k and k != j and i != j:
                now = 9000 +i*100 +k*10+j
                nines.append(now)
ansdict={}
for nine in nines:
    con = str(nine)
    for i in range(2,10):
       con += str(nine*i) 
       if len(con)>=9:
           break
    if sorted(list(con))==ing:
        ansdict[nine]=con
        
print(max(ansdict.values()))
        
