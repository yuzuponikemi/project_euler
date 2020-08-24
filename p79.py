#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:08:11 2018

@author: fiction
p79


A common security method used for online banking is to ask the user 
for three random characters from a passcode. 
For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret passcode of unknown length.


手で解いた　73162890
"""

f = open('p079_keylog.txt')
attempts = [x[:-1] for x in f.readlines()]

ansls =[]
posls =[]
for attempt in attempts:
    one = attempt[:2]
    two = attempt[1:]
    
    