#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:53:52 2018

@author: fiction
p60


The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will 
always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four 
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate
 to produce another prime.

"""
import math
import itertools as itl


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
            

input_list = sieve_of_erastosthenes(10000)
primes = [i for i, b in enumerate(input_list) if b == True]
primes.remove(2)

print("yes")

#def check(ls):
#    table = ['01','02','03','04','10','12','13','14','20','21','23','24','30','31','32','34','40','41','42','43']
#    for num in table:
#        p1 = ls[int(num[0])]
#        p2 = ls[int(num[1])]
#        pr = int(str(p1)+str(p2))
#        pl = int(str(p2)+str(p1))
#        if pr in primes and pl in primes:
#            continue
#        else:
#            return False
#    return True
                
"""   
#1228^5*20の計算量であり困難
#枝刈りするなど対策が必要
#それにこの方法では最小かどうかわからない   ↓
""" 
#for one in primes[:500]:
#    print(one)
#    for tw in primes[1:]:
#        for th in primes[2:]:
#            for fou in primes[3:]:
#                for fiv in primes[500:]:
#                    out = False
#                    ls = [one,tw,th,fou,fiv]
#                    if len(set(ls))<5:
#                        continue
#                    if check(ls):
#                        print("got")
#                        print(ls)
#                        print(sum(ls))
#                        out = True
#                    else:
#                        continue
#                if out:
#                    break
#            if out:
#                break
#        if out:break
#    if out:
#        break

"""
#まず２つの素数間で条件を満たす組を見つける
prime:[nodelist]
5quokeならlen(set)==5になるはず
この場合計算は len(primes)*each[nodelist]になり短くなる　　　↓
"""
prime2=[]
def check2(p1,p2):
    out=False
    pr = int(str(p1)+str(p2))
    pl = int(str(p2)+str(p1))
    for k in range(2,int(pr**0.5 +1)):
        if pr%k==0:
            out = True
            break
    for k in range(2,int(pl**0.5 +1)):
        if pl%k==0:
            out = True
            break
    if out:
        return False
    else:
        return True

primesetdic={}
for p1 in primes:
    okset={p1}
    for p2 in primes:
        if p1 == p2:
            continue
        if check2(p1,p2):
            okset.add(p2)
    primesetdic[p1]=okset

#primelsdic={}
#for p1 in primes:
#    okls=[p1]
#    for p2 in primes:
#        if p1 == p2:
#            continue
#        if check2(p1,p2):
#            okls.append(p2)
#    primelsdic[p1]=okls

anslist=[]
for p in primes:
    baseset=primesetdic[p]
    for pos in list(primesetdic[p]):
        if p == pos:
            continue
        nowset=baseset&primesetdic[pos]
        if len(nowset)<4:
            continue
        comset = nowset.difference({p,pos})
        for th,fo,fi in itl.combinations(list(comset),3):
            hantei = nowset&primesetdic[th]&primesetdic[fo]&primesetdic[fi]
            need = {p,pos,th,fo,fi} 
            if hantei>=need and len(hantei)>4:
                anslist.append(list(hantei))
            
best=1000000
for ans in anslist:
    now = sum(ans)
    if now < best:
        best = now
        print(ans)

print(best)

"""
一万以下の素数なので
これで26033をベストとして得るが
最小化は不明
↓
26033以下の素数について計算しなおせばこれが正解だと確信できる
"""