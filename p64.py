#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 00:02:16 2018

@author: fiction
p64


All square roots are periodic when written as continued fractions and can be written in the form:
√N = a0 + 	
1
  	a1 + 	
1
  	  	a2 + 	
1
  	  	  	a3 + ...

For example, let us consider √23:
√23 = 4 + √23 — 4 = 4 +  	
1
	 = 4 +  	
1
  	
1
√23—4
	  	1 +  	
√23 – 3
7

If we continue we would get the following expansion:
√23 = 4 + 	
1
  	1 + 	
1
  	  	3 + 	
1
  	  	  	1 + 	
1
  	  	  	  	8 + ...

The process can be summarised as follows:
a0 = 4, 	  	
1
√23—4
	 =  	
√23+4
7
	 = 1 +  	
√23—3
7
a1 = 1, 	  	
7
√23—3
	 =  	
7(√23+3)
14
	 = 3 +  	
√23—3
2
a2 = 3, 	  	
2
√23—3
	 =  	
2(√23+3)
14
	 = 1 +  	
√23—4
7
a3 = 1, 	  	
7
√23—4
	 =  	
7(√23+4)
7
	 = 8 +  	√23—4
a4 = 8, 	  	
1
√23—4
	 =  	
√23+4
7
	 = 1 +  	
√23—3
7
a5 = 1, 	  	
7
√23—3
	 =  	
7(√23+3)
14
	 = 3 +  	
√23—3
2
a6 = 3, 	  	
2
√23—3
	 =  	
2(√23+3)
14
	 = 1 +  	
√23—4
7
a7 = 1, 	  	
7
√23—4
	 =  	
7(√23+4)
7
	 = 8 +  	√23—4

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?


"""


def g(n,b,c,L,M):
    if (b,c) in M:return L
    if n==b*b: return L
    M.append((b,c))
    C, t = (n-b*b)/c, int(n**0.5)
    u = (b+t)%C
    A = ((b+t))//C
    B = t-u
    L.append(A)
    return g(n,B,C,L,M)

def f(n):
    t=0
    for i in range(n+1):
        s = g(i, int(i**0.5), 1, [], [])
        if len(s)%2: t += 1
    return t

n = 10000
print(f(n))

