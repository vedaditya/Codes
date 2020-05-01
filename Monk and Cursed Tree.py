# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:56:27 2020

@author: aryavedaitya
"""

"""
The link of problem is given below:
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-cursed-tree/
"""


import sys
sys.setrecursionlimit(9999)
class nodes():
    def __init__(self,n):
        self.data=n
        self.left=None
        self.right=None
input()
class BST():
    def add(self,node,b):
        if node.data>b.data:
            if b.right!=None:
                self.add(node,b.right)
            else:
                b.right=node
        else:
            if b.left!=None :
                self.add(node,b.left)
            else:
                b.left=node

    def __init__(self):
        array=list(map(int,input().split()))
        self.bst=nodes(array[0])
        for i in array[1:]:
            n=nodes(i)
            self.add(n,self.bst)
        x,y=map(int,input().split())
        self.ma=max(x,y)
        a=self.bst
        while True:
            if (x>a.data and y>a.data):
                a=a.right
            elif (x<a.data and y<a.data):
                a=a.left
            else:
                break;
        self.trav(x,a)
        self.trav(y,a)
        print(self.ma)

    def trav(self,a,b):
        if a>b.data:
            self.ma=max(self.ma,b.data)
            self.trav(a,b.right)
        elif a<b.data:
            self.ma=(max(self.ma,b.data))
            self.trav(a,b.left)
        
BST()