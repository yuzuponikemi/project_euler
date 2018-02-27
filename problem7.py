#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:25:04 2018

@author: yusukeikemi

problem7
What is 10001st prime number?
"""
primes =[1]
i = 2
k = True
while True:
    clears = []
    checkers = range(1,int(i/2))
    for checker in checkers:
        if i % checker ==0:
            clears.append(checker)
    if clears == [1]:
        primes.append(i)
        print(primes)
    i +=1
        
            
    if len(primes)>10001:
        print("answer is "+str(primes[10000]))
        break
print("end")