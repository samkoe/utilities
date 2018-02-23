# zombie_part3.py
#----------------------------------------------------------
# Part 3 refactors the place_monster() function and the 
# monster attribute variables into a create_monster() 
# function. It also creates the place_cheese() function and
# the "take" command to pick up the cheese.
#
# We also debug some of our command processing in the game
# loop.
#----------------------------------------------------------#

# import libraries
import os
import random

# create map
#
# kitchen => dining room
# dining room => kitchen, ballroom
# ballroom => dining room
#

#------------------------------ FUNCTIONS ------------------------------#

# room function (controls map and room details)
def room_details(current):
    if current == "Kitchen":
        print("Kitchen")
        print("--------------------")
        print("A dank and dirty room buzzing with flies.")
        print("The dining room is east.")

    elif current == "Dining Room":
        print("Dining Room")
        print("--------------------")
        print("A large room with ornate golden decorations on each wall.")
        print("The kitchen is west.")
        print("The ballroom is north.")

    else:
        print("Ballroom")
        print("--------------------")
        print("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")
        print("The dining room is south.")

# move function (gives possible room directions)
def move(current, direction):
    if current == "Kitchen":
        if direction.lower() == "east":
            current = "Dining Room"

    elif current == "Dining Room":
        if direction.lower() == "west":
            current = "Kitchen"
        else:
            current = "Ballroom"

    else:
        if direction.lower() == "south":
            current = "Dining Room"

    return current

# make zombie function (randomly located)
def create_zombie():
    rand_room = random.randint(1, 3)
    if rand_room == 1:
        room = "Kitchen"
    elif rand_room == 2:
        room = "Dining Room"
    elif rand_room == 3:
        room = "Ballroom"

    name = "Larry"
    description = "A smelly zombie"
    message = "What's up, dude! I'm hungry, and I like brains."

    return room, name, description, message

def place_cheese():
    rand_cheese = random.randint(1, 3)
    if rand_cheese == 1:
        room = "Kitchen"
    elif rand_cheese == 2:
        room = "Dining Room"
    elif rand_cheese == 3:
        room = "Ballroom"

    return room

#------------------------------ GAME ------------------------------#

# clear screen and give directions
os.system("clear")

print("+-------------------+".center(50))
print("|    Zombie Room    |".center(50))
print("+-------------------+".center(50))

# game loop

current_room = "Kitchen"
zombie_room, zombie_name, zombie_description, zombie_message = create_zombie()
cheese_room = place_cheese()
have_cheese = False

dead = False

while dead == False:
    # print current room
    print("\n")
    room_details(current_room)
    # print zombie details
    if current_room == zombie_room:
        print()
        print(zombie_description, "named", zombie_name, "is here! He looks like he has something to say.")
    if current_room == cheese_room:
        print()
        print("A large, stinky chunk of cheese moulders in the corner.")

    # prompt user for command
    command = input("> ")

    # evaluate and execute move command
    if command.lower() in ["north", "south", "east", "west"]:
        current_room = move(current_room, command)

    # talk to zombie - if there is one! 
    elif command.lower() == "talk":
        if current_room == zombie_room:
            print(zombie_message)
        else:
            print("Um...There's no one else here.")

    # put cheese in backpack
    elif command.lower() == "take":
        if current_room == cheese_room:
            have_cheese = True
            print("You put the cheese in your backpack. Now you can fight the zombie!")
        else:
            print("There's nothing here to take!")

    # warn user about invalid commands
    else:
        print("I don't know how to " + command)
        print("\n-----------------------------------")



