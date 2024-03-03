import time

commands = ["north", "east", "south", "west", "map", "use", "grab", "inventory", "stats", "help"]

# Variables
grade = "F"
percent = 0
inventory = []
player_location = [2, 79]

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

def show_map():
    global player_location
    global game_map

    new_game_map = [list(line) for line in game_map]

    for i in range(len(new_game_map)):
        for j in range(len(new_game_map[i])):
            if new_game_map[i][j] == '\033[31mP\033[0m':
                new_game_map[i][j] = ' '

    new_game_map[player_location[0]][player_location[1]] = '\033[31mP\033[0m'

    for line in new_game_map:
        print(''.join(line))

def welcome_message():
    print(" _    _      _                            _          _____         _      ___      _                 _                  _ ")
    print("| |  | |    | |                          | |        |_   _|       | |    / _ \    | |               | |                | |")
    print("| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | | _____  _| |_  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |")
    print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ \/ / __| |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |")
    print("\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | |  __/>  <| |_  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/_|")
    print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/\___/_/\_\\__| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_)\n")

def check_command(north, north_location, north_function, east, east_location, east_function, south, south_location, south_function, west, west_location, west_function, use, grab, use_amount, grab_item):
    global player_location
    global game_map
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
                north_function()
                break
            else:
                print("You can't go that way.")
        elif command == "east":
            if east:
                player_location = east_location
                east_function()
                break
            else:
                print("You can't go that way.")
        elif command == "south":
            if south:
                player_location = south_location
                south_function()
                break
            else:
                print("You can't go that way.")
        elif command == "west":
            if west:
                player_location = west_location
                west_function()
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
    check_command(False, [0, 0], False, False, [0, 0], False, False, [0, 0], False, True, [2, 65], north_gate, False, False, 0, 0)

def north_gate():
    print("You are in the school, just inside the North Gate.")
    print("You turn and see the North Gym to the south. You can also continue west to the quad.")
    check_command(False, [0, 0], None, False, [0, 0], None, True, [4, 66], inside_north_gym, True, [6, 27], west_quad, False, False, 0, 0)

def inside_north_gym():
    print("You are inside the North Gym.")

def west_quad():
    print("You are in the West Quad.")

start_game()