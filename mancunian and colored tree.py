# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:11:03 2020

@author: aryavedaditya 

question link:- https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/mancunian-and-colored-tree/
"""

from collections import defaultdict
from sys import stdin
n,c=map(int,stdin.readline().split())
tree=[0,0]
tree.extend(list(map(int,stdin.readline().split())))
colourlist=list(map(int,stdin.readline().split()))
colourdic=defaultdict()
for i in range(len(colourlist)):
    colourdic[i+1]=colourlist[i]
res='-1 '
for i in range(2,n+1):
    colour=colourdic[i]
    node=tree[i]
    while colourdic[node]!=colour:
        node=tree[node]
        if node==0:
            node =-1
            break;
    res+=str(node)+' '
print(res)