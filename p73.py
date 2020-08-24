#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:03:25 2018

@author: fiction
p73


Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 
5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of 
reduced proper fractions for d ≤ 12,000?

"""
import math

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial): 
            input_list[s] = False
            

input_list = sieve_of_erastosthenes(12000)
primes = [i for i, b in enumerate(input_list) if b == True]


count = 0
#ans=0
#hcfset = set()
for n in range(2,12001):
    print(n)
    if n in primes:
        for i in range(1,n):
            if 1/3<i/n and i/n<1/2:
                count+=1
        continue
                
    nlist = [True for i in range(1,n)]
    for p in primes:
        if p>=n:break
        if n%p!=0:continue
        else:
            for s in range(p,n,p):
                nlist[s-1]=False
    for ind,val in enumerate(nlist):
        if val:
            if 1/3<(ind+1)/n and (ind+1)/n<1/2:
                count+=1
    
print(count)

#ansls = list(hcfset)
#ansls.sort()
#th = ansls.index(Fr(1,3))
#tw = ansls.index(Fr(1,2))
#ans = tw-th -1


"""
import math

def gcd(m,n):
  if m*n == 0:
    return m + n
  elif m>n:
    return gcd(m%n,n)
  else:
    return gcd(m,n%m)

count = 0
for i in range(4,12001):
  for j in range(2,math.floor(i/2)+1):
    count += gcd(i,j) == 1 and 1/3 < j/i and j/i < 1/2
      
print(count)    
"""