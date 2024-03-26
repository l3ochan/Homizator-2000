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
print("Welcome to the Personator 2000")
print("Enter command, 'help general' to display help, 'help imnew' to display beginners's guide : ")
# =====Initialisation=====
#Format date de naissance
day = 24
month = 12
year = 2004
birthdate = (day,month,year)

#Format name
name = "Michel"
surname = "Pasquier"
identity = (name,surname)

#Types de données, stockage sous forme de 
#dictionnaire pour identifier les données par un id
null = 0
dad = 1
mom = 2
child = 3
# Dictionnaire des types de données, pourrait permettre le multilingue
persontypeDictionnary = {
    0 : "null",
    1 : "dad",
    2 : "mom",
    3 : "child",
    4 : "CO2 Level",
    5 : "Air quality",
    6 : "Sound level", 
    7 : "Atmospheric pressure",
    8 : "Energy consumption" 
}


# Mappage du paramètre que l'utilisateur rentrera lors de l'entrée d'une ligne
persontypeeMapping = {
    "null": null,
    "dad": dad,
    "mom": mom,
    "child": child,
}
#Indexe des colonnes du tableau, aka ordre de stockage
columnIndex = {
    'name': 0,
    'surname': 1,
    'birthdate': 2,
    'persontype': 3
}


datatype = null

#Machine état annulation commande
cancel = False

#Format stockage des données (pour le moment)
mainData = []
mainDataInstant = ()
sorted_mainData = []
filtered = False 


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
        print("==============================================")
        print("         Welcome to the Help Section          ")
        print("==============================================")
        print("Here is a list of available commands and how to use them:")
        print(" ")
        print("GENERAL:")
        print("  exit - Closes the application.")
        print("  help general - Displays this help section.")
        print("  help datatypes - Displays the different types of data that you can record.")
        print(" ")
        print("ADDING DATA:")
        print("  add data - Allows you to manually add a data entry.")
        print("    When this command is called, you will be prompted to enter:")
        print("    - The date (format dd/mm/yyyy)")
        print("    - The time (format hh:mm:ss)")
        print("    - The sensor ID")
        print("    - The value captured by the sensor")
        print("    - The data type (temp, lum, etc.)")
        print(" ")
        print("DISPLAYING DATA:")
        print("  show data - Displays all recorded data.")
        print(" ")
        print("FILTERING AND SORTING DATA:")
        print("  show data filter [sensor type] [value] - Displays data filtered based on the sensor type and specified value.")
        print("    Example: 'show data filter sensorID Office' will display all data where the sensor ID is 'Office'.")
        print(" ")
        print("DEBUG MODE (Quick Data Addition):")
        print("  debug add [number] - Automatically generates and adds a specified number of random data entries.")
        print("    Example: 'debug add 10' will add 10 new random data entries.")
        print(" ")
        print("Note: Parameters in brackets '[]' should be replaced with your specific values when using the commands.")
    elif type == "imnew":
        print("========================================================")
        print("      Welcome to Homizator 2000 - Beginner's Guide      ")
        print("========================================================")
        print(" ")
        print("Homizator 2000 is your comprehensive solution for managing and analyzing sensor data. Whether you're tracking temperature, brightness, or air quality, Homizator 2000 makes data handling effortless. Here’s how to get started:")
        print(" ")
        print("1. ADDING DATA")
        print("To begin recording sensor data, use the 'add data' command. You'll be prompted to enter details step by step:")
        print("  - Date in dd/mm/yyyy format. For example, '24/12/2024'.")
        print("  - Time in hh:mm:ss format. Such as '12:57:56'.")
        print("  - Sensor ID, which could be a specific name or location like 'Office'.")
        print("  - The sensor's value, a numerical data point that the sensor records.")
        print("  - Data type, which describes the nature of the data (e.g., 'temp' for temperature).")
        print(" ")
        print("2. VIEWING DATA")
        print("After adding data, you can view all entries by using the 'show data' command. This will display all recorded entries in a structured format, showcasing the date, time, sensor ID, value, and data type.")
        print(" ")
        print("3. FILTERING DATA")
        print("If you're looking for specific information, 'show data filter' allows you to narrow down entries based on sensor type and value. For instance, to view all entries from the 'Office' sensor, you'd use:")
        print("  show data filter sensorID Office")
        print(" ")
        print("4. GETTING HELP")
        print("Need a refresher on commands or data types? 'help general' provides an overview of all commands, while 'help datatypes' lists all supported data types and their descriptions.")
        print(" ")
        print("5. EXITING THE PROGRAM")
        print("When you're done, simply type 'exit' to close Homizator 2000.")
        print(" ")
        print("We hope this guide helps you get started smoothly. Happy data tracking!")
    return None


#Ajotuer manuellement une donnée au tableau
def addData():  
    identity = def_identity()
    birthdate = def_birthdate()
    persontype = def_persontype()
#    print(date)
    if cancel:
        print("canceled !")
        return (cancel)
    name,surname = identity
    mainDataInstant = (name, surname, birthdate, persontypeDictionnary[persontype])
    mainData.append(mainDataInstant)
    print("New data has been stored in database.")
    print(f"Entry #{len(mainData)}:")
    print(f"  Name: {name}")
    print(f"  Surname: {surname}")
    print(f"  Bithdate: {birthdate[0]}/{birthdate[1]}/{birthdate[2]}")
    print(f"  Persontype: {persontypeDictionnary[persontype]}")
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

def def_birthdadate(): #On donne la date
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
    sorted_mainData = filterEntries(filtertype,value)
    showData(sorted_mainData)
    return

def showDataFiltered():
    global filtered
    if filtered:
        showData(sorted_mainData)
    else:
        print("No filters applied, run 'show data filtered <Column> <Value>' to set one up")
    
def clearFilters():
    global filtered
    if filtered:
        dialog = input("Are you sure you want to clear filters")
        if dialog == "cancel":
            return 
        elif dialog == "yes":
            sorted_mainData = []
            print("Successfully cleared filters")
            filtered = False
            return
        elif dialog == "no":
            print("Canceled !")
            return
        else:
            print("Invalid entry")
            clearFilters()
            return 
    else:
        print("No filters applied!")
        


#Filtrer les colonnes du tableau
def filterEntries(filtertype,value): #Entrée de la colonne (filtertype) et de la valeur souhaitée (ex bureau)
    global filtered
    if filtertype not in columnIndex:
        print("Unknown Filter")
        return
    elif filtertype == columnIndex["datatype"]:
        if value not in datatypeMapping:
            print("Unknown data type. Please try again")
            help(datatype)
        else:
            filtertype=columnIndex[filtertype]
            value = datatypeMapping[value]
            value = datatypeDictionnary[value]
    else:
        filtertype=columnIndex[filtertype]
        #print(filtertype)
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
        filtered = True
    return 

#Parce que vscode c'est de la merde
def update_screen():
    print("Updated !")
    return None

# =====friendly commands===== 
# Définir les commandes et indiquer si elles acceptent des paramètres (True) ou non (False)
commands = {
    "add data": (addData, False),
    "show data": (showData, False),
    "debug add": (add_data_debug, True),
    "show data filter": (sortSystem, True),  # Cette fonction accepte des paramètres
    "help" : (help, True),
    "update screen" : (update_screen, False),
    "show data filtered": (showDataFiltered, False),
    "clear filters": (clearFilters, False),
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
    user_input = input(">")
    if user_input == "exit":
        break
    process_command(user_input)


print("Goodbye !")
print("Thanks for trying Homizator 2000 !")