#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:43:09 2018

@author: fiction
p24

A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic[辞書] permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

"""first solution"""
#from itertools import permutations
#perms = ["".join(p) for p in permutations('0123456789')]
#print(perms)
#print(perms[999999])


"""second solution"""



def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        return "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet 
        #(now it's index will begin with step + 1)
        permutations(string_copy, step + 1)


def make_perm_loop():
    """
    単純なプログラム
    関数定義中にループが増えると煩雑になるため再帰定義のほうがよい場合のひとつ
    """
    perm = []
    # 1 番目の数字を選ぶ
    for a in range(1, 5):
        perm.append(a)
        # 2 番目の数字を選ぶ
        for b in range(1, 5):
            if b in perm: continue
            perm.append(b)
            # 3 番目の数字を選ぶ
            for c in range(1, 5):
                if c in perm: continue
                perm.append(c)
                # 4 番目の数字を選ぶ
                for d in range(1, 5):
                    if d in perm: continue
                    perm.append(d)
                    print(perm)
                    perm.pop()
                perm.pop()
            perm.pop()
        perm.pop()




# 順列を格納するリスト
perm = []
anslist=[]
# 順列の生成
def make_perm(n, m = 0):
    """
     関数 make_perm(n) は、1 から n までの順列を生成します。考え方は繰り返し版と同じで、
     数字を選んでリスト perm に追加します。perm はグローバル変数ですが、perm の値を更新するのではなく、
     リストを更新しているので global 宣言しなくても動作します。あとは perm にはない数字を選んでいきます。
     最初の呼び出しで 1 つの数字を選び、次の再帰呼び出しで 2 つめの数字を選びます。
     このように、n 重のループが n 回の再帰呼び出しに対応するわけです。
     引数 m は選んだ数字の個数をカウントします。n と m が等しい場合は n 個の数字を選んだので 
     perm を出力します。ここで n 番目の再帰呼び出しが終了し、n - 1 番目の再帰呼び出しに戻ります。
     そのあとは、pop() で選んだ数字を削除して新しい数字を選びます。
     もしも選ぶ数字がなければ、n - 2 番目の再帰呼び出しに戻り、n - 2 番目の数字を選び直します。
     これで 1 から n までの順列をすべて生成することができます。 
     """
    if n == m:
        anslist.append(perm)
    else:
        for x in range(1, n + 1):
            if x in perm: continue
            perm.append(x)
            make_perm(n, m + 1)
            perm.pop()




