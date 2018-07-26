#!/usr/bin/python3

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import smtplib,ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import email.utils
import sys
import os
import getpass
import time
import pymongo 

Time=time.strftime("%d-%m-%Y",time.gmtime())
uname = getpass.getuser()


root=Tk()
root.title('DA OT Portal')



root.geometry("600x300+650+250")

icon= PhotoImage(file='/usr/share/icons/ubuntu-mobile/apps/240/amazon.png')
root.tk.call('wm','iconphoto',root._w, icon)




    

label_1= Label(root,text='Reason for staying Back :',font= "Times 18 bold",fg="BLACK")
label_1.grid(row=0,column=0)

global lable_2
lable_2= Entry(root)
lable_2.grid(row=0,column=1)



label_3= Label(root,text='Extending time (in Hours)',font= "Times 18 bold",fg="BLACK")
label_3.grid(row=1,column=0)

global label_4
lable_4= Entry(root)
lable_4.grid(row=1,column=1)

def quit():
    root.quit()

def mail():
    Reason = str(lable_2.get())
    Hours = str(lable_4.get())
    
        
    Client = pymongo.MongoClient("mongodb://admin:password@127.0.0.1:27017") #mongodb://admin:password@localhost:27017/

    mydb = Client["Final"]

    mycol=  mydb[Time]
    mydict= {"name":uname,"hours":Hours,"reason":Reason}
    x = mycol.insert(mydict)
    print(x)
    root.quit()

btn_1 =Button(root,text='Submit',font="Times 18 ",fg="BLACK",command=mail)
btn_1.bind()
#btn_1.grid(row=2,column=1)
btn_1.grid()

btn_2 =Button(root,text='cancel',font="Times 18 ",fg="BLACK",command=quit)
#btn_2.grid(row=3,column=1)
btn_2.grid()

#root.after(10000,lambda:root.quit())
root.mainloop()

