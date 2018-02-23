# zombie_part2.py
#----------------------------------------------------------
# Part 2 creates a single zombie and places it in a random 
# room. It also creates conversation for the zombie and 
# adds the 'talk' command.
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

# make monster function (randomly located)
def place_monster():
    rand_room = random.randint(1, 3)
    if rand_room == 1:
        zombie_room = "Kitchen"
    elif rand_room == 2:
        zombie_room = "Dining Room"
    elif rand_room == 3:
        zombie_room = "Ballroom"

    return zombie_room

#------------------------------ GAME ------------------------------#

# clear screen and give directions
os.system("clear")

print("+-------------------+".center(50))
print("|    Zombie Room    |".center(50))
print("+-------------------+".center(50))

# game loop

current_room = "Kitchen"
zombie_room = place_monster()

# create monster
zombie_name = "Larry"
zombie_description = "A smelly zombie"
zombie_message = "What's up, dude! I'm hungry, and I like brains."

dead = False

while dead == False:
    # print current room
    print("\n")
    room_details(current_room)
    # print monster details
    if current_room == zombie_room:
        print()
        print(zombie_description, "named", zombie_name, "is here! He looks like he has something to say.")

    # prompt user for command
    command = input("> ")

    # evaluate and execute command
    if command.lower() in ["north", "south", "east", "west"]:
        current_room = move(current_room, command)
    elif command.lower() == "talk":
        print("\n[" + zombie_name + " says]: " + zombie_message)
    else:
        print("I don't know how to " + command)
        print("\n-----------------------------------")



