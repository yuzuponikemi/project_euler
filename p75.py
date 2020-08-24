#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:04:43 2018

@author: fiction
p75


It turns out that 12 cm is the smallest length of wire that can be bent to 
form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
sided right angle triangle, and other lengths allow more than one solution to be found;
 for example, 
 using 120 cm it is possible to form exactly three different integer sided 
 right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000
 can exactly one integer sided right angle triangle be formed?

a^2 + b^2 = c^2
a<b<c
"""
import math
L = 1500000
ldic = {x:0 for x in range(5,L+1)}

#
#als = []
#count=0
#maxa = int(L/4)
#for a in range(1,maxa+1):
#    outnow = False
#    for p in als:
#        if a%p==0:
#            outnow= True
#            break
#    if outnow:continue
#    out = False
#    for b in range(a,int(L)):
#        c2 = a**2 + b**2
#        c = int(math.sqrt(c2))
#        l = a+b+c
#        
#        if c==math.sqrt(c2):
#            print(a,b,c,str(l)+'cm')
#            als.append(a)
##                alist = [x for x in range(a,500001,a)]
#            for newl in range(l,L+1,l):
#                ldic[newl] +=1
#
##                als.extend(alist)
#            out = True
#        if l>L:break
#        if out:
#            break
#                
#        
#count=0
#for val in ldic.values():
#    if val == 1:
#        count+=1
#print('Ans',count)

"""

count=0
for val in ldic.values():
    if val == 1:
        count+=1

print(count)
146621
but ans is 161667
"""

"""
a = m2 - n2 (∵ a = M - N だから)

b = 2 m n (∵ b2 = 4 M N だから)

c = m2 + n2
Let's try this
"""


for m in range(2,int(math.sqrt(L/2))):
    for n in range(1,m):
        if (((n + m) % 2) == 1 and math.gcd(n, m) == 1) :
            a = m**2-n**2
            b = 2*n*m
            c = m**2+n**2
            l = a+b+c
            if l<L:
                print(a,b,c,str(l)+'cm')
                for newl in range(l,L+1,l):
                    ldic[newl] +=1

count=0
for val in ldic.values():
    if val == 1:
        count+=1
print('Ans',count)