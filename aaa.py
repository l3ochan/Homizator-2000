# =====Initialisation=====
#Format jour
day = 24
month = 12
year = 2004
date = (day,month,year)

#Format temps
hours = 12
minutes = 57
seconds = 56
time = (hours,minutes,seconds)

#Format sensor
sensorID = "FfFF6f"
value = 45.2

#Types de données, stockage sous forme de 
#dictionnaire pour identifier les données par un id
datatype = 1
datatypes = {
    0 : "null",
    1 : "Temperature",
    2 : "Luminosité",
    3 : "Taux d'humidité",
    4 : "Niveau de CO2",
    5 : "Qualité de l'air",
    6 : "Niveau sonore", 
    7 : "Pression atmosphérique",
    8 : "Consommation d'énergie" 
}


#Format stockage des données (pour le moment)
main_data = [date, time, sensorID, value, datatypes[datatype]]

def add_data():
    date_box = input("Donne date avec ce format jj:mm:aaaa")
    day,month,year = date_box.split('/')
    day = int(day)
    month = int(month)
    year = int(year)