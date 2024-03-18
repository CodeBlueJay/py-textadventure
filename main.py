import time, re

commands = ["north", "east", "south", "west", "map", "use", "grab", "inventory", "stats", "help", "settings"]

# ANSI escape codes
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
ORANGE = "\033[91m"
MAGENTA = "\033[35m"
BLACK = "\033[30m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Variables
grade = "F"
percent = 0
inventory = ["Progress Report"] # Progress Report is default.
player_location = [2, 79]
auto_map = False

game_map = [
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

rooms = [
    {"name": "North Gym", "items": "basketball", "coordinates": [4, 66], "use": False, "grab": True},
    {"name": "Office", "items": "report card", "coordinates": [2, 41], "use": True, "grab": False}
]

def show_map():
    global player_location
    global game_map

    game_map = [list(line) for line in game_map]

    game_map[player_location[0]][player_location[1]] = 'P'

    player_printed = False

    for i, line in enumerate(game_map):
        for j, char in enumerate(line):
            if char == 'P' and not player_printed and [i, j] == player_location:
                print(f"{RED}{char}{RESET}", end="") # Player Icon Color
                player_printed = True
            elif re.match(r'[a-zA-Z0-9 ]', char):
                print(f"{MAGENTA}{char}{RESET}", end="") # Map Locations Color
            elif re.match(r'[_|]', char):
                print(f"{CYAN}{char}{RESET}", end="") # Map Borders Color
            else:
                print(char, end="")
        print()

def welcome_message():
    print(" _    _      _                            _          _____         _      ___      _                 _                  _ ")
    print("| |  | |    | |                          | |        |_   _|       | |    / _ \    | |               | |                | |")
    print("| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | | _____  _| |_  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |")
    print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ \/ / __| |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |")
    print("\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | |  __/>  <| |_  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/_|")
    print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/\___/_/\_\\__| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_)\n")

def check_command(north, north_location, north_function, east, east_location, east_function, south, south_location, south_function, west, west_location, west_function, use, grab):
    global player_location
    global game_map
    global rooms
    global room_location
    global auto_map
    while True:
        command = input("> ")
        if command == "map":
            show_map()
        elif command == "inventory":
            show_inventory()
        elif command == "stats":
            show_stats()
        elif command == "help":
            print("Commands: " + str(commands))
        elif command == "settings":
            change_settings()
        elif command == "north":
            if north:
                player_location = north_location
                if auto_map == True:
                    show_map()
                north_function()
                break
            else:
                print("You can't go that way.")
        elif command == "east":
            if east:
                player_location = east_location
                if auto_map == True:
                    show_map()
                east_function()
                break
            else:
                print("You can't go that way.")
        elif command == "south":
            if south:
                player_location = south_location
                if auto_map == True:
                    show_map()
                south_function()
                break
            else:
                print("You can't go that way.")
        elif command == "west":
            if west:
                player_location = west_location
                if auto_map == True:
                    show_map()
                west_function()
                break
            else:
                print("You can't go that way.")
        elif command == "use":
            for room in rooms:
                if player_location == room["coordinates"]:
                    use_item = room["items"]
            if use:
                if use_item in inventory:
                    inventory.remove(use_item)
                    print("You used" + use_item + ".")
                else:
                    print("You've used that already.")
            else:
                print("You can't use anything here.")
        elif command == "grab":
            for room in rooms:
                if player_location == room["coordinates"]:
                    grab_item = room["items"]
            if grab:
                if grab_item not in inventory:
                    inventory.append(grab_item)
                    print("You grabbed the " + grab_item + ".")
                else:
                    print("You already have that item.")
            else:
                print("There is nothing to grab.")
        else:
            print("Invalid command!")


def show_inventory():
    total_width = 20
    print(" ____________________ ")
    print("|     Inventory      |")
    print("|--------------------|")
    for item in inventory:
        word_width = total_width - len(item)
        left_spaces = word_width // 2
        right_spaces = word_width - left_spaces
        print("|" + ' ' * left_spaces + item + ' ' * right_spaces + "|")
    print("|____________________|")

def show_stats():
    print(" ________________ ")
    print("|     Grades     |")
    print("|----------------|")
    print("|  Grade: " + grade + "      |")
    if percent < 10:
        print("|  Percent: " + str(percent) + "%   |")
    else:
        print("|  Percent: " + str(percent) + "%  |")
    print("|________________|")

def change_settings():
    global auto_map
    while True:
        print(" _________________________________ ")
        print("|            Settings             |")
        print("| 1. Toggle auto-map              |")
        print("|    (Automatically shows the map |")
        print("|     after every move)           |")
        print("| 2. Back to game                 |")
        print("|_________________________________|")
        setting = input("Choose a setting to change: ")
        if setting == "1":
            auto_map = not auto_map
            if auto_map:
                print("Auto-map turned on.")
                break
            else:
                print("Auto-map turned off.")
                break
        elif setting == "2":
            break
        else:
            print("Invalid option.")

def start_game():
    welcome_message()
    print("You are a lone Troy Student, fighting to secure good grades and making your Asian parents proud.")
    print("Your objective it to make it across the school, visitng as many classes as possible to get the best grades.")
    print("When you are done, go to the office and show the principal your grades.")
    print("Commands: " + str(commands) + '\n')
    time.sleep(1)
    print("You stand in front of the North Gym gate.")
    print("You have a map of the school")
    show_map()
    print("Go 'west' to get in the school and start the game. Type 'settings' to change settings.")
    check_command(False, [0, 0], False, False, [0, 0], False, False, [0, 0], False, True, [2, 65], north_gate, False, False)

def north_gate():
    print("You are in the school, just inside the North Gate.")
    print("You turn and see the North Gym to the south. You can also continue west to the quad.")
    check_command(False, [0, 0], None, False, [0, 0], None, True, [4, 66], inside_north_gym, True, [6, 50], east_quad, False, False)

def inside_north_gym():
    print("You are inside the North Gym.")
    print("There is a basketball lying there.")
    print("You can grab it or go back outside north.")
    check_command(True, [2, 79], north_gate, False, [0, 0], None, False, [0, 0], None, False, [0, 0], None, 0, False, True)

def east_quad():
    print("You are in the East Quad.")
    print("You can go north to the Office, west to the West Quad, south into the 500s Building and the PE Intersection, or back east to the North Gate.")
    check_command(True, [2, 41], office, True, [2, 65], north_gate, True, [0, 0], quad_south, True, [6, 27], west_quad, False, False)

def office():
    print("You are in the Office, ready to leave.")
    print("The principal is there.")
    print("He wants to see your grades.")
    print("You can use your progress report or go south to the East Quad.")
    check_command(False, [0, 0], None, False, [0, 0], None, True, [6, 50], east_quad, False, [0, 0], None, True, False)

def west_quad():
    print("You are in the West Quad.")

def quad_south():
    print("You decide to go south.")
    print("1. You can go to the 500s Building.")
    print("2. You can go to the PE Intersection.")

start_game()