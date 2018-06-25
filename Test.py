#!/usr/bin/python3
import webbrowser
from tkinter import *
import sys
import os
import getpass
import time
from datetime import datetime
from datetime import timedelta
import gi
from tkinter import ttk
import threading
gi.require_version('Notify','0.7')

from gi.repository import Notify



uname = getpass.getuser()
t=time.strftime('%I:%M %p',time.localtime())

#Creating Main_Window
global win
def win():
    root= Tk()
    root.title("Pop-Up Notification for PUNCH-OUT")
    root.configure()
    root.geometry("600x400+400+350") 


#Amazon Icon for pop-up Window
    #root.wm_iconbitmap('favicon.ico')
    #icon= PhotoImage(file='amazon.png')
    #root.tk.call('wm','iconphoto',root._w, icon) #tk.call

#Content of the Window

    #photo = PhotoImage(file='/usr/share/icons/ubuntu-mobile/apps/144/amazon.png')
    #label = Label(root,image=photo).pack()


    label_1=Label(root,text = "Hi  "+uname ,font= "Times 18 bold",fg="BLACK").pack()

    label_2=Label(root,text= " It's " +t,font= "Times 28 bold",fg="RED" ).pack() 

    label_3=Label(root,text= " \n Do you want to PUNCH_OUT ? \n ",font ='Times 14',fg='BLACK').pack()

    def link(event):
    
        url="https://mytime-lite.aka.corp.amazon.com/wfc/applications/suitenav/navigation.do?ESS=true?redirect=/wfc/applications/wtk/html/ess/timestamp.jsp"
        webbrowser.open(url)
        
        Notify.init('Time_OFF_Notification')
        pop_up=Notify.Notification.new("Hi " +uname+ " !" ,"Click on the 'Record Time Stamp' button to Punch-OUT",'/usr/share/icons/ubuntu-mobile/apps/240/amazon.png')	
        pop_up.show()
        pop_up.set_urgency(2)
        root.quit()        


    def exit():
        
        Notify.init('Time_OFF_Notification')
        pop_up=Notify.Notification.new("Thanks You " +uname+ " !" ,"We will remind you after 5 Minutes",'/usr/share/icons/ubuntu-mobile/apps/240/amazon.png')	
        pop_up.show()
        pop_up.set_urgency(2)

        if (button2 !='normal'):
            two()
            root.withdraw()     

                
            
        
    def two():
        
        root.after(2*4000,lambda:win())
        #root.withdraw()
        #root.after(9000,lambda:root.quit())

    


    button1= Button(root,text="Yes",font="Times 16")
    button1.bind("<Button-1>",link)
    button1.pack()


    button2= Button(root,text="Remind me after 5 Minutes ",font="Times 16",command=exit,state='normal')
    button2.bind("<Button-2>")
    button2.pack()
    
    
    #root.after(20000,lambda:root.quit())
    

    
    root.mainloop()
    root.destroy()   

win()










