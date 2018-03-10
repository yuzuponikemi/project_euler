#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 04:57:42 2018

@author: fiction
p51

By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, 
are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest
 prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, 
is part of an eight prime value family.

1.置換する桁は何桁でもいい(問題文から読み取れなかった)
2.置換する桁数は33の倍数(根拠がよく分からない)
3.11の位は置換してはならない(これは分かる)
4.88個置換するのだから0,1,20,1,2のいずれかで置換可能
5.最小の素数には0,1,20,1,2が22つ以上含まれる
"""

primes=[]
for i in range(10001,1000000,2):
    out = False
    for k in range(2,int(i**0.5 +1)):
        if i%k==0:
            out = True
            break
    if not out:
        primes.extend([i])
        
ans=0
out = False
for p in primes:
    st = str(p)
    setst = set(st)
    ls = list(st)
    if len(setst)<len(st):
        print(p)
        for num in list(setst):
            ls.remove(num)
        print(ls)
        if len(ls)>1:
            if ls[0]==ls[1]:
                ls.remove(ls[1])
        for target in ls:
            targetind = ""
            for ind,val in enumerate(list(st)):
                if val == target:
                    targetind += str(ind)
            pos = []
            for ind,s in enumerate(targetind):
                for r in targetind[ind+1:]: 
                    pos.append(s+r)
            print(pos)
            for po in pos:
                ls = list(st)
                one = int(po[0])
                two = int(po[1])
                count=0
                for i in range(0,10):
                    ls[one] = str(i)
                    ls[two] = str(i)
                    if int("".join(ls)) in primes:
                        count +=1
                print(count)
                if count > 7:
                    ans = p
                    out = True
                    break
        if  out:
            break

print(ans)
                
                
            

                
            
        