"""
Created on Mon Jan 27 13:55:12 2020

@author: aryav
"""

from tkinter import *
import requests
class irctc:
    def __init__(self):
        self.root =Tk()
        self.root.title("IRCTC")
        self.root.minsize(500,800)
        self.root.maxsize(500,800)
        
        self.root.configure(background="#166353")
        
        
        self.label1=Label(self.root,text="Train route",bg='#166353',fg='#ffffff')
        self.label1.configure(font=("Constantia",20,'bold'))
        self.label1.pack(pady=(30,10))
        
        self.trainNo=Entry(self.root)
        self.trainNo.configure(font=(0))
        self.trainNo.pack(ipady=10)
        
        
        self.click=Button(self.root,text="Fetch station",width=29,height=2,command=lambda:self.fetch())
        self.click.pack(pady=(15,15))
        
        
        
        self.result=Label(self.root,bg='#166353',fg='#ffffff')
        self.result.configure(font=("Constantia",10,'bold'))
        self.result.pack(pady=(30,10))
        
        
        self.root.mainloop()
    def fetch(self):
        train_no=self.trainNo.get()
        url='https://api.railwayapi.com/v2/route/train/{}/apikey/**********/'.format(train_no)
        data=requests.get(url)
        response=data.json()
        lis=''
        for i in response['route']:
            
            lis=lis+(i['station']['name'])+' | '
            lis=lis+str(i['scharr'])+' | '
            lis=lis+str(i['schdep'])+' | '
            lis+=str(i['distance'])+"Km \n"
            
            
            
        self.result.configure(text=lis)
obj=irctc()
