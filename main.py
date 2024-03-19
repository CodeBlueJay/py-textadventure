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
WHITE = "\033[37m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"
GREENB = GREEN + BOLD

# Variables
grade = "F"
percent = 0
inventory = ["Progress Report"] # Progress Report is default.
player_location = [2, 79]
auto_map = False
basketball_taken = 0

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
    {"name": "North Gym", "items": "Basketball", "coordinates": [4, 66], "use": False, "grab": True, "variable": basketball_taken},
    {"name": "Office", "items": "Progress Report", "coordinates": [2, 41], "use": True, "grab": False, "variable": None}
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
                print(f"{RED}{BOLD}{char}{RESET}", end="") # Player Icon Color
                player_printed = True
            elif re.match(r'[a-zA-Z0-9 ]', char):
                print(f"{CYAN}{BOLD}{char}{RESET}", end="") # Map Locations Color
            elif re.match(r'[_|]', char):
                print(f"{YELLOW}{BOLD}{char}{RESET}", end="") # Map Borders Color
            else:
                print(char, end="")
        print()

def welcome_message():
    print(f"{CYAN}{BOLD} _    _      _                            _          _____         _      ___      _                 _                  _ ")
    print(f"| |  | |    | |                          | |        |_   _|       | |    / _ \    | |               | |                | |")
    print(f"| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | | _____  _| |_  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |")
    print(f"| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ \/ / __| |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |")
    print(f"\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | |  __/>  <| |_  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/_|")
    print(f" \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/\___/_/\_\\__| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_){RESET}\n")

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
            print(f"Words in {GREEN}green{RESET} are commands you can type.")
            print(f"The commands that you can use anywhere are: {GREEN}map{RESET}, {GREEN}inventory{RESET}, {GREEN}stats{RESET}, {GREEN}help{RESET}, and {GREEN}settings{RESET}.")
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
                    print("You used " + use_item + ".")
                    if player_location == [2, 41]:
                        break
                else:
                    print("You've used that already.")
            else:
                print("You can't use anything here.")
        elif command == "grab":
            for room in rooms:
                if player_location == room["coordinates"]:
                    grab_item = room["items"]
                    grab_checker = room["variable"]
            if grab:
                if grab_item not in inventory:
                    inventory.append(grab_item)
                    print("You grabbed the " + grab_item + ".")
                    grab_checker = 1
                    for room in rooms:
                        if player_location == room["coordinates"]:
                            room["variable"] = grab_checker
                else:
                    print("You already have that item.")
            else:
                print("There is nothing to grab.")
        else:
            print("Invalid command!")


def show_inventory():
    total_width = 20
    print(" ____________________ ")
    print(f"|     {MAGENTA}{BOLD}Inventory{RESET}      |")
    print("|--------------------|")
    for item in inventory:
        word_width = total_width - len(item)
        left_spaces = word_width // 2
        right_spaces = word_width - left_spaces
        print(f"|" + ' ' * left_spaces + item + ' ' * right_spaces + "|")
    print("|____________________|")

def show_stats():
    global grade
    global percent
    calculate_grade()
    print(" ________________ ")
    print(f"|     {MAGENTA}{BOLD}Grades{RESET}     |")
    print("|----------------|")
    print(f"|  {YELLOW}{BOLD}Grade:{RESET} " + grade + "      |")
    if percent < 10:
        print(f"|  {YELLOW}{BOLD}Percent:{RESET} " + str(percent) + "%   |")
    else:
        print(f"|  {YELLOW}{BOLD}Percent:{RESET} " + str(percent) + "%  |")
    print("|________________|")

def calculate_grade():
    global percent
    global grade
    if percent == 100:
        grade = "S"
    elif percent >= 90:
        grade = "A"
    elif percent >= 80:
        grade = "B"
    elif percent >= 70:
        grade = "C"
    elif percent >= 60:
        grade = "D"
    else:
        grade = "F"

def change_settings():
    global auto_map
    while True:
        print(" _________________________________ ")
        print(f"|            {MAGENTA}{BOLD}Settings{RESET}             |")
        print(f"| {GREENB}1.{RESET} Toggle auto-map              |")
        print("|    (Automatically shows the map |")
        print("|     after every move)           |")
        print(f"| {GREENB}2.{RESET} Back to game                 |")
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
    print(f"Go {GREENB}west{RESET} to get in the school and start the game. Type {GREENB}settings{RESET} to change settings.")
    check_command(False, [0, 0], False, False, [0, 0], False, False, [0, 0], False, True, [2, 65], north_gate, False, False)

def north_gate():
    print("You are in the school, just inside the North Gate.")
    print(f"You turn and see the North Gym to the {GREENB}south{RESET}. You can also continue {GREENB}west{RESET} to the quad.")
    check_command(False, [0, 0], None, False, [0, 0], None, True, [4, 66], inside_north_gym, True, [6, 50], east_quad, False, False)

def inside_north_gym():
    global basketball_taken
    print("You are inside the North Gym.")
    for room in rooms:
        if player_location == room["coordinates"]:
            basketball_taken = room["variable"]
    if basketball_taken == 0:
        print("There is a basketball lying there.")
        print(f"You can {GREENB}grab{RESET} it or go back outside {GREENB}north{RESET}.")
        check_command(True, [2, 79], north_gate, False, [0, 0], None, False, [0, 0], None, False, [0, 0], None, False, True)
    else:
        print(f"You can go back outside {GREENB}north{RESET}.")
        check_command(True, [2, 79], north_gate, False, [0, 0], None, False, [0, 0], None, False, [0, 0], None, False, True)

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
    end_game()

def end_game():
    global grade
    global percent
    print("You show the principal your grades.")
    calculate_grade()
    if grade == "S":
        s_ending()
    elif grade == "A":
        a_ending()
    elif grade == "B":
        b_ending()
    elif grade == "C":
        c_ending()
    elif grade == "D":
        d_ending()
    elif grade == "F":
        f_ending()

def s_ending():
    print("The principal is amazed at your grades.")
    print("He gives you a scholarship to any college you want.")
    print("Rank: Child Prodigy")

def west_quad():
    print("You are in the West Quad.")

def quad_south():
    print("You decide to go south.")
    print("1. You can go to the 500s Building.")
    print("2. You can go to the PE Intersection.")

start_game()
