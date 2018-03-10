#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:15:55 2018
unsolved
@author: fiction
p31
In England the currency is made up of pound, £, and pence, p, 
and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

"""

coins = [1,2,5,10,20,50,100]
maisu = [0,0,0,0,0,0,0]
ways = 1#200
#one two five ten twen fifty hund
full = 200
oks=[]


def calc(maisu):
    ans = 0
    for i in range(0,7):
        ans += coins[i]*maisu[i]
    return ans

for hund in range(0,3):
    maisu = [0,0,0,0, 0, 0, 0]
    maisu[6]=hund
#    if calc(maisu) == full:
#        oks.append(maisu)
#        break
    for fifty in range(0,int((200-hund*100)/50+1)):
        maisu[5]=fifty
        for twen in range(0,int((200-hund*100-fifty*50)/20+1)):
            maisu[4]=twen
#            if calc(maisu) == full:
#                oks.append(maisu)
#                break
            for ten in range(0,int((200-hund*100-fifty*50-twen*20)/10+1)):
                maisu[3]=ten
#                if calc(maisu) == full:
#                    oks.append(maisu)
#                    break
                for five in range(0,int((200-hund*100-fifty*50-twen*20-ten*10)/5+1)):
                    maisu[2]=five
#                    if calc(maisu) == full:
#                        oks.append(maisu)
#                        break
                    for two in range(0,int((200-hund*100-fifty*50-twen*20-ten*10-five*5)/2+1)):
                        maisu[1]=two
#                        if calc(maisu) == full:
#                            oks.append(maisu)
#                            break
                        for one in range(0,int((200-hund*100-fifty*50-twen*20-ten*10-five*5-two*2+1))):
                            maisu[0]=one
                            ways+=1
                            if calc(maisu) == full:
                                oks.append(maisu[:])
                                print(maisu)
print(len(oks)+1)                 



"""
最後のmaisu[:]はmaisuにするとおかしくなる、oksに正しく保存できなくなる
問題の正解はだせるが
苦労した部分なので注意
これはIDと値の違い、参照を学ぶいい例
"""    