print("Welcome to the Homizator 2000")
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
sensor_value = 45.2

#Types de données, stockage sous forme de 
#dictionnaire pour identifier les données par un id
null = 0
temp = 1
lum = 2
hum = 3
co2 = 4
air = 5
son = 6
atm = 7
conso = 8

datatype_dictionnary = {
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

datatype = null

cancel = 0

#Format stockage des données (pour le moment)
main_data = []
main_dataInstant = (date, time, sensorID, sensor_value, datatype_dictionnary[datatype])
#commandes d'aides
def help_datatypes():
    print("Voici les différents types de données enregistrés.")
    print(" ")
    print(" ")
    print("+----------------+-------------------------+-------+-----------------------------------------+")
    print("| Champ datatype | Type de donnée          | Unité | Description                             |")
    print("+----------------+-------------------------+-------+-----------------------------------------+")
    print("| null           | Aucun                   | N/A   | Aucune donnée disponible                |")
    print("| temp           | Température             | °C    | Mesure de la température ambiante       |")
    print("| lum            | Luminosité              | Lux   | Niveau d'éclairage mesuré               |")
    print("| hum            | Taux d'humidité         | %     | Pourcentage d'humidité dans l'air       |")
    print("| co2            | Niveau de CO2           | ppm   | Concentration de CO2 dans l'air         |")
    print("| air            | Qualité de l'air        | AQI   | Indice de qualité de l'air              |")
    print("| son            | Niveau sonore           | dB    | Niveau de bruit ambiant                 |")
    print("| atm            | Pression atmosphérique  | hPa   | Pression de l'air mesurée               |")
    print("| conso          | Consommation d'énergie  | kWh   | Quantité d'énergie consommée            |")
    print("+----------------+-------------------------+-------+-----------------------------------------+")

#Ajotuer manuellement une donnée au tableau
def add_data():
    global cancel
    cancel = 0
    def_date()
    def_time()
    def_sensorData()
    def_datatype()
    if cancel == 1:
        print("quit !")
        return
    main_dataInstant = (date, time, sensorID, sensor_value, datatype_dictionnary[datatype])
    main_data.append(main_dataInstant)
    print("New data has been stored in database.")
    print(main_data[-1])
    print("executez ................... pour voir les données")


def def_date():
    global date, cancel
    date_box = input("Donne date avec ce format jj/mm/aaaa")
    if date_box == "quit":
        cancel = 1
        return
    day,month,year = date_box.split('/') #Séparation des données entrées par l'utilisateur
    day = int(day)
    month = int(month)
    year = int(year)
    if not (1 <= day <= 31):
        print("La date n'est pas comprise entre 1 et 31 ! Merci de réessayer")
        def_date()
        return 
    if not (1 <= month <= 12):
        print("Le mois n'est pas compris entre 1 et 12 ! Merci de réessayer")
        def_date()
        return 
    date = (day,month,year)
    return 
    
def def_time():  
    global time, cancel
    if cancel == 1:
        return
    time_box = input("Donne date avec ce format hh:mm:ss")
    if time_box == "quit":
        cancel = 1
        return
    hours,minutes,seconds = time_box.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if not (1 <= hours <= 24):
        print("Il n'y a que 24h dans une journée ! Merci de réessayer")
        def_time()
        return 
    if not (0 <= minutes < 60):
        print("Les minutes ne sont pas comprises entre 1 et 60 ! Merci de réessayer")
        def_time()
        return 
    if not (0 <= seconds < 60):
        print("Les secondes ne sont pas comprises entre 1 et 60 ! Merci de réessayer")
        def_time()
        return 
    time = (hours,minutes,seconds)
    return 

def def_sensorData():
    global cancel
    if cancel == 1:
        return
    global sensorID, sensor_value, datatype
    sensorID = input("Donne identifiant sensor")
    if sensorID == "quit":
        cancel = 1
        return
    sensor_value = input("donne valeur du capteur")
    if sensor_value == "quit":
        cancel = 1
        return
    datatype = input("Donne type de donnée, executez help_datatypes pour avoir une liste des types de données.")
    if datatype == "quit":
        cancel = 1
        return
    return 

def def_datatype():
    global datatype, cancel
    if cancel == 1:
        return
    datatype = input("Donne type de donnée, executez help_datatypes pour avoir une liste des types de données.")
    if datatype == "quit":
        cancel = 1
        return
    if datatype not in datatype_dictionnary:
        print(f"Type de donnée invalide : {datatype}. Veuillez utiliser un identifiant valide.")
        help_datatypes()
        def_datatype()




# =====friendly commands===== 
# Un dictionnaire associant les commandes de l'utilisateur aux fonctions correspondantes
commands = {
    "help datatypes": help_datatypes,
    "add data" : add_data,
    #Commandes à ajouter
}

def process_command(input_command):
    # Traite l'entrée et appelle la fonction correspondante
    if input_command in commands:
        commands[input_command]()
    else:
        print("Unknown command")
# Boucle principale pour lire les commandes de l'utilisateur
while True:
    user_input = input("Entrez votre commande : ")
    if user_input == "quit":
        break
    process_command(user_input)


print("Goodbye !")