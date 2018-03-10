#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:44:34 2018

@author: fiction
p26


A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.



正規表現で最初の０はとばす
残りの数字を文字列として格納

"""
#numsdic = {}
#for i in range(2,1000):
#    val = 1/i
#    numsdic[i]=str("{0:.18f}".format(val))[:-2]
#    
#    
#
##S.find(sub) # S.rfind(sub)	部分文字列 sub の位置を返す。見つからない場合は -1 を返す。
##S.index(sub) # S.rindex(sub)	部分文字列 sub の位置を返す。見つからない場合は ValueError を送出する。
##S.count(sub)	#部分文字列 sub の出現回数を返す。
#longest=0
#for frac in numsdic.values():
#    now = frac[:]
#    frac = frac[2:]
#    for i in range(0,5):
#        if frac[0]=="0":
#            frac = frac[1:]
#        else:
#            break
#    for k in range(1,len(frac)):
#        count =frac.count(frac[0:k])
#        long = len(frac[0:k])
#        if count >2 and long > longest:
#            longest=long
#            ans=now
        

def calc(d):
    a = 1

    mod_set = set()

    while True:
        a *= 10

        if (a % d) in mod_set:
            break
        else:
            mod_set.add(a % d)
        a %= d

    mod_set = set()

    length = 0
    while True:
        a *= 10

        if (a % d) in mod_set:
            break
        else:
            mod_set.add(a % d)
            length += 1

        a %= d

    return length
"""
これは、普通に割り算の筆算と同じ事をやればいいな。余りをsetに持つようにして、
同じ余りが出てきた時点でループと見なして検出すればよい。
ただし、1周目はループの長さはわからない（最初にゴミが入っている可能性がある）ので、
2周目を検出しなくてはならないのが面倒なところだけど。
この余分な手順は、余りをすべて数列として持って厳密に数列からループ検出をすれば必要ない。
だけど、そうすると結構時間がかかりそうな気がするし、かえって複雑になる気がするので却下。
下のプログラムは、「ループ長 d」という順番で表示するようになっている。sort に渡せば答えが出る。
"""
for i in range(2, 1000):
    print(calc(i), i)
    

