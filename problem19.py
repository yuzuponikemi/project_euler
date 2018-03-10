#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:33:42 2018

@author: fiction
ploblem19


You are given the following information, but you may prefer to do some 
research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century 
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
mokuyou
"""

one = 31*7+30*4+28
leap = one + 1
count = 0
cent21 = list(range(1901,2001))

#(days-4)%7=0==sunday
#for year in cent21:
#    if year%4==0:
#        if year%400!=0:
#            days +=leap
#        else:
#            days +=one
#    else:
#        days += one

month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
lmonth = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
mont = list(month.values())
lmont = list(lmonth.values())


days =1

for year in cent21:
    if year%4==0:
        if year%400!=0:
            for day in lmont:
                
                if (days+1)%7==0:
                    count +=1
                days += day
        else:
            for day in mont:
                
                if (days+1)%7==0:
                    count +=1
                days += day
    else:
        for day in mont:
                
                if (days+1)%7==0:
                    count +=1
                days += day
    
print(count)
