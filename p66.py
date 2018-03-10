#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 00:03:13 2018

@author: fiction
p66


Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1
x^2 = 1+ Dy^2

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, 
the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
value of x is obtained.

"""
##これも微妙　大きなリストよりも逐一チェックのほうが早い
#posx2=[]
#for x in range(0,100000000):
#    posx2.append(x**2)
#    


"""
正解をだすためには x,yの範囲を10000以上にしなければならないが、非常に時間がかかってしまう
largestx=1
ans=0
for d in range(0,1001):
    if int(d**0.5)==d**0.5:
        continue
    out = True
    for y in range(1,100000000):
        x2 = 1+d*y**2
        if int(x2**0.5)==x2**0.5:
            okx = x2**0.5
            print(d,okx)
            out = False
            break
    if out:
        print("warning!!")
        input()
    if okx > largestx:
        largestx=okx
        ans = d

#print(ans)！２９で不正解だった　５分かかったのに

"""

#これも間違い
#場合分けが不十分

#solution
#(x+1)(x-1)=Dy^2　　　　　→D=3のみ
#        = D * y^2　　　　→D=2,3のみ
#        = Dy * y　　　　　→　これで考える
#        で場合分け
#
#"""
#D != 2,3では
#1,
#x = D - 1
#y^2 = D - 2
#2,
#x = D + 1
#y^2 = D + 2
#の二通りしかありえない
#これで各Dに対して二回の計算でxを計算できるようになった
#"""
#largestx=1
#ans=0
#for d in range(4,1001):
#    x=0
#    one = d-2
#    two = d+2
#    if int(one**0.5)==one**0.5:
#        x = d-1
#    if int(two**0.5)==two**0.5:
#        x = d+1
#        
#    if x>largestx:
#        largestx=x
#        ans=d
#print(ans)
        




"""
D = (x-1)/y * (x+1)/yなどをかんがえると、
Dの約数の組(a,d)　a<b　で組み合わせを考えられる   
　　　　=>これもちがう　D=5,x=9の場合を考えてみる必要がある
"""
#
#largestx = 1
#ans=0
#smallestx=100
#for d in range(5,1001):
#    ab=[]
#    smallestx=1000
#    for i in range(1,int(d**0.5)):
#        if d%i==0:
#            ab.append((i,int(d/i)))
#    for tu in ab:
#        a,b = tu[0],tu[1]
#        one = (b-2)/a
#        two = (b+2)/a
#        if int(one**0.5)==one**0.5:
#            xone = b-1
#            if xone<smallestx:smallestx=xone
#        if int(two**0.5)==two**0.5:
#            xtwo = b+1
#            if xtwo<smallestx:smallestx=xtwo
#        if (b+a)%(b-a)==0:
#            xthree = (b+a)/(b-a)
#            if xthree<smallestx:smallestx=xthree
##    if smallestx > largestx:
##         largestx = smallestx
##         ans = d
#    print('D:'+str(d)+'  smallestx:'+str(smallestx))
#    
#
#print(ans)
#        
"""#wikipediaより
平方数でない正の整数 n に対してペル方程式は必ず自明な解 (x = 1, y = 0) 以外の整数解を持つことが知られている。
また1つの解 (x, y) を得たとすれば、

    x k + y k sqrt(n) = ( x + y n )^k 

は全てペル方程式の解になる。また逆にペル方程式の全ての解は最小解の冪乗になることが知られている。

最小解を得る法としては、連分数展開からの近似分数を利用する方法が良く用いられる。

具体的には、√n の連分数展開を、√n = A = [a0; a1, a2, ..., am] と置き、
近似分数P/Qを、P/Q = B = [a0; a1, a2, ..., am − 1]とすると、(x, y) = (P, Q) が解になる。
但し、周期 m が奇数の場合は、右辺 = −1 の解が得られるので、1 の解を得るには上記の式で二乗する必要がある。
ここで、A はa0 を整数部分、a1, a2, ..., am を循環節とする無限連分数で、B は循環節を一周期だけ採り、
最後の項amを除いた、有限連分数である。ちなみに、a1, a2, ..., am − 1は左右対称となっており、am = 2a0 が常に成立する。

ｎ＝＝Dとしてこの問題に適用できる
例えば n が 7 ならば、√7 = [2; 1, 1, 1, 4] (周期は 4 で偶数) なので、[2; 1, 1, 1] から近似分数 8/3 
が得られ、(x, y) = (8, 3) が最小解となる。n が 61 の場合は 、 
sqrt61 = [ 7 ; 1 , 4 , 3 , 1 , 2 , 2 , 1 , 3 , 4 , 1 , 14 ] (
周期は 11 で奇数) なので近似分数 29718/3805 が得られ、右辺 = −1 の最小解は 
( x 1 , y 1 ) = ( 29718 , 3805 ) となる。
右辺 = 1 の最小解は、 x + y sqrt(61) = ( x 1 + y 1 sqrt(61) )^2 から (x, y) = (1766319049, 226153980) となる。

解の公式から

    α = x + y n , β = x − y n 
とおくと、

    x k = ( α k + β k ) / 2 , y k = ( α k − β k ) / ( 2 n ) 
が得られる。つまり、ペル方程式の解に対して、yk/y, 2xk はリュカ数列を構成する。
"""        
import sys
sys.setrecursionlimit(10000)
from fractions import Fraction as Fr

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

def any_expansion(n,ls,k):
    now = Fr(int(ls[n-1]))
    for i in range(1,n):
        now = Fr(1,now) + int(ls[n-1-i])
    ans = 1/now+k
    return ans.numerator,ans.denominator


def f(n):
    best=0
    ans=0
    for i in range(2,n+1):
        if int(i**0.5)==i**0.5:
            continue
        k=int(i**0.5)
        s = g(i, int(i**0.5), 1, [], [])
        print(s)
        if len(s)==1:
            j = 1
            se = s
        else:
            j= len(s)-1
            se = s[:-1]
        x,y = any_expansion(j,se,k)
        print(x,y,k)
        if len(s)%2 and len(s)!=1:
            x1 = x**2 + i*y**2
            y1 = 2*x*y
            print(i,x1,y1)
            if x1**2 - i*y1**2!=1:
                print('shit')
            if x1>best:
                best = x1
                ans=i
        else:
            if x**2 - i*y**2!=1:
                print('shit')
            print(i,x,y)
            if x>best:
                best = x
                ans=i
    return best,ans

n = 1000
print(f(n))