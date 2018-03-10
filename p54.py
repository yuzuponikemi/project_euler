#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:28:40 2018

@author: fiction
p54


In the card game poker, a hand consists of five cards and are ranked,
 from lowest to highest, in the following way:

    High Card: Highest value card.50
    One Pair: Two cards of the same value.200
    Two Pairs: Two different pairs.400
    Three of a Kind: Three cards of the same value.450
    Straight: All cards are consecutive values.500
    -Flush: All cards of the same suit.600
    Full House: Three of a kind and a pair.650
    Four of a Kind: Four cards of the same value.800
    -Straight Flush: All cards are consecutive values of same suit.1100
    -Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.1100+100

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest 
value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
 But if two ranks tie, for example, both players have a pair of queens, 
 then highest cards in each hand are compared (see example 4 below); 
 if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
	 	2C 3S 8S 8D TD
Pair of Eights
	 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
	 	2C 5C 7D 8S QH
Highest card Queen
	 	Player 1
3	 	2D 9C AS AH AC
Three Aces
	 	3D 6D 7D TD QD
Flush with Diamonds
	 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
	 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
	 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
	 	3C 3D 3S 9S 9D
Full House
with Three Threes
	 	Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
 the first five are Player 1's cards and the last five are Player 2's cards. 
 You can assume that all hands are valid (no invalid characters or repeated cards),
 each player's hand is in no specific order, 
 and in each hand there is a clear winner.

How many hands does Player 1 win?

"""
table={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,\
'T':10,'J':11,'Q':12,'K':13,'A':14}



def flash(p):
    color = set()
    for card in p:
        color.add(card[-1])
    if len(color)==1:
        return True
    else:
        return False



def straight(p):
    if p[0]+4 == p[1]+3 == p[2]+2 == p[3]+1 == p[4]:
        return True
    else:
        return False
    
    
def count(p):
    score = 0
    pdic={}

    for c in p:
        if p.count(c)!=1:
            pdic[c]=p.count(c)
    for pair in pdic.values():
        if pair == 2:
            score += 200
        if pair == 3:
            score += 450
        if pair == 4:
            score == 800

    return score,pdic
            
        
    


    
    
    
f = open('p054_poker.txt')
data1 = f.readlines()  # ファイル終端まで全て読んだデータを返す
f.close()
data1=[x[:-1] for x in data1]

p1win =0
p2win = 0
for match in data1:
    out = False
    p1score=0
    p2score=0
    p1s = match[:14].split()
    p2s = match[15:].split()
    p1 = sorted([table[x[0]] for x in p1s])
    p2 = sorted([table[x[0]] for x in p2s])
    if flash(p1s):
        p1score +=600+max(p1)
    if flash(p2s):
        p2score +=600+max(p2)
    if straight(p1):
        if p1score == 600:
            if sum(p1)== 60:
                p1win += 1
                continue
        p1score += 500+max(p1)
    if straight(p2):
        if p2score >= 600:
            if sum(p2)== 60:
                p2win += 1
                continue
        p2score += 500+max(p2)
    p1c,p1dic = count(p1)
    p2c,p2dic = count(p2)
    p1score += p1c
    p2score += p2c
    if p1score > p2score:
        p1win +=1
        continue
    if p1score < p2score:
        p2win+=1
        continue
    if p1score!=0 and p1dic.values()!=[2,2]:
        for p1d,p2d in zip(sorted(p1dic.items(), key=lambda x: -x[1]),sorted(p2dic.items(), key=lambda x: -x[1])):
            if p1d[0]>p2d[0]:
                p1win+=1
                out = True
                break
            elif p1d[0]<p2d[0]:
                p2win+=1
                out = True
                break
            else:
                continue
    if p1dic.values()== [2,2]:
        for p1d,p2d in zip(sorted(p1dic.items()).reverse(),sorted(p2dic.items()).reverse()):
            if p1d[0]>p2d[0]:
                p1win+=1
                out = True
                break
            elif p1d[0]<p2d[0]:
                p2win+=1
                out = True
                break
            else:
                continue
            
    if out:
        continue
    p1.reverse()
    p2.reverse()
    for p1n,p2n in zip(p1,p2):
        if p1n>p2n:
            p1win+=1
            out = True
            break
        elif p1n<p2n:
            p2win+=1
            out = True
            break
        else:
            continue
    if out:
        continue
    if True:
        print("warning!")
        break
        
        
            
            
        
        
        
        
        
        
    
    
    
    
    
    
            
            
    
    

