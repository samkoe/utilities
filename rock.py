# rock.py

import time
import random

# Game Intro
print("Let's play Rock, Paper, Scissors.\n")
time.sleep(1)

# Countdown
print("Ready?\n")
time.sleep(1)
print("1...")
time.sleep(1)
print("2...")
time.sleep(1)
print("3...")
time.sleep(1)

play_again = True

while play_again:

	# Player inputs choice
	player = ""
	while player != "rock" and player != "paper" and player != "scissors":
		player = input("\nEnter your choice (rock, paper, or scissors) > ")

	# Computer makes random choice
	rand_choice = random.randint(1, 3)
	if rand_choice == 1:
		computer = "rock"
	elif rand_choice == 2:
		computer = "paper"
	else:
		computer = "scissors"

	print("\nThe computer chooses: ", computer, "\n")
	time.sleep(1)

	# Test for winner
	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer.title(), "covers", player)
		else:
			print("You win!", player.title(), "smashes", computer)

	elif player == "paper":
		if computer == "rock":
			print("You win!", player.title(), "covers", computer)
		else:
			print("You lose!", computer.title(), "cut", player)

	else:
		if computer == "rock":
			print("You lose!", computer.title(), "smashes", player)
		else:
			print("You win!", player.title(), "cut", computer)

	play_again = input("\nWant to play again (Y or N)? > \n")
	if play_again.lower() == "n" or play_again.lower() == "no":
		play_again = False







