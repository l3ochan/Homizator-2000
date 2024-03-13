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






#Format stockage des données (pour le moment)
main_data = [date, time, sensorID, sensor_value, datatype_dictionnary[datatype]]

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
    def_date()
    def_time()
    def_sensorData()
    main_data.append[date, time, sensorID, sensor_value, datatype_dictionnary[datatype]]
    print("New data has been stored in database.")
    print(main_data[-1])
    print("executez ................... pour voir les données")


def def_date():
    date_box = input("Donne date avec ce format jj/mm/aaaa")
    day,month,year = date_box.split('/') #Séparation des données entrées par l'utilisateur
    day = int(day)
    month = int(month)
    year = int(year)
    if day > 31 or day < 1:
        print("La date n'est pas comprise entre 1 et 31 ! Merci de réessayer")
        def_date()
        return None
    if month > 12 or month < 1:
        print("Le mois n'est pas compris entre 1 et 12 ! Merci de réessayer")
        def_date()
        return None
    def_time
    
def def_time():  
    time_box = input("Donne date avec ce format hh:mm:ss")
    hours,minutes,seconds = time_box.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if hours > 24 or day < 1:
        print("Il n'y a que 24h dans une journée ! Merci de réessayer")
        def_time()
        return None
    if minutes > 60 or minutes < 1:
        print("Les minutes ne sont pas comprises entre 1 et 60 ! Merci de réessayer")
        def_time()
        return None
    if seconds > 60 or seconds < 1:
        print("Les secondes ne sont pas comprises entre 1 et 60 ! Merci de réessayer")
        def_time()
        return None
    print("Nous allons maintenant entrer les données du capteur")
    def_sensorData()

def def_sensorData ():
    sensorID = input("Donne identifiant sensor")
    sensor_value = input("donne valeur du capteur")
    datatype = input("Donne type de donnée, executez help_datatypes pour avoir une liste des types de données.")




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