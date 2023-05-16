########################################################
# Title: CS 30 RPG Map
# Name: Calvin Hui
# Version: 002
########################################################
""" This is an RPG Map """

# map layout
Map = [
    ['shed', 'backyard', 'flowerbed'],
    ['kitchen', 'dining-room', 'living-room'],
    ['washroom', 'front-foyer', 'garage']
]

map_info = {
    'shed': {
        "location": "Your at the shed.",
        "description": {
            'locked': "There's a shed in the backyard, but seems like its locked.",
            'unlocked': "You open the shed door and you see a staircase that descends into darkness."
                        "\n"
                        "Suddenly you hear a eerie noice coming from the shadow, so you investigate"
                        "\n"
                        "End of Part One"
        }
    },
    'backyard': {
        "location": "The Backyard.",
        "description": "The grass looks like in hasn't been cut since."
    },
    'flowerbed': {
        "location": "The Flowerbed.",
        "description": "Beautiful flowers but there is something shiny in stuck in the flowerbed."
    },
    'kitchen': {
        "location": "The Kitchen.",
        "description": "Doesnt seem like anyone has been in here."
    },
    'dining-room': {
        "location": "The Dining Room",
        "description": "Something smells."
    },
    'living-room': {
        "location": "The Living Room.",
        "description": "Doesnt seem like anyone is living here."
    },
    'washroom': {
        "location": "The Washroom.",
        "description": "Just a washroom."
    },
    'front-foyer': {
        "location": "Welcome to the Abandoned House."
                    "\n"
                    "You are currently in the foyer.",
        "description": "If you would like to leave type: Quit."
    },
    'garage': {
        "location": "The Garage.",
        "description": "Just a garage, doesn't seem like there is anything interesting."
    },
}

# start location
row = 2
col = 1
MaxCol = 2
MaxRow = 2

Items = ['key']  # list of items

playing = True  # naming True as playing

Inventory = []  # placeholder for items to be added


def menu():
    """The main menu of the game"""
    global row, col, MaxRow, MaxCol, playing  # globe variables that the menu pulls from
    while playing:
        action_choice = input(f"Choice: ")  # player choices are inputted

        if (action_choice.lower() == 'walk') or (action_choice.lower() == 'w'):  # if the player types: walk or w
            print(f"Where would you like to go?")  # prints question
            if row != 0:
                print(f" * North")  # prints north as an option if the row does not equal to 0
            if row != MaxRow:
                print(f" * South")  # prints south as an option if the row does not exceed 2
            if col != MaxCol:
                print(f" * East")  # print east as an option if the column does not exceed 2
            if col != 0:
                print(f" * West")  # print west as an option if the column does not equal to 0
            print(f" * Back")

            # player can input their desired direction with in the list above
            movement_choice = input(f"Choice: ")  # player movement choices are inputted

            # if the movement choice was north or n the player will subtract 1 from the row in the array
            if (movement_choice.lower() == 'north') or (movement_choice.lower() == "n") and row > 0:
                row -= 1
                break
            # if the movement choice was south or s the player will add 1 unit to the row in the array
            elif (movement_choice.lower() == 'south') or (movement_choice.lower() == "s") and row < MaxRow:
                row += 1
                break
            # if the movement choice was east or e the player will add 1 unit to the column in the array
            elif (movement_choice.lower() == 'east') or (movement_choice.lower() == "e") and col < MaxCol:
                col += 1
                break
            # if the movement choice was north or n the player will subtract 1 from the column in the array
            elif (movement_choice.lower() == 'west') or (movement_choice.lower() == "w") and col > 0:
                col -= 1
                break
            elif movement_choice.lower() == 'back' or 'b':  # type back to back out and return to main menu
                return
            else:
                print(f"Sorry cant go that way!")  # any other movement input would print invalid option message

        elif (action_choice.lower() == 'inventory') or (action_choice.lower() == 'i'):  # if player types inventory or i
            inventory()  # run inventory function
            print('\n')
            messages()

        elif (action_choice.lower() == 'quit') or (action_choice.lower() == 'q'):  # if player types quit or q
            print("Are you sure you want to quit?")  # print confirmation message
            # print instructions to quit and input function
            confirmation = input(f"Type Quit or Q to quit the game: quit: ")
            if confirmation.lower() == 'quit' or 'q':  # if the player types quit or q
                playing = False  # playing switches to false
                break  # break to exit

        else:
            print("Invalid Option")  # if the player inputs an invalid option


def messages():
    """
    Messages that corresponds to the location the player is currently in and execute functions for player being there
    """
    global row, col, MaxRow, MaxCol, playing, Inventory  # global variables that the function pulls from the lists above
    while playing:
        location_description = Map[row][col]  # location description dictated by the location of the player on the map
        if location_description == 'front-foyer':  # if the location matches the name then print
            print(map_info['front-foyer']["location"])
            print(map_info['front-foyer']["description"])
            menu_options()  # prints menu options
            menu()  # goes back to the action menu
        if location_description == 'living-room':  # if the location matches the name then print
            print(map_info['living-room']["location"])
            print(map_info['living-room']["description"])
            menu_options()  # prints action menu options
            menu()  # goes back to the action menu
        if location_description == 'garage':  # if the location matches the name then print
            print(map_info['garage']["location"])
            print(map_info['garage']["description"])
            menu_options()  # prints action menu options
            menu()  # goes back to the action menu
        if location_description == 'flowerbed':  # if the location matches the name then print
            print(map_info['flowerbed']["location"])
            print(map_info['flowerbed']["description"])
            pickup()  # function that picks up the key the player said they saw
            menu_options()  # prints action menu options
            menu()  # goes back to the action menu
        if location_description == 'shed':  # if the location matches the name then print
            print(map_info['shed']["location"])
            print(map_info['shed']["description"]['locked'])
            if Inventory == 'key':
                print(map_info['shed']['description']['unlocked'])
            menu_options()  # prints action menu options
            menu()  # goes back to the action menu options
        if location_description == 'dining-room':  # if the location matches the name then print
            print(map_info['dining-room']["location"])
            print(map_info['dining-room']["description"])
            menu_options()  # prints action menu options
            menu()  # goes back to the action menu options
        if location_description == 'backyard':  # if the location matches the name then print
            print(map_info['backyard']["location"])
            print(map_info['backyard']["description"])
            menu_options()  # prints action menu options
            menu()  # goes back to the action menu options
        if location_description == 'kitchen':
            print(map_info['kitchen']["location"])
            print(map_info['kitchen']["description"])
            menu_options()
            menu()
        if location_description == 'washroom':
            print(map_info['washroom']["location"])
            print(map_info['washroom']["description"])
            menu_options()
            menu()
    print(f"Goodbye :( .")  # when the loop ends it prints the farewell message


def inventory():
    """Prints the inventory"""
    print(f"Current Inventory: ")  # Current Inventory message
    for item in Inventory:  # list items in the inventory list
        print(f" * {item.capitalize()}")  # prints items in a list capitalized
        return


def pickup():
    """In a certain part of the map you can pick up an item"""
    global Items, Inventory, row, col  # global variables that the function pulls from the lists above
    location_description = Map[row][col]  # current location
    if location_description == 'flowerbed':  # if you are in the flowerbed
        for item in Items:
            print("You picked up a key.")  # print item being added to inventory
            Inventory.append(item)  # add item to inventory


def menu_options():
    """Menu options"""
    print('* Walk')  # print walk
    print('* Inventory')  # print inventory
    print('* Quit')  # print quit


while playing:  # starts main loop
    messages()
