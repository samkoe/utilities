# zombie_part4.py
#----------------------------------------------------------
# Part 4 adds the fight command (finally!) and a new
# function--fight_zombie()--to randomly determine the 
# outcome of the fight.
#
# We also spend some time cleaning up the output of the 
# game to improve UX.
#----------------------------------------------------------#

# import libraries
import os
import random
import time

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

def fight_zombie():
    print("You throw the cheese at the zombie's head...\n")
    time.sleep(2.5)

    outcome = random.randint(1, 2)
    if outcome == 1:
        win = True      # user kills zombie
    else:
        win = False     # user killed by zombie

    return win

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
win = False

while dead == False and win == False:
    # print current room
    print("\n")
    room_details(current_room)
    # print zombie details
    if current_room == zombie_room:
        print()
        print(zombie_description, "named", zombie_name, "is here! He looks like he has something to say.")
    if current_room == cheese_room:
        print()
        print("A large, stinky chunk of cheese moulders in the corner.\n")

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
            print("Um...There's no one else here.\n")

    # put cheese in backpack
    elif command.lower() == "take":
        if current_room == cheese_room:
            have_cheese = True
            print("You put the cheese in your backpack. Now you can fight the zombie!\n")
        else:
            print("There's nothing here to take!\n")

    # fight zombie
    elif command.lower() == "fight":
        if current_room == zombie_room:
            if have_cheese == True:
                result = fight_zombie()
                if result:
                    print("You have defeated the zombie! The stinky cheese is yours to keep!\n")
                    win = True

                else:
                    print("The zombie defeats you. That's what you get for using cheese as a weapon!\n")
                    dead = True

            else:
                print("You have no weapon, so you attack the zombie with your bare hands...\n")
                time.sleep(2)
                print("But the zombie easily overpowers you and turns you into a snack.\n")
                dead = True

        else:
            print("There's no one here to fight.")

    # warn user about invalid commands
    else:
        print("I don't know how to " + command)
        print("\n-----------------------------------")



