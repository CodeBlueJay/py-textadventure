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

    # Convert the map to a list of lists
    game_map = [list(line) for line in game_map]

    # Update the player's location
    game_map[player_location[0]][player_location[1]] = '\033[31mP\033[0m'

    # Convert the map back to a list of strings
    game_map = [''.join(line) for line in game_map]

    # Print the map
    for line in game_map:
        print(line)

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
