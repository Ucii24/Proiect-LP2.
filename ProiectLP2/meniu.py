from tkinter import *
from tkinter import ttk

from ProiectLP2 import grafic, interfata_calendar

# creaza o instanta de cadru sau fereastră tkinter
win= Tk()

#setarea geometrica
win.geometry("750x250")

#definim functia pentru a deschide fereastra
def open_win1():
   return interfata_calendar.calendar()

def open_win2():
   return grafic.grafic()

#creaza label-ul
Label(win, text= "Alege ce vrei sa afiseze", font= ('Helvetica 17 bold')).pack(pady=30)
#creaza un buton pentru a deschide o fereastra noua
ttk.Button(win, text="Calendar", command=open_win1).pack()
ttk.Button(win, text="Grafic", command=open_win2).pack()
win.mainloop()

