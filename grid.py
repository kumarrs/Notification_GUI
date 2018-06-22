#!/usr/bin/python3

from tkinter import *
from tkinter import ttk 
import smtplib,ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import email.utils
import sys
import os
import getpass



root=Tk()
root.title('DA OT Portal')



root.geometry("500x300+400+350")

icon= PhotoImage(file='/usr/share/icons/ubuntu-mobile/apps/240/amazon.png')
root.tk.call('wm','iconphoto',root._w, icon)




    

label_1= Label(root,text='Reason for staying Back :',font= "Times 18 bold",fg="BLACK")
label_1.grid(row=0,column=0)

global lable_2
lable_2= Entry(root)
lable_2.grid(row=0,column=1)



label_3= Label(root,text='How long ?? (in Hours)',font= "Times 18 bold",fg="BLACK")
label_3.grid(row=1,column=0)

global label_4
lable_4= Entry(root)
lable_4.grid(row=1,column=1)

def quit():
    root.quit()

def mail():
    ab = str(lable_2.get())
    bc = str(lable_4.get())
    msg = MIMEText('I am staying back due to ' +ab+ '\n I need '+bc+' Hours to complete my task')
    msg['Subject'] = 'OT Tracking Mail:Staying back after 6PM'
    msg['from'] = 'kumarrs@amazon.com'
    msg['To'] = 'kumarrs@amazon.com'
    s = smtplib.SMTP('localhost')
    s.sendmail('kumarrs@amazon.com',['kumarrs@amazon.com'],msg.as_string())
    s.quit
    print("Mailed Successfully")
    root.quit()

btn_1 =Button(root,text='Submit',font="Times 18 ",fg="BLACK",command=mail)
btn_1.bind(mail)
#btn_1.grid(row=2,column=1)
btn_1.grid()

btn_2 =Button(root,text='cancel',font="Times 18 ",fg="BLACK",command=quit)
#btn_2.grid(row=3,column=1)
btn_2.grid()


root.mainloop()