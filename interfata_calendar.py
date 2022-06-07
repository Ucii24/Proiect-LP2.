from tkinter import *
from tkcalendar import Calendar

from pathlib import Path
from urllib.request import *
import json

def calendar():
    nume_fisier = "ProiectLp2.json"

    url = "https://covid19.primariatm.ro/istoric-covid19-tm.json"

    file_name = Path("ProiectLp2.json")

    try:
        if file_name.exists():

            f = open("ProiectLp2.json")

        else:
            print('Fisierul nu exista!')
            response = urlopen(url)
            data_json = json.loads(response.read())
            print("Fisierul trebuie descarcat!")
            with open(nume_fisier, 'w') as outf:
                 json.dump(data_json, outf, indent = 4)
            print('Fisierul a fost descarcat!')

        with open('ProiectLp2.json', 'r') as date:
            data = json.load(date)

    except:
        print('Eroare!')

    #----------------------------------------------------------------------------------------------------------------------

    # Se creaza interfata
    root = Tk()

    # Setam Dimensiunea interfetei
    root.geometry("300x400")

    # Adaugam Calendarul
    cal = Calendar(root, selectmode = 'day',
                   year = 2021, month = 4,
                   day = 20)

    cal.pack(pady = 20)

#cal get date - luna/zi/an // json -> an/luna/zi

    def grad_date():

        datap = cal.get_date()

        x = str(datap)

        if x[1] == '/':

            if x[3] == '/':
                zi = x[2]
                an = '20' + x[4:]
            else:
                zi = x[2:4]
                an = '20' + x[5:]
            luna = x[0]

        else:
            if x[4] == '/':
                zi = x[3]
                an = '20' + x[5:]
            else:
                zi = x[3:5]
                an = '20' + x[6:]
            luna = x[0:2]

        if int(zi) < 10:
            zi = '0' + zi
        if int(luna) < 10:
            luna = '0' + luna

        datac = an + '-' + luna + '-' + zi


        with open('ProiectLp2.json', 'r') as f:
            data = json.load(f)

        gasit = 0
        for i in list(data):

            if i['data'] == datac:
                try:
                    date.config(text = f"Cazuri :  {str(i['cazuri'])}\nRata este : {str(i['rata'])}")
                except:
                    date.config(text = f"Cazuri :  {str(i['cazuri'])}\nPe aceasta data nu a fost intregistrata o rata")
                gasit = 1
                break
        if gasit == 0:
            date.config(text = f"!DATA NEINREGISTRATA!")



    # Adaugare buton + eticheta
    Button(root, text = "Confirma data selectata",
           command = grad_date).pack(pady = 20)

    date = Label(root, text = "")
    date.pack(pady = 20)

    # Executam libraria Tkinter
    root.mainloop()

    return 'calendar - closed'

if __name__ == '__main__':
    print(calendar())
