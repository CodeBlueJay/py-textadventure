import time

commands = ["north", "east", "south", "west", "map", "use", "grab", "inventory", "stats"]

def show_map():
    print("___________________________________________________________________________________")
    print("|                |   |               | |                       |                  |")
    print("|                |   |     Theater   | |   Office   ___________|                  |")
    print("|                |   |_______________| |___________|         ____________         |")
    print("|                |                                          |            |        |")
    print("|     300's      |                                          |   North    |        |")
    print("|   Building     |                   Quad                   |    Gym     |        |")
    print("|                |                                          |____________|        |")
    print("|                |              ______________________   ______         ______    |")
    print("|                |   _______   |                      | |      | ____  |      |   |")
    print("|________________|  |       |  |                      | | Girl ||    | | Boys |   |")
    print("|___________________|       |  |       500's          | |Locker||Pool| |Locker|   |")
    print("|                           |  |      Building        | | Room ||____| | Room |   |")
    print("|      400's Building       |  |                      | |______|       |______|   |")
    print("|___________________________|  |                      |                           |")
    print("|                              |______________________|                           |")
    print("|                                                                                 |")
    print("|_________________________________________________________________________________|")

def welcome_message():
    print(" _    _      _                            _          _____         _      ___      _                 _                  _ ")
    print("| |  | |    | |                          | |        |_   _|       | |    / _ \    | |               | |                | |")
    print("| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | | _____  _| |_  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |")
    print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ \/ / __| |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |")
    print("\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | |  __/>  <| |_  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/_|")
    print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/\___/_/\_\\__| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_)\n")

def start_game():
    welcome_message()
    print("You are a lone Troy Student, fighting to secure good grades and making your Asian parents proud.\n")
    print("Commands: " + str(commands) + '\n')
    time.sleep(1)
    print("You stand in front of the North Gym gate.")
    print("You have a map of the school")
    show_map()

start_game()