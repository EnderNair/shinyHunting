import pyautogui
import cv2
import keyboard
from pynput.keyboard import Key, Controller
import time

#creates instance of keyboard
keyboard = Controller()

# Load the image of Normal Treeko to search for
image = cv2.imread('Treeko.png')

# Find the image on the screen and get its location
location = pyautogui.locateOnScreen(image)

# This number will iterate for every reset and print once a shiny is found
resets = 0

# Set a flag variable to keep track of whether the image has been found
found_image = True

# Start a while loop that will continue until the image is found
while found_image:
    # Search the screen for the image (normal Treeko)
    location = pyautogui.locateOnScreen(image)
    
    # If Normal Treeko is not found, variable found_image will be set to False and break from the loop
    if location is None:
        found_image = False
        break
    
    # This code will navigate the player through the menus while soft-resetting
    # This code is set for finding Shiny Treeko at 5x speed in an emulator (mGBA)
    # Code may need to be adjusted for different conditions and outcomes.
    
    # This is the deafult hotkey in mGBA to soft reset the game. Adjust if needed.
    RESET = 'ctrl+r'
    
    time.sleep(0.15)
    pyautogui.hotkey(*RESET.split('+'))
    time.sleep(0.15)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    # Select Treeko
    keyboard.press(Key.left)
    time.sleep(0.15)
    keyboard.release(Key.left)
    time.sleep(0.35)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    keyboard.press('x')
    time.sleep(0.15)
    keyboard.release('x')
    time.sleep(0.35)
    
    print('Normal Treeko Count: ')
    resets += 1
    print(resets)

# Displays message once shiny has been found
print("Hooray! A Shiny has been Found!")
print('Total Encounters:')
print(resets)
