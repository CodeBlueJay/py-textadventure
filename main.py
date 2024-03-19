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
YELLOWB = YELLOW + BOLD
WHITEB = WHITE + BOLD

# Variables
grade = "F"
percent = 0
inventory = ["Progress Report"] # Progress Report is default.
player_location = [2, 79]
auto_map = False
basketball_taken = 0

rooms = [
    {"name": "North Gym", "items": "Basketball", "coordinates": [4, 66], "use": False, "grab": True, "variable": basketball_taken},
    {"name": "Office", "items": "Progress Report", "coordinates": [2, 41], "use": True, "grab": False, "variable": None}
]

def show_map():
    global player_location
    global game_map

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
                print(f"{YELLOWB}{char}{RESET}", end="") # Map Borders Color
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
            print("Commands: " + GREENB + str(commands) + RESET)
            print(f"Words in {GREENB}green{RESET} are commands you can type.")
            print(f"The commands that you can use anywhere are: {GREENB}map{RESET}, {GREENB}inventory{RESET}, {GREENB}stats{RESET}, {GREENB}help{RESET}, and {GREENB}settings{RESET}.")
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
    print(f"|     {YELLOWB}Inventory{RESET}      |")
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
    print(f"|     {YELLOWB}Grades{RESET}     |")
    print("|----------------|")
    print(f"|  Grade: " + grade + "      |")
    if percent < 10:
        print(f"|  Percent: " + str(percent) + "%   |")
    else:
        print(f"|  Percent: " + str(percent) + "%  |")
    print("|________________|")

def calculate_grade():
    global percent
    global grade
    if percent == 100:
        grade = RED + BOLD + "S" + RESET
    elif percent >= 90:
        grade = ORANGE + BOLD + "A" + RESET
    elif percent >= 80:
        grade = YELLOW + BOLD + "B" + RESET
    elif percent >= 70:
        grade = GREEN + BOLD + "C" + RESET
    elif percent >= 60:
        grade = BLUE + BOLD + "D" + RESET
    else:
        grade = MAGENTA + BOLD + "F" + RESET

def change_settings():
    global auto_map
    while True:
        print(" _________________________________ ")
        print(f"|            {YELLOWB}Settings{RESET}             |")
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
    print(f"{WHITEB}You are a lone Troy Student, fighting to secure good grades and making your Asian parents proud.\n{RESET}")
    input(f"Press {GREENB}enter{RESET} to advance.\n")
    print(f"{WHITEB}Your objective it to make it across the school, visiting as many classes as possible to get the best grades.{RESET}")
    input()
    print(f"{WHITEB}When you are done, go to the office and show the principal your grades.{RESET}")
    input()
    print("Commands: " + GREENB +str(commands) + RESET + '\n')
    input()
    print(f"{BOLD}You stand in front of the North Gym gate.")
    print(f"You have a map of the school{RESET}")
    show_map()
    print(f"Go {GREENB}west{RESET} to get in the school and start the game. Type {GREENB}settings{RESET} to change settings.")
    check_command(False, [0, 0], False, False, [0, 0], False, False, [0, 0], False, True, [2, 65], north_gate, False, False)

def north_gate():
    print(f"{BOLD}You are in the school, just inside the North Gate.{RESET}")
    print(f"You turn and see the North Gym to the {GREENB}south{RESET}. You can also continue {GREENB}west{RESET} to the quad.")
    check_command(False, [0, 0], None, False, [0, 0], None, True, [4, 66], inside_north_gym, True, [6, 50], east_quad, False, False)

def inside_north_gym():
    global basketball_taken
    print(f"{BOLD}You are inside the North Gym.{RESET}")
    for room in rooms:
        if player_location == room["coordinates"]:
            basketball_taken = room["variable"]
    if basketball_taken == 0:
        print(f"{BOLD}There is a basketball lying there.{RESET}")
        print(f"You can {GREENB}grab{RESET} it or go back outside {GREENB}north{RESET}.")
        check_command(True, [2, 65], north_gate, False, [0, 0], None, False, [0, 0], None, False, [0, 0], None, False, True)
    else:
        print(f"You can go back outside {GREENB}north{RESET}.")
        check_command(True, [2, 79], north_gate, False, [0, 0], None, False, [0, 0], None, False, [0, 0], None, False, True)

def east_quad():
    print("You are in the East Quad.")
    print(f"You can go {GREENB}north{RESET} to the Office, {GREENB}west{RESET} to the West Quad, {GREENB}south{RESET} into the 500s Building and the PE Intersection, or back {GREENB}east{RESET} to the North Gate.")
    check_command(True, [2, 41], office, True, [2, 65], north_gate, True, [0, 0], quad_south, True, [6, 27], west_quad, False, False)

def office():
    print("You are in the Office, ready to leave.")
    print("The principal is there.")
    print("He wants to see your grades.")
    print(f"You can {GREENB}use{RESET} your progress report or go {GREENB}south{RESET} to the East Quad.")
    check_command(False, [0, 0], None, False, [0, 0], None, True, [6, 50], east_quad, False, [0, 0], None, True, False)
    end_game()

def end_game():
    global grade
    global percent
    print("You show the principal your grades.")
    calculate_grade()
    if "S" in grade:
        s_ending()
    elif "A" in grade:
        a_ending()
    elif "B" in grade:
        b_ending()
    elif "C" in grade:
        c_ending()
    elif "D" in grade:
        d_ending()
    elif "F" in grade:
        f_ending()

def s_ending():
    print("The principal is amazed at your grades.")
    print("He gives you a scholarship to any college you want.")
    print("Your Asian parents are proud of you.")
    print("They say you are just as good as your 5 year old cousin in China.")
    print(f"Rank: {YELLOWB}Child Prodigy{RESET}")

def a_ending():
    print("The principal is proud of your grades.")
    print("He sends you off with a farewell and lots of candy.")
    print("Your Asian parents accept your grades happily.")
    print("They will take all A's.")
    print(f"Rank: {YELLOWB}Smart Kid{RESET}")

def b_ending():
    print("The principal is happy that you managed acceptable grades.")
    print("He wishes you farewell and good luck at the gate.")
    print("Your Asian parents are slightly bothered that you almost had all A's.")
    print("They tell you that you did sufficient.")
    print(f"Rank: {YELLOWB}Average Student{RESET}")

def c_ending():
    print("The principal is relieved that you managed to pass and graduate.")
    print("He hopes you can study harder and go on to get into college.")
    print("Your Asian parent's silence says it all.")
    print("They say at least you passed.")
    print(f"Rank: {YELLOWB}Lucky Passer{RESET}")

def d_ending():
    print("The principal is sad that you failed but almost passed.")
    print("He says to take summer school with confidence that you will do better.")
    print("Your Asian parent's expressions say it all.")
    print("They are disappointed in you.")
    print(f"Rank: {YELLOWB}Close Misser{RESET}")

def f_ending():
    print("The principal is shocked that you somehow got that low of a grade.")
    print("He dejectedly hands you a summer school sentence and tells you to study harder.")
    print("Your Asian parent's silence and expressions fills you with shame.")
    print("They have no words to describe your failure.")
    print(f"Rank: {YELLOWB}Summer School Silence{RESET}")

def west_quad():
    print("You are in the West Quad.")

def quad_south():
    print("You decide to go south.")
    print(f"{GREENB}1.{RESET} You can go to the 500s Building.")
    print(f"{GREENB}2.{RESET} You can go to the PE Intersection.")

start_game()
