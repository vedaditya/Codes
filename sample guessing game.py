# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:16:29 2020

@author: aryav
"""
import random
def guessing_game():
    jackpot=random.randint(1,100)
    guess=int(input("Guess the number:- "))
    counter=1
    while(True):
        if guess>jackpot:
            print("Guess Lower")
        elif guess==jackpot:
            print("You got the jackpot in ",counter,"times")
            break;
        else:
            print("Guess higher")
        counter+=1
        guess=int(input("Guess again"))

guessing_game()
