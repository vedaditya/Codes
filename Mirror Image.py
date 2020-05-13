# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:22:12 2020

@author: aryavedaditya

question link:- https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/mirror-image-2/
"""

dic={}
mirror={'1':'1'}
n,q=map(int,input().split())
for i in range(1,n):
    a=input().split()
    if a[0] not in dic:
        dic[a[0]]=[0,0]
    if a[-1]=='L':
        mirr=(mirror[a[0]])+'R'
        dic[a[0]][0]=a[1]
        mirror[a[1]]=mirr
    else:
        mirr=str(mirror[a[0]])+'L'
        dic[a[0]][1]=a[1]
        mirror[a[1]]=mirr
#print(dic,mirror)

for _ in range(q):
    number=input()
    if number==1:
        res='1'
        print(res)
        continue
    if number in mirror:
        temp=mirror[number][1:]
        child='1'
        for i in temp:
            if child =='0' or child not in dic:
                child='0'
                break;
            child=str(dic[child][0]) if i=='L' else str(dic[child][1])

    if child!='0':
        res=str(child) 
    else :
        res='-1'
    print(res)

