# game1.py

# import libraries
import RPi.GPIO as GPIO
import time
import os
import random

# Setup GPIO library and constants
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GREEN = 18
BLUE = 23
RED = 24
BUTTONPIN = 25

# Setup up input/output pins
for i in [GREEN, BLUE, RED]:
    GPIO.setup(i, GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN)

# Listen for button press
def button_press(points, led):
    start = time.time()		# beginning of light-on interval
    ButtonNotPressed = True	# button has not been pressed
    while ButtonNotPressed:	# while the button has not been pressed
        if GPIO.input(BUTTONPIN) == False and led = BLUE:	# button pressed, led is blue
            now = time.time()	# time when button was pressed
            ButtonNotPressed = False
            if (now - start) <= 0.2:	# if button pressed within .2 sec
                print("You scored a point.")
                points += 1
                time.sleep(0.2 - (now - start))	# wait until interval of .2 sec is over
        else:	# if button not pressed while light on
            now = time.time()	# measure interval
            if (now - start) > .2:	# turn light off after .2 sec
                break
    return points

# randomly select which led to turn on
def rand_light():
    leds = [GREEN, BLUE, RED]
    led = random.choice(leds)
    return led

# clear screen
os.system("clear")

# print title and instructions
print("----------------".center(50))
print("+    Game 1    +".center(50))
print("----------------".center(50))

print("\nPress the button when the blue light is on to score a point.")
time.sleep(2.5)
print("\nI'll time how long it takes you to get 10 points.")
time.sleep(2.5)
print("\nReady? Here we go...")
time.sleep(2)
print("\nBegin!")

# initialize points and start the game clock
points = 0
game_start = time.time()

# main game loop
while points < 10:	# while the player has less than 10 points	
    led = rand_light()	# randomly select light, store pin number in led
    GPIO.output(led, GPIO.HIGH)	# turn on light
    points = button_press(points, led)	# test for button press in .2 sec interval
    GPIO.output(led, GPIO.LOW)	# turn off light
    time.sleep(1)	# wait 1 sec before next light turns on

game_end = time.time()	# stop game clock
game_time = game_end - game_start	# calculate the player's time

print("\nIt took you", game_time, "to score 10 points!")	# print results to player
