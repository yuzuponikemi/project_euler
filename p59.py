#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:51:02 2018

@author: fiction
p59

Each character on a computer is assigned a unique code and the preferred standard is 
ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on 
the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", 
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method
 is to use a password as a key. If the password is shorter than the message, 
 which is likely, the key is repeated cyclically throughout the message. 
 The balance for this method is using a sufficiently long password key for security,
 but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
 a file containing the encrypted ASCII codes, and the knowledge that the plain 
 text must contain common English words, decrypt the message and find the sum of
 the ASCII values in the original text.

"""

#def tenstobin(n):
#    """ 0<n<1000000"""
#    table=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,1048576,2097152,4194304,8388608]
#    table = table[::-1]
#    binary=[]
#    for ind,val in enumerate(table):
#        if n//val==1:
#            binary.append("1")
#            n -= val
#        else:
#            if binary != []:
#                binary.append("0")
#    return "".join(binary)



f = open('p059_cipher.txt')
data1 = [int(x) for x in f.read().split(',')]
#tex = ""
#for num in data1:
#    tex += num
#texbin = bin(int(tex))[2:]
#lentex = len(texbin)

stop = False
lowers=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for a in lowers:
    for b in lowers:
        for c in lowers:
            out = False
#            key = bin(int(str(ord(a))+str(ord(b))+str(ord(c))))[2:]
#            keyfixed = ''
#            while len(keyfixed) <= lentex:
#                keyfixed += key
#            amari = -lentex +len(keyfixed)
#            keyfixed = keyfixed[:-amari]
            keys = [ord(a),ord(b),ord(c)]
            keyf = []
            while out == False:
                for key in keys:
                    keyf.append(key)
                    if len(keyf)==len(data1):
                        out = True
                        break
            plaintex = ""
            ans=0
            for pl,key in zip(data1,keyf):
                plaintex +=str(chr(pl^key))
                ans += pl^key
            if "the" in plaintex and "and" in plaintex and "be" in plaintex:
                print(str(a)+str(b)+str(c))
                print(ans)
                stop = True
                break
        if stop:
            break
    if stop:
        break
                
            
                
            
            
            