from bs4 import BeautifulSoup
import csv
import requests
import time as time2
from datetime import datetime
# 1 Diesel
# 5 LPG
# 2 E10



def preisabfrage (indexsprit, tankstellenurl) :
    html = requests.get(tankstellenurl).text
    anfangdiesel = f"span id=\"current-price-{indexsprit}\">"
    begin = html.find(anfangdiesel)
    end = html.find("</span>", begin)
    return (html[begin + len(anfangdiesel): end])


T1 = "https://www.clever-tanken.de/tankstelle_details/21974"
T2 = "https://www.clever-tanken.de/tankstelle_details/10063"
T3 = "https://www.clever-tanken.de/tankstelle_details/37955"
T4 = "https://www.clever-tanken.de/tankstelle_details/40018"
print(f"Diesel: {preisabfrage(1,T1)} Maunzi{preisabfrage(5,T1)}")


while (True):
    with open('T1.csv', 'a', newline='') as student_file:
        time = datetime.now()
        writer = csv.writer(student_file)
        # Diesel, Benzin E10, Benzin E5, LPG, Uhrzeit, Tankstelle
        writer.writerow([preisabfrage(1,T1), preisabfrage(2,T1),preisabfrage(3,T1), preisabfrage(5,T1),time , 21974])

    with open('T1.csv', 'a', newline='') as student_file:
        time = datetime.now()
        writer = csv.writer(student_file)
        # Diesel, Benzin E10, LPG, Uhrzeit, Tankstelle
        writer.writerow([preisabfrage(1,T2), preisabfrage(2,T2),preisabfrage(3,T2), preisabfrage(5,T2),time , 10063])

    with open('T1.csv', 'a', newline='') as student_file:
        time = datetime.now()
        writer = csv.writer(student_file)
        # Diesel, Benzin E10, LPG, Uhrzeit, Tankstelle
        writer.writerow([preisabfrage(1,T3), preisabfrage(2,T3),preisabfrage(3,T3), preisabfrage(4,T3),time , 37955])

    with open('T1.csv', 'a', newline='') as student_file:
        time = datetime.now()
        writer = csv.writer(student_file)
        # Diesel, Benzin E10, LPG, Uhrzeit, Tankstelle
        writer.writerow([preisabfrage(1,T4), preisabfrage(2,T4),preisabfrage(3,T4), preisabfrage(6,T4),time , 40018])
    print(f"Übertragen um: {time}")
    time2.sleep(600)


