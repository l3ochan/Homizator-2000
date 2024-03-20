# Léonard fait toujours des usines à gaz.
import random
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
sensorData=(sensorID,sensor_value)

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

datatypeDictionnary = {
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

datatypeMapping = {
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
columnIndex = {
    'date': 0,
    'time': 1,
    'sensorID': 2,
    'sensor_value': 3,
    'datatype': 4
}

filtered = 0
datatype = null

#Machine état annulation commande
cancel = False

#Format stockage des données (pour le moment)
mainData = []
mainDataInstant = ()
sorted_mainData = []


#=====commandes d'aides=====
def help(type):
    if type == "datatype":
        print("Here are all the supported data types, the data type field is required to insert new data.")
        print(" ")
        print(" ")
        print("+----------------+-------------------------+-------+-----------------------------------------+")
        print("| Data type field | Data type              | Unit  | Description                             |")
        print("+----------------+-------------------------+-------+-----------------------------------------+")
        print("| null           | None                    | N/A   | Not a datatype                          |")
        print("| temp           | Temperature             | °C    | Measurement of ambient temperature      |")
        print("| lum            | Luminosity              | Lux   | Measured level of lighting              |")
        print("| hum            | Humidity rate           | %     | Percentage of humidity in the air       |")
        print("| co2            | CO2 level               | ppm   | CO2 concentration in the air            |")
        print("| air            | Air quality             | AQI   | Air quality index                       |")
        print("| son            | Sound level             | dB    | Ambient noise level                     |")
        print("| atm            | Atmospheric pressure    | hPa   | Measured air pressure                   |")
        print("| conso          | Energy consumption      | kWh   | Amount of energy consumed               |")
        print("+----------------+-------------------------+-------+-----------------------------------------+")

    elif type == "general":
        print("A rédiger")
    else:
        print("Unknown parameter")
        print(" ")
        print("Supported parameters: ")
        print(" ")
        print("help general: Returns the general help section")
        print(" ")
        print ("help datatypes : Returns type of data supported")
        print(" ")
    return None

        



#Ajotuer manuellement une donnée au tableau
def addData():  
    date = def_date()
    time = def_time()
    sensorData = def_sensorData()
    datatype = def_datatype()
#    print(date)
    if cancel:
        print("canceled !")
        return (cancel)
    sensorID,sensor_value = sensorData
    mainDataInstant = (date, time, sensorID, sensor_value, datatypeDictionnary[datatype])
    mainData.append(mainDataInstant)
    print("New data has been stored in database.")
    print(f"Entry #{len(mainData)}:")
    print(f"  Date: {date[0]}/{date[1]}/{date[2]}")
    print(f"  Time: {time[0]}:{time[1]}:{time[2]}")
    print(f"  Sensor ID: {sensorID}")
    print(f"  Value: {sensor_value}")
    print(f"  Data Type: {datatypeDictionnary[datatype]}")
    print("-----")
    print("Execute 'show data' to see all entries")

def add_data_debug(debug_revolutions): #Petit script pour générer X entrées aléatoires au hazard pour remplir le tableau
    print("Debug mode") #car c'est relou de faire des entrées à la main 
    if debug_revolutions.isdigit()==True:
        debug_revolutions=int(debug_revolutions)
    else:
        debug_revolutions=int(debug_revolutions)
        print("Revolutions number is not an integer")
        return
    debug_repetitions = 0
    while debug_repetitions != debug_revolutions: #valeurs aléatoires pour l'heure, le jour et les données capteur
        date = random.randint(0,30),random.randint(1,12),random.randint(1970,2077)
        time = random.randint(0,24),random.randint(0,60),random.randint(0,60)
        sensorID = random.choice(['Office','Living_room','Entry','Toilet','Garage','Bathroom','Kitchen'])
        sensor_value = random.randint(0,150)
        datatype=random.choice(list(datatypeMapping.values()))
        mainDataInstant = (date, time, sensorID, sensor_value, datatypeDictionnary[datatype])
        mainData.append(mainDataInstant)
        print("New data has been stored in database.")
        print(f"Entry #{len(mainData)}:")
        print(f"  Date: {date[0]}/{date[1]}/{date[2]}")
        print(f"  Time: {time[0]}:{time[1]}:{time[2]}")
        print(f"  Sensor ID: {sensorID}")
        print(f"  Value: {sensor_value}")
        print(f"  Data Type: {datatypeDictionnary[datatype]}")
        print("-----")
        print("Execute 'show data' to see all entries")
        debug_repetitions+=1
    print(f"Debug loop successfully executed {debug_repetitions} times.")
    return

def def_date(): #On donne la date
    global cancel
    date_box = input("Input time with format jj/mm/aaaa, type cancel to cancel")
    if date_box == "cancel":
        cancel = True
        return 
    day,month,year = date_box.split('/') #Séparation des données entrées par l'utilisateur
    day = int(day)
    month = int(month)
    year = int(year)
    if not (1 <= day <= 31):
        print("Date is not between 1 and 31 ! Please verify your input.")
        def_date()
        return 
    if not (1 <= month <= 12):
        print("Month is not between 1 and 12 ! Please verify your input.")
        def_date()
        return 
    date = (day,month,year)
    return date
    
def def_time():  #On donne l'heure
    global cancel
    if cancel:
        return
    time_box = input("Input time with format hh:mm:ss")
    if time_box == "cancel":
        cancel = True
        return 
    hours,minutes,seconds = time_box.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if not (1 <= hours <= 24):
        print("There's only 24hrs in one day. Please verify your input.")
        def_time()
        return 
    if not (0 <= minutes < 60):
        print("Minutes are note between 1 and 60 ! Please verify your input.")
        def_time()
        return 
    if not (0 <= seconds < 60):
        print("Seconds are note between 1 and 60 ! Please verify your input.")
        def_time()
        return 
    time = (hours,minutes,seconds)
    return time

def def_sensorData():#On donne les infos du capteur
    global cancel
    if cancel:
        return
    sensorID = input("Input sensorID")
    if sensorID == "cancel":
        cancel = True
        return 
    sensor_value = input("Input sensor value")
    if sensor_value == "cancel":
        cancel = True
        return 
    sensorData = (sensor_value,sensorID)
    return sensorData

def def_datatype():# on définit le type de donnée
    global cancel
    if cancel:
        return
    datatype_input = input("Enter data type, type 'help datatypes' for more info")
    if datatype_input == "cancel":
        cancel = True
        return
    # Utilise le dico datatypeMapping pour obtenir la valeur entière numérique correspondante (multilanguage)
    if datatype_input in datatypeMapping:
        datatype = datatypeMapping[datatype_input]
    else:
        print("Unknown data type. Please try again")
        help(datatype)
        def_datatype()
    return datatype

#=====Controleurs=====
def sortSystem(filtertype,value):
    sorted_mainData = sortEntries(filtertype,value)
    showData(sorted_mainData)
    return


#Filtrer les colonnes du tableau
def sortEntries(filtertype,value): #Entrée de la colonne (filtertype) et de la valeur souhaitée (ex bureau)
    if filtertype not in columnIndex:
        print("Unknown Filter")
        return
    else:
        filtertype=columnIndex[filtertype]
        print(filtertype)
        #On retourne le tableau trié pour l'assigner à une variable dans sortSytem()
    return [line for line in mainData if line[filtertype].lower() == value.lower()] 
        
def showData(data=None):
    dataSource = data if data is not None else mainData
    #Si aucunes données à montrer, afficher un message d'erreur
    if not dataSource:
        print("No data to show.")
        return
    for entry_no, data in enumerate(dataSource, start=1):
        #Affichage 'sexy'
        date, time, sensorID, sensor_value, datatype = data #déballage de tuple
        print(f"Entry #{entry_no}:")
        print(f"  Date: {date[0]}/{date[1]}/{date[2]}")
        print(f"  Time: {time[0]}:{time[1]}:{time[2]}")
        print(f"  Sensor ID: {sensorID}")
        print(f"  Value: {sensor_value}")
        print(f"  Data Type: {datatype}")
        print("-----")
    return 

# =====friendly commands===== 
# Définir les commandes et indiquer si elles acceptent des paramètres (True) ou non (False)
commands = {
    "add data": (addData, False),
    "show data": (showData, False),
    "debug add": (add_data_debug, True),
    "show data filter": (sortSystem, True),  # Cette fonction accepte des paramètres
    "help" : (help, True),
}

def process_command(input_command):
    parts = input_command.split(' ')
    found_command = None
    params = []

    # Identifier la commande la plus longue qui correspond
    for cmd in sorted(commands.keys(), key=len, reverse=True):
        if input_command.startswith(cmd):
            found_command = cmd
            break

    if found_command:
        func, accepts_params = commands[found_command]
        # Extraire les paramètres si présents
        if len(input_command) > len(found_command):
            # Assurez-vous qu'il y a un espace après la commande avant de prendre des paramètres
            if input_command[len(found_command)] == ' ':
                params = input_command[len(found_command)+1:].split(' ')
        
        # Exécuter la commande avec ou sans paramètres selon le cas
        if accepts_params:
            if len(params) == 0:
                print(f"Error: Missing required parameter for command '{found_command}'.")
            else:
                func(*params)
        else:
            if len(params) > 0:
                print(f"Error: Command '{found_command}' does not accept parameters.")
            else:
                func()
    else:
        print("Unknown command, for a list of commands, type 'help'.")


# Boucle principale pour lire les commandes de l'utilisateur
while True:
    user_input = input("Enter command, 'help general' to display help, 'help imnew' to display beginners's guide : ")
    if user_input == "exit":
        break
    process_command(user_input)


print("Goodbye !")
print("Thanks for trying Homizator 2000 !")