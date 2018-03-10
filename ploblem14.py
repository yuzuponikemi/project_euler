#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:05:40 2018

@author: fiction
ploblem14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
numbersr = list(range(1000000,0,-1))
numbers = set(numbersr)
appeared = set()

def Collatz(n):
    if n%2==0:
        return n/2
    else:
        return n*3+1
dic={}
best=0
long = 0
while True:
    now = numbers.pop()
    num = now
    count = 0
    numlist=[num]
    while True:
        num= Collatz(num)
        numlist.append(num)
        count += 1
        if num in dic.keys():
            for n in numlist:
                dic[n]=len(numlist)-numlist.index(n)+dic[num]           
            if dic[now] > long:
                long = dic[now]
                best = now
            break
        if num==1:
            #ex[9,3,5,2,1]なら　dic[3]=len(numlist)-numlist.index(3)
            for n in numlist:
                dic[n]=len(numlist)-numlist.index(n)         
            if count > long:
                long = count
                best = now
#                
            break
        
        appeared.add(num)
    numbers = numbers-appeared
    print(len(numbers))
    if numbers == set():
        break
print("answer")
print(best)

        