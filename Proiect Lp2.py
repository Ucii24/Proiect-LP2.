from tkinter import *
from tkcalendar import Calendar

# Se creaza interfata
root = Tk()

# Setam Dimensiunea interfetei
root.geometry("800x600")

# Adaugam Calendarul
cal = Calendar(root, selectmode = 'day',
               year = 2022, month = 5,
               day = 25)

cal.pack(pady = 20)

def grad_date():
    date.config(text = "Data selectata este: " + cal.get_date())

# Adaugare buton + eticheta
Button(root, text = "Alege Data",
       command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Executam libraria Tkinter
root.mainloop()
