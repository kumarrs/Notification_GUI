#!/usr/bin/python3
import webbrowser
from tkinter import *
import smtplib,ssl 
from email.mime.text import MIMEText
import smtplib
import email.utils
import sys
import os
import getpass

import time
import datetime

uname = getpass.getuser()
root= Tk()
root.title("Pop-Up Notification for PUNCH-OUT")
root.configure(background="#EEEEEE")
root.geometry("600x400+400+350")

"""Amazon Icon for po-up Window"""

icon= PhotoImage(file='/usr/share/icons/ubuntu-mobile/apps/240/amazon.png')
root.tk.call('wm', 'iconphoto',root._w, icon)


label=Label(root,text="Hi  "+uname+",  It's 6.00PM. Click \'yes\' to punch-out \n or \n Click \'NO\' to Punch-OUT Later", font= "Times 18 bold ",fg='RED',bg="WHITE")   #bg="#EEEEEE , fg="#555555""
label.pack()




def link(event):
    #browser = webdriver.Chrome()
    #browser.get 
    url="https://www.amazon.com/"
    webbrowser.open(url)
    root.quit()
    
    
    """time.sleep(3)	
    roo=webbrowser.find_element_by_link_text("Try Prime")
    roo.click()	#//td/a[@id='ess.recordTimestampButton.Label']"""



def mail():
    
    msg = MIMEText('Hi Mr.X, '+uname+' is staying back to complete his work')
    msg['Subject'] = "Extended Reason"
    msg['from'] = 'kumarrs@amazon.com'
    msg['To'] = 'kumarrs@amazon.com'
    s = smtplib.SMTP('localhost')
    s.sendmail('kumarrs@amazon.com',['kumarrs@amazon.com'],msg.as_string())
    s.quit
    print("Mailed Successfully")
    root.quit()


def dialog_box():
    root1= Tk()
    root1.title("Additional Details for Staying-Back")
    root1.configure()
    #root1.geometry("200x100+400+350")s

    #frame_1= Frame(root1,width=200,height=100).pack(side=BOTTOM)
    label_1=Label(root1,text='Reason for Extension').pack()
    label_2=Label(root1,text='No.of Hours needed to finish your TASK').pack()
    entry_1 = Entry(root1).pack()
    entry_2 = Entry(root1).pack()    


    label_1.grid(row=0,column=0)
    label_2.grid(row=1,column=0)
    
    entry_1.grid(row=0,column=1)
    entry_2.grid(row=1,column=1)
    
    
    root1.mainloop()
    root1.quit


button1= Button(root,text="yes")
button1.bind("<Button-1>",link)
button1.pack()

button2= Button(root,text="No",command=mail)
button2.bind("<Button-2>",mail)
button2.pack()

button3= Button(root,text="Check",command=dialog_box)
button3.bind("<Button-3>",dialog_box)
button3.pack()


root.mainloop()

