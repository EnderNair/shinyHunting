#Author: Adrian Madsen
#Date: 3/26/2023
#Autmoatic Wild Encounter Shiny Finder

import pyautogui as py
import cv2
import keyboard
from pynput.keyboard import Key, Controller
import time
import telegram
import asyncio

print('Beginning Automagic Shiny Hunting Script...')
start_time = time.time()

#creates instance of keyboard
keyboard = Controller()

# Encounter count
encounters = 0

#Shiny Aron: 2052 encounters, 410 Minutes
#Shiny Lotad: 13941 encounters
#Shiny Wurmple: 5839 encounters, 1210 minutes

# Load the images to search for
#zig = cv2.imread('Zigzagoon.png')
#pooch = cv2.imread('Poochyena.png')
#ralts = cv2.imread('Ralts.png')
#lotad = cv2.imread('Lotad.png')
#sursk = cv2.imread('Surskit.png')
#wurmp = cv2.imread('Wurmple.png')
zubat = cv2.imread('Zubat.png')
aron = cv2.imread('Aron.png')
maku = cv2.imread('Makuhita.png')
abra = cv2.imread('Abra.png')
sabl = cv2.imread('Sableye.png')
trainer = cv2.imread('Trainer.png')

# Makes player walk back and forth until it encounters a pokemon
def walk():
    found_trainer = False
    while found_trainer is False:
        Trainer = py.locateOnScreen(trainer, confidence=0.9)
        if Trainer:
            found_trainer is True
            break
        else:
            print("Searching for Pokemon...")
            py.keyDown('left')
            time.sleep(.05)
            py.keyUp('left')
            py.keyDown('right')
            time.sleep(.05)
            py.keyUp('right')
            py.keyDown('left')
            time.sleep(.05)
            py.keyUp('left')
            py.keyDown('right')
            time.sleep(.05)
            py.keyUp('right')
            time.sleep(.05)

#Exits the battle
def runaway():
    print("No Shiny Pokemon Detected.")
    py.keyDown('x')
    time.sleep(.1)
    py.keyUp('x')
    time.sleep(1.6)
    py.keyDown('right')
    time.sleep(.17)
    py.keyUp('right')
    print("Running...")
    time.sleep(.17)
    py.keyDown('down')
    time.sleep(.17)
    py.keyUp('down')
    py.keyDown('x')
    time.sleep(.15)
    py.keyUp('x')
    py.keyDown('x')
    time.sleep(.15)
    py.keyUp('x')
            
# Main Function
time.sleep(1)
found_image = True

while found_image:
    walk()
    time.sleep(1)
    Zubat = py.locateOnScreen(zubat, confidence=0.9)
    Aron = py.locateOnScreen(aron, confidence=0.9)
    Makuhita = py.locateOnScreen(maku, confidence=0.9)
    Abra = py.locateOnScreen(abra, confidence=0.9)
    Sableye = py.locateOnScreen(sabl, confidence=0.9)
    
    if Zubat is None and Aron is None and Makuhita is None and Abra is None and Sableye is None:
        found_image = False
        break
    
    runaway()
    
    encounters += 1
    print("Encounters:", encounters)
    
keyboard.press('j')
time.sleep(.1)
keyboard.release('j')

end_time = time.time()
elapsed_time = end_time - start_time
minutes_time = elapsed_time / 60
print("Hooray! A Shiny has been Found!")
print("Total Encounters:", encounters)
print("Total time: {:.2f} minutes".format(minutes_time))

#Telegram bot sends message to Reminders Group Chat
bot = telegram.Bot(token='5872208164:AAFbiIGmzh8M_sHovkYhKZ0rss4IwFNRWyo')

chat_id = '-1001579744417'
text = 'Hello Adrian. Your Shiny Hunting Script has found a Shiny Pokemon!'

async def send_telegram_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

asyncio.run(send_telegram_message(chat_id, text))

