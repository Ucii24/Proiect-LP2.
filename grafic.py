from pathlib import Path
from urllib.request import *
import json
import matplotlib.pyplot as plt

def grafic():
    nume_fisier = "ProiectLp2.json"

    url = "https://covid19.primariatm.ro/istoric-covid19-tm.json"

    file_name = Path("ProiectLp2.json")

    if file_name.exists():

        f = open("ProiectLp2.json")


    else:
        response = urlopen(url)
        data_json = json.loads(response.read())
        print("Fisierul trebuie descarcat!")
        with open(nume_fisier, 'w') as outf:
             json.dump(data_json, outf, indent = 4)

        #print(data_json)
        print('Fisierul a fost descarcat!')

    with open('ProiectLp2.json', 'r') as date:
        data = json.load(date)

    for cazuri in list(data)[:5]:

        y = int(cazuri['cazuri'])
        for zile in list(data)[:5]:
            x = int(zile['data'][-2:])


            plt.plot([y],[x],'o')



    plt.xlabel('x - Zile ')


    plt.ylabel('y - Cazuri')

    plt.title('Cazuri covid ')


    plt.show()

    return 'Grafic - closed'

if __name__ == '__main__':
    print(grafic())

