import time

commands = ["north", "east", "south", "west", "map", "use", "grab", "inventory", "stats", "help"]

# Variables
grade = "F"
percent = 0
inventory = []
player_location = [2, 79]

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

def welcome_message():
    print(" _    _      _                            _          _____         _      ___      _                 _                  _ ")
    print("| |  | |    | |                          | |        |_   _|       | |    / _ \    | |               | |                | |")
    print("| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | | _____  _| |_  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |")
    print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ \/ / __| |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |")
    print("\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | |  __/>  <| |_  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/_|")
    print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/\___/_/\_\\__| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_)\n")

def check_command(north, north_location, east, east_location, south, south_location, west, west_location, use, grab, use_amount, grab_item):
    global player_location
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
        elif command == "north":
            if north:
                player_location = north_location
                break
            else:
                print("You can't go that way.")
        elif command == "east":
            if east:
                player_location = east_location
                break
            else:
                print("You can't go that way.")
        elif command == "south":
            if south:
                player_location = south_location
                break
            else:
                print("You can't go that way.")
        elif command == "west":
            if west:
                player_location = west_location
                break
            else:
                print("You can't go that way.")
        elif command == "use":
            if use:
                if use_amount > 0:
                    use_amount -= 1
                    print("You used an item. Remaining items: " + str(use_amount))
                else:
                    print("There's nothing to use.")
            else:
                print("You can't use that here.")
        elif command == "grab":
            if grab:
                if grab_item in current_room_items:
                    inventory.append(grab_item)
                    current_room_items.remove(grab_item)
                    print(f"You have grabbed {grab_item}.")
                else:
                    print("There's nothing to grab.")
            else:
                print("You can't grab that here.")
        else:
            print("Invalid command!")


def show_inventory():
    print(" ____________________ ")
    print("|     Inventory      |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|____________________|")

def show_stats():
    print(" ______________ ")
    print("|  Grade: " + grade + "    |")
    print("|  Percent: " + str(percent) + "% |")
    print("|______________|")

def start_game():
    welcome_message()
    print("You are a lone Troy Student, fighting to secure good grades and making your Asian parents proud.")
    print("Your objective it to make it across the school, visitng as many classes as possible to get the best grades.")
    print("Commands: " + str(commands) + '\n')
    time.sleep(1)
    print("You stand in front of the North Gym gate.")
    print("You have a map of the school")
    show_map()
    print("Go 'west' to get in the school and start the game.")
    check_command(False, [0, 0], False, [0, 0], False, [0, 0], True, [0, 0], False, False, 0, 0)
    north_gate()

def north_gate():
    print("You are in the school, just inside the North Gate.")
    print("You turn and see the North Gym to the south. You can also continue west to the quad.")
    # check_command(False, [0, 0], False, [0, 0], True, [0, 0], True, [2, 78], False, False, 0, 0)

start_game()