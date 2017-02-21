# game2.py

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
def button_press(chances, led):
    start = time.time()		# beginning of light-on interval
    ButtonNotPressed = True	# button has not been pressed
    while ButtonNotPressed:	# while the button has not been pressed

        # button pressed when blue light is on
        if GPIO.input(BUTTONPIN) == False and led == BLUE:
            now = time.time()	# time when button was pressed
            ButtonNotPressed = False	# button has been pressed
            if (now - start) <= 0.1:	# if button pressed in 0.1 sec interval
                os.system("clear")	# clear screen and print victory message
                print()
                print("+------------+".center(50))
                print("+  You won!  +".center(50))
                print("+------------+".center(50))
                print()
                chances = 0		# set chances to zero to exit game loop
                time.sleep(0.1 - (now - start))	# wait remainder of 0.1 sec interval

        # button pressed when green or red light is on
        elif GPIO.input(BUTTONPIN) == False and (led == GREEN or led == RED):
            now = time.time()
            ButtonNotPressed = False
            if (now - start) <= 0.1:
                chances -= 1	# subtract one chance
                if chances == 0:	# if player is out of chances
                    os.system("clear")	# clear screen and print defeat message
                    print("\nYou lost! Better luck next time.")
                    print()
                else:
                    print("You missed! Chances left:", chances)	# print remaining chances
                time.sleep(0.1 - (now - start))

        # button not pressed in 0.1 sec interval
        else:
            now = time.time()	# measure interval
            if (now - start) > 0.1:	# turn light off after 0.1 sec
                break

    return chances	# return remaining chances to function call

# Clear Screen
os.system("clear")

# Print title and instructions
print("----------------".center(50))
print("+    Game 2    +".center(50))
print("----------------".center(50))

print("\nPress the button when the blue light is on to win.")
time.sleep(2.5)
print("\nIt will be tough...")
time.sleep(2.5)
print("\nYou only get 10 chances, so be careful.")
time.sleep(2.5)
print("\nReady? Here we go...")
time.sleep(2)
print("\nBegin!")
time.sleep(.5)

# main game loop
chances = 10
while chances > 0:
    # red led
    led = RED
    GPIO.output(RED, GPIO.HIGH)
    chances = button_press(chances, led)
    GPIO.output(RED, GPIO.LOW)
    if chances == 0:
        break
    time.sleep(0.1)
    
    # blue led
    led = BLUE
    GPIO.output(BLUE, GPIO.HIGH)
    chances = button_press(chances, led)
    GPIO.output(BLUE, GPIO.LOW)
    if chances == 0:
        break
    time.sleep(0.1)

    # green led
    led = GREEN
    GPIO.output(GREEN, GPIO.HIGH)
    chances = button_press(chances, led)
    GPIO.output(GREEN, GPIO.LOW)
    if chances == 0:
        break
    time.sleep(0.1)

    # blue led
    led = BLUE
    GPIO.output(BLUE, GPIO.HIGH)
    chances = button_press(chances, led)
    GPIO.output(BLUE, GPIO.LOW)
    if chances == 0:
        break
    time.sleep(0.1)
