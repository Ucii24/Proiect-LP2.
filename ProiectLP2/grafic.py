from pathlib import Path
from urllib.request import *
import json
import matplotlib.pyplot as plt
from datetime import *

def grafic():
    nume_fisier = "ProiectLp2.json"

    url = "https://covid19.primariatm.ro/istoric-covid19-tm.json"

    file_name = Path("ProiectLp2.json")

    if file_name.exists():
        #print("Fisierul exista!")
        f = open("ProiectLp2.json")
        #for line in f:
        #print(line)

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

            plt.plot([y,x])

    #plt.plot([1,2,3,4])
    plt.xlabel('x - Cazurile Covid ')
    #plt.xlim(1,32)

    plt.ylabel('y - Zile')

    plt.title('Cazuri covid ')


    plt.show()

    return 'Grafic - closed'

if __name__ == '__main__':
    print(grafic())

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# use seaborn style
#sns.set_theme()

# create data
#values=np.cumsum(np.random.randn(1000,1))

# use the plot function
#plt.plot(values)

# show the graph
#plt.show()
