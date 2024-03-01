import time

commands = ["north", "east", "south", "west", "map", "use", "grab", "inventory", "stats"]

def show_map(player_location):
    map = [
        "___________________________________________________________________________________",
        "|                |   |               | |                       |                  |",
        "|                |   |     Theater   | |   Office   ___________|    North Gate    |",
        "|                |   |_______________| |___________|         ____________         |",
        "|                |                                          |            |        |",
        "|     300s       |                                          |   North    |        |",
        "|   Building     |                   Quad                   |    Gym     |        |",
        "|                |                                          |____________|        |",
        "|                |              ______________________   ______         ______    |",
        "|                |   _______   |                      | |      | ____  |      |   |",
        "|________________|  |       |  |                      | | Girl ||    | | Boys |   |",
        "|___________________|       |  |       500s           | |Locker||Pool| |Locker|   |",
        "|                           |  |      Building        | | Room ||____| | Room |   |",
        "|       400s Building       |  |                      | |______|       |______|   |",
        "|___________________________|  |                      |      ________             |",
        "|                              |______________________|     | South  |            |",
        "|                                    ______________         |  Gym   |            |",
        "|                                   |              |        |________|            |",
        "|                                   |     900s     |                              |",
        "|                                   |   Building   |                              |",
        "|                                   |______________|                              |",
        "|_________________________________________________________________________________|"
    ]

    # Convert the map to a list of lists
    map = [list(line) for line in map]

    # Update the player's location
    map[player_location[0]][player_location[1]] = '\033[31mP\033[0m'

    # Convert the map back to a list of strings
    map = [''.join(line) for line in map]

    # Print the map
    for line in map:
        print(line)

def welcome_message():
    print(" _    _      _                            _          _____         _      ___      _                 _                  _ ")
    print("| |  | |    | |                          | |        |_   _|       | |    / _ \    | |               | |                | |")
    print("| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | | _____  _| |_  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |")
    print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ \/ / __| |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |")
    print("\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | |  __/>  <| |_  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/_|")
    print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/\___/_/\_\\__| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_)\n")

def start_game():
    player_location = [2, 79]
    welcome_message()
    print("You are a lone Troy Student, fighting to secure good grades and making your Asian parents proud.\n")
    print("Commands: " + str(commands) + '\n')
    time.sleep(1)
    print("You stand in front of the North Gym gate.")
    print("You have a map of the school")
    show_map(player_location)
    print("Go 'west' to get in the school and start the game.")
    command = input("> ")
    if command == "west":
        player_location = [2, 65]
        show_map(player_location)
    elif command == "map":
        show_map(player_location)
    elif command == "stats":
        print("Grade: 100")
        print("Attack: 10")
        print("Defense: 10")
        print("Speed: 10")

def north_gate():
    print("You are at the North Gate.")
    print("You see the North Gym to the south. You can also go west to the quad.")

start_game()