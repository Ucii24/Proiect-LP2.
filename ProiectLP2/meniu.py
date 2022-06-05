#Import tkinter library
from tkinter import *
from tkinter import ttk

from ProiectLP2 import grafic, interfata_calendar

#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a new function to open the window

def open_win1():
   return interfata_calendar.calendar()

def open_win2():
   return grafic.grafic()

#Create a label
Label(win, text= "Alege ce vrei sa afiseze", font= ('Helvetica 17 bold')).pack(pady=30)
#Create a button to open a New Window
ttk.Button(win, text="Calendar", command=open_win1).pack()
ttk.Button(win, text="Grafic", command=open_win2).pack()
win.mainloop()
