#!/usr/bin/python3
import webbrowser
from tkinter import *
import sys
import os
import getpass
import time
from datetime import datetime
import gi
from tkinter import ttk
import threading
gi.require_version('Notify','0.7')
from gi.repository import Notify



uname = getpass.getuser()

#Main_Window
global win
def win():
    root= Tk()
    root.title("PUNCH-OUT Reminder")
    root.configure()
    root.geometry("600x300+650+250") 
    

#Label_Content
    label_1=Label(root,text = "Hey "+uname+ " ! ! ! " ,font= "Times 18 bold",fg="BLACK").pack()

    label_2=Label(root,text= " It's 6 o'Clock "  ,font= "Times 30 bold",fg="RED" ).pack() 

    label_3=Label(root,text= " \n Do you want to PUNCH_OUT ? \n ",font ='Times 14',fg='BLACK').pack()

    def link(event):
    
        url="https://mytime-lite.aka.corp.amazon.com/wfc/applications/suitenav/navigation.do?ESS=true?redirect=/wfc/applications/wtk/html/ess/timestamp.jsp"
        webbrowser.open(url)
        root.quit()
        
        Notify.init('Time_OFF_Notification')
        pop_up=Notify.Notification.new("Hi " +uname+ " !" ,"Click on the 'Record Time Stamp' button to Punch-OUT",'/home/local/ANT/kumarrs/Aces/amazon.png')	
        pop_up.show()
        pop_up.set_urgency(2)
                
    def disable_event():
        pass

    def exit():
        
        Notify.init('Time_OFF_Notification')
        pop_up=Notify.Notification.new("Thanks You " +uname+ " !" ,"We will remind you after 5 Minutes",'/home/local/ANT/kumarrs/Aces/amazon.png')	
        pop_up.show()
        pop_up.set_urgency(2)

        if (button2 !='normal'):
            root.after(300000,lambda:win())
            root.withdraw()     
           
                
#Button_creation        
    button1= Button(root,text="Yes",font="Times 16")
    button1.bind("<Button-1>",link)
    button1.pack()


    button2= Button(root,text="Remind me after 5 Minutes ",font="Times 16",command=exit,state='normal')
    button2.bind("<Button-2>")
    button2.pack()
    
    root.protocol("WM_DELETE_WINDOW",disable_event)
    root.mainloop()
    root.quit()  

win()










