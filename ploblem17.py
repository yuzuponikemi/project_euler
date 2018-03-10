#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:07:11 2018

@author: fiction
ploblem17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

"""

numwords = ["one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",\
            "eighteen","nineteen"]
tens = ["twenty","thirty","forty","fifty","sixty","seventy"\
            ,"eighty","ninety"]
numlet = {(numwords.index(x)+1):len(x) for x in numwords}
teenlet = {(teens.index(x)+10):len(x) for x in teens}
tenlet = {(tens.index(x)+2):len(x) for x in tens}

def Howmanylet(n):
    keta = len(str(n))
    lett =0
    if keta == 3:
        lett = numlet[int(str(n)[0])]+7
        if n%100==0:
            return lett
        else:
            lett +=3
            if int(str(n)[-2])==1:
                lett += teenlet[int(str(n)[-2:])]
                return lett
            else:
                if n%10==0:
                    lett += tenlet[int(str(n)[-2])]
                    return lett
                else:
                    if int(str(n)[1])==0:
                        lett += numlet[int(str(n)[-1])]
                        return lett
                    else:
                        lett += tenlet[int(str(n)[-2])]+numlet[int(str(n)[-1])]
                        return lett
    if keta == 2:

        if int(str(n)[-2])==1:
            lett += teenlet[int(str(n)[-2:])]
            return lett
        else:
            if n%10==0:
                lett += tenlet[int(str(n)[-2])]
                return lett
            else:
                if int(str(n)[1])==0:
                    lett += numlet[int(str(n)[-1])]
                    return lett
                else:
                    lett += tenlet[int(str(n)[-2])]+numlet[int(str(n)[-1])]
                    return lett
    else:
        lett += numlet[int(str(n)[0])]
        return lett
        
    
        
all =0
for i in range(1,1000):
    all = all + Howmanylet(i)
answer = all + 11
print(answer)    
    