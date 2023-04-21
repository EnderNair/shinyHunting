import pyautogui
import cv2
import keyboard
from pynput.keyboard import Key, Controller
import time

#creates instance of keyboard
keyboard = Controller()

# Load the image to search for
image = cv2.imread('Treeko.png')

# Find the image on the screen and get its location
location = pyautogui.locateOnScreen(image)

#previous attempt took 8761 but game must have crashed?
resets = 12800

# Set a flag variable to keep track of whether the image has been found
found_image = True

# Start a while loop that will continue until the image is found
while found_image:
    # Search the screen for the image
    location = pyautogui.locateOnScreen(image)
    
    # If the image is found, set the flag variable to True and break out of the loop
    if location is None:
        found_image = False
        break
    
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

keyboard.press('j')
time.sleep(.1)
keyboard.press('k')
time.sleep(.1)
keyboard.press('3')
print("Hooray! A Shiny has been Found!")
print('Total Encounters:')
print(resets)
