print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(" @,,,*,*(////////,*,/,,,*,,,,,,,,,,,,,,,,,,,/,,,,****,,,,,,,,,,.   @")
print(" @,,,*//////////((((((////////////*,,,,,,,,,/,,,,****,,,,,,,,,,.   @")
print(" @,/////////./(((((((///////////////,,,,,,,,/,,,,****,,,,,,,,,,.   @")
print(" @(///////     /((((/////     ///////,,,,,,,/,,,,****,,,,,,,,,,.   @")
print(" @(//////         (//////     *//////,,,,,,,/,,,,****,,,,,,,,,,.   @")
print(" @,////((((#        *////     *////((*******/,,,,****,,,,,,,,,,.   @")
print(" @**,(((((((((         /(     */(((#%////////,,,,****,,,,,,,,,,.   @")
print(" @**,***,*/((///////   . .       *(#%%&&////////,,,,****,,,,,,,,,,.@")
print(" @**,***,*,,*////(((((           (%&&&&&//,/////,,,,****,,,,,,,,,,.@")
print(" @**,***,*,*(######(((        /&&&@@@&##(////,,,,****,,,,,,,,,,.   @")
print(" @**,***,*,**//#((((//((         @&#(&@@@@///,,,,****,,,,,,,,,,.   @")
print(" @**,***,*,**///*//((((#%&@        #@@@@@@@@&,,,,****,,,,,,,,,,.   @")
print(" @**,***,*,*******((#%&&@ @@@         @@@&#(///,,****,,,,,,,,,,.   @")
print(" @**,***,*,*******#%&&@@@   (#@@        ///(((##%%***,,,,,,,,,,.   @")
print(" @**,***,*,///////&@@@@@@     %@@@         ##%%%%%%%*,,,,,,,,,,.   @")
print(" @**,***,*,(((((((@@@@&#(     #@@@%#(        (%%####((#,,,,,,,,.   @")
print(" @**,***,*,(((((((@@%#(#&     #@%#(((((         (((((((((,,,,,,.   @")
print(" @**,***,*,///////%#(#%&@     #%(((((####%        *(((((((((,,,.   @")
print(" @**,***,*,*******(##%&@@     /(((((#####(((         (((((((((,.   @")
print(" @**,***,*,*******#%&&@@@     /((((#####(((((((        /(((((((((,,@")
print(" @**,***,*,*******%&@@@@@     *(((####(((((((((((         ((((((((,@")
print(" @**,***,*,///////&@@@@@@                                   ((((((/@")
print(" @**,***,*,(((((((@@@@@@&                                 .(((((((,@")
print(" @**,***,*,///////@@@@&%#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(((((((((,,@")
print(" @**,***,*,////////@&%#(((((((((#((((((((((((((((((((((((((((((*.,,@")
print(" @**,***,*,//********#((((((((((((((((((((((((((((((((((((((,***.,,@")
print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
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
    2 : "Brightness",
    3 : "Humidity",
    4 : "CO2 Level",
    5 : "Air quality",
    6 : "Sound level", 
    7 : "Atmospheric pressure",
    8 : "Energy consumption" 
}

datatype_mapping = {
    "null": null,
    "temp": temp,
    "lum": lum,
    "hum": hum,
    "co2": co2,
    "air": air,
    "son": son,
    "atm": atm,
    "conso": conso
}

datatype = null

#Machine état annulation commande
cancel = 0

#Format stockage des données (pour le moment)
main_data = []
main_dataInstant = (date, time, sensorID, sensor_value, datatype_dictionnary[datatype])
#

#=====commandes d'aides=====
def help_datatypes():
    print("Here are all the supported data types, the data type field is required to insert new data.")
    print(" ")
    print(" ")
    print("+----------------+-------------------------+-------+-----------------------------------------+")
    print("| Data type field | Data type              | Unit  | Description                             |")
    print("+----------------+-------------------------+-------+-----------------------------------------+")
    print("| null           | None                    | N/A   | No data available                       |")
    print("| temp           | Temperature             | °C    | Measurement of ambient temperature      |")
    print("| lum            | Luminosity              | Lux   | Measured level of lighting              |")
    print("| hum            | Humidity rate           | %     | Percentage of humidity in the air       |")
    print("| co2            | CO2 level               | ppm   | CO2 concentration in the air            |")
    print("| air            | Air quality             | AQI   | Air quality index                       |")
    print("| son            | Sound level             | dB    | Ambient noise level                     |")
    print("| atm            | Atmospheric pressure    | hPa   | Measured air pressure                   |")
    print("| conso          | Energy consumption      | kWh   | Amount of energy consumed               |")
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
    print("Execute show data to see all entries")


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
    return 

def def_datatype():
    global datatype, cancel
    if cancel == 1:
        return
    datatype_input = input("Enter data type, help datatypes for more info")
    if datatype == "quit":
        cancel = 1
        return
    # Utilise le dico datatype_mapping pour obtenir la valeur entière numérique correspondante (multilanguage)
    if datatype_input in datatype_mapping:
        datatype = datatype_mapping[datatype_input]
    else:
        print("Unknown data type. Please try again")
        help_datatypes
        def_datatype
        
def showData():
    if not main_data:
        print("No data to show.")
        return

    for entry_no, data in enumerate(main_data, start=1):
        date, time, sensorID, sensor_value, datatype = data
        print(f"Entry #{entry_no}:")
        print(f"  Date: {date[0]}/{date[1]}/{date[2]}")
        print(f"  Time: {time[0]}:{time[1]}:{time[2]}")
        print(f"  Sensor ID: {sensorID}")
        print(f"  Value: {sensor_value}")
        print(f"  Data Type: {datatype}")
        print("-----")



# =====friendly commands===== 
# Un dictionnaire associant les commandes de l'utilisateur aux fonctions correspondantes
commands = {
    "help datatypes": help_datatypes,
    "add data" : add_data,
    "show data" : showData,
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
    user_input = input("Enter command, help to display help : ")
    if user_input == "quit":
        break
    process_command(user_input)


print("Goodbye !")
print("Thanks for trying Homizator 2000 !")