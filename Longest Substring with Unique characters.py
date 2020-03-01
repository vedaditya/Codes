# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:08:49 2020

@author: Vedaditya
"""
import time

st=input("Enter the string:- ")
def fn(st):
    n=len(set(st))
    for i in range(n,0,-1):
        for j in range(0,len(st)-i):
            if len(set(st[j:j+i]))==len(st[j:j+i]):
                print("length of string is :",i,"and the string is:- ",st[j:j+i])
                break;
        else:
            continue
        break;
        
tm=time.time()
fn(st)    
print(time.time()-tm)
