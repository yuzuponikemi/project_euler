# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file 

perindromic number ex) 9009=91*99 
[Find the largest peridrome made from the product of two 3-digit numbers]
"""
check = 0

list1 = range(0,1000)
list2 = range(0,1000)
list1 = list1[::-1]
list2 = list2[::-1]
peridromlist=[]
for i in list1:
    for k in list2:
        check = i*k
        strcheck = str(check)
        reverse = strcheck[::-1]
        if strcheck == reverse:
            print(i,k,check)
            peridromlist.append(check)

answer = max(peridromlist)
print("answer is "+str(answer))
            
        

