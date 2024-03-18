import re

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

player_location = [8, 55]

def show_map():
    global player_location
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
                print(f"{RED}{char}{RESET}", end="") # Player Icon Color
                player_printed = True
            elif re.match(r'[a-zA-Z0-9 ]', char):
                print(f"{MAGENTA}{char}{RESET}", end="") # Map Locations Color
            elif re.match(r'[_|]', char):
                print(f"{CYAN}{char}{RESET}", end="") # Map Borders Color
            else:
                print(char, end="")
        print()

show_map()

''' LOCATIONS
Starting Pos (Outside North Gate) - [2, 79]
Inside North Gate - [2, 65]
Inside North Gym - [4, 66]
East Quad - [6, 50]
West Quad - [6, 27]
Inside 500s Building - [11, 49]
Inside Office - [2, 41]
PE Intersection - [8, 55]
'''
