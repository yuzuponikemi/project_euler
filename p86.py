#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:05:38 2018

@author: fiction
p86


A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, 
F, sits in the opposite corner. By travelling on the surfaces of the room the shortest 
"straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and 
the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, 
with integer dimensions, up to a maximum size of M by M by M, 
for which the shortest route has integer length when M = 100. 
This is the least value of M for which the number of solutions first exceeds two thousand; ]
the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.

"""
#import math
#
#def countCub(m):
#    count = 0
#    mt3 = 0
#    mt2 = 0
#    # m1 < m2 < m3
#    for hw in range(3,2m+1):
##        mt3 = m3**2
##        for m2 in range(1,m3+1):
##            for m1 in range(1,m2+1):
###                ls = sorted([m1,m2,m3])
#        short = (m1+m2)**2+m
##                if int(math.sqrt(short))==math.sqrt(short):
##                    count +=1
#        if math.sqrt(short).is_integer():
#            count += 1
#    return(count)
#
#i=1000
#while True:
#   i += 1
#   now = countCub(i)
#   print(now,i)
#   if now>1000000:
#       print(i)
#       break
l = 2
while count<1000000 :
     