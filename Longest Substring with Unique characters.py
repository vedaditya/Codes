"""
Created on Sun Mar  1 23:08:49 2020

@author: Vedaditya
"""
import time

st=input("Enter the string:- ")
def fn(st):                                 #This function will print the longest substring 
    n=len(set(st))                          #Counting the number of unique characters in string 
    for i in range(n,0,-1):                 #Max possible length of substring will be equal to unique numbers in string(n), so we are
                                                      #  searching only for substring having length less than n
        for j in range(0,len(st)-i):
            if len(set(st[j:j+i]))==len(st[j:j+i]):
                print("length of string is :",i,"and the string is:- ",st[j:j+i])
                break;
        else:
            continue
        break;                      #Breaking the Outer loop only if inner loop is inner loop doesn't complete 
        
tm=time.time()
fn(st)    
print(time.time()-tm)               #printing the time required for giving the output. It may varry with machines or compilers.
