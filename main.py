import time

commands = ["north", "east", "south", "west", "map", "use", "grab", "inventory", "stats"]

def show_map():
    print("____________________________________________________________________________")
    print("|                |   |               | |                       |           |")
    print("|                |   |     Theater   | |        Office         |           |")
    print("|                |   |_______________| |_______________________|           |")
    print("|                |                                                         |")
    print("|     300's      |                                                         |")
    print("|   Building     |                                                         |")
    print("|                |                                                         |")
    print("|                |              ______________________                     |")
    print("|                |   _______   |                      |                    |")
    print("|________________|  |       |  |                      |                    |")
    print("|___________________|       |  |       500's          |                    |")
    print("|                           |  |      Building        |                    |")
    print("|      400's Building       |  |                      |                    |")
    print("|___________________________|  |                      |                    |")
    print("|______________________________|______________________|____________________|")

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