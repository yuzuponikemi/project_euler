#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:06:42 2018

@author: fiction
p78


Let p(n) represent the number of different ways in which n coins
 can be separated into piles. 
 For example, five coins can be separated into piles in exactly seven different ways,
 so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

containing another number a number of times without a remainder.
"24 is divisible by 4"

    p(k) = p(k − 1) + p(k − 2) − p(k − 5) − p(k − 7) + p(k − 12) + p(k − 15) − p(k − 22) − ...

を得る。ここで p(0) = 1 および負の整数 k に対して p(k) = 0 とし、和は ½n(3n − 1) の形
（ただし n は正または負の整数全体を走る）の一般五角数全体にわたってとるものとする
（順に n = 1, −1, 2, −2, 3, −3, 4, −4 ..., とすると、
値として 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, ... が得られる）。
和における符号は交互に +, +, −, −, +, +, ... と続く。 

"""

#TOO SLOW
#dic21 = {x:0 for x in range(3,1000000)}
#
#def calc21(n,ls):
#    """
#    nをls=[3,2,1]などの数字の組み合わせで表す
#    """
#    if ls == [2,1]:
#        return n//2+1
#    cou=0
#    maxi = n//ls[0]
#    for i in range(0,maxi+1):
#        cou += calc21(n-i*ls[0],ls[1:])
#    return cou
#
#def p(n):
#    return calc21(n,[x for x in range(n-1,0,-1)])+1
#
#
#
#for i in range(3,1000000):
#    now = p(i)
#    if now%1000000==0:
#        print('ans')
#        print(i)
#        break
#    print(i)
#    print(now)
#        
    
#BETTER SOLUTION
nls = []
ls = [[x,-x] for x in range(1,10000)]
for l in ls:
    nls.extend(l)
minusl = []
for g in nls:
    minusl.append(g*(3*g-1)/2)


    
pdic = {0:1}
 


def p(k):
    pk = 0
    if k == 0:
        return 1
    if k < 0:
        return 0
        
    for i in minusl:
        if k < i:
            nowl = minusl[:minusl.index(i)]
            break
    for ind,now in enumerate(nowl):
        if k-now in pdic.keys():
            if ind%4 == 0 or ind%4 == 1:
                pk += pdic[k-now]
            else:
                pk -= pdic[k-now]
        else:
            
            if ind%4 == 0 or ind%4 == 1:
                pk += p(k-now)
            else:
                pk -= p(k-now)
    pdic[k] = pk
    return pk


for i in range(3,1000000):
    now = p(i)
    if now%1000000==0:
        print('ans')
        print(i)
        break
    print(i)



