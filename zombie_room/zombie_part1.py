# zombie_part1.py
#----------------------------------------------------------
# Part 1 creates the game title, beginning game loop,
# the room_details() function (to print the room details),
# and the move() function to change rooms.
#----------------------------------------------------------

# import libraries
import os
import random

# create map
#
# kitchen => dining room
# dining room => kitchen, ballroom
# ballroom => dining room
#

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

# clear screen and give directions
os.system("clear")

print("+-------------------+".center(50))
print("|    Zombie Room    |".center(50))
print("+-------------------+".center(50))

# game loop

current_room = "Kitchen"

dead = False

while dead == False:
    # print current room
    print("\n")
    room_details(current_room)

    command = input("> ")

    if command.lower() in ["north", "south", "east", "west"]:
        current_room = move(current_room, command)
    else:
        print("I don't know how to " + command)
        print("\n-----------------------------------")



