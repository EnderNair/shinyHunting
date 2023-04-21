# shinyHunting
This is Python code I have created that will hunt for various shiny pokemon automatically using emulators . Various different methods are used, but mainly image tracking in Python. It is specifically meant for hunting in Generation 3, but could very easily be updated to work for any generation.

In order to run this code, you will have to install some libraries use pip. There are a couple specific ones I can recall but you may need to do some testing on your own. I ran all of this code in Linux, so it may require some different libraries in Windows. I gave all of my compiler errors to ChatGPT and it told me what libraries to install. It has been a while so I don't remember all of them, so you will have to trial and error it yourself until it works. I recommend trying the findShinyTreeko.py before the shinyWildEncounter.py as it is simpler to test.

pyautogui
pynput
cv2

You'll need a library that will let your code use imageTracking on your screen.


FOR findShinyTreeko:

This code is specifically designed for soft-resetting to find shiny Treeko. I used the mGBA emulator and ran it at 5x speed. This is important to keep in mind because there is timing for button presses. The timing can be adjusted if you emulate your game slower or faster.

This code can be reused to hunt for the other starters as well. Regardless, you will need to provide a screenshot of the starter Pokemon you wish to hunt for within the same directory as the findShinyTreeko file. I recommend taking a small screenshot of only a small part of the pokemon. The less pixels it has to compare, the more reliably it will work. Otherwise, you can set the confidence value to a smaller percentage. Your milage may vary.

I have provided the screenshot for Treeko in the repository

HOW TO USE:
1. Open Emulator
2. Reach the first battle screen with Treeko on the field
3. Run findShinyTreeko.py
4. Quickly click or Alt+Tab the Emulator so that it is selected
5. Wait for script to find Shiny Treeko


FOR shinyWildEncounter:

This code will need to be adjusted for which specific pokemon you are shiny hunting. The way I have it set up is for it to hunt EVERY possible Pokemon on the route you are hunting in. This means you will need to have screenshots of every Pokemon that you can encounter in the route. Due to the nature of the code, it will NOT work if it cannot detect every Pokemon.

I also added basic functionality for a Telegram bot to send a message once the script found a shiny. I have commented this out and removed the token and server addresses. You will need to research how to create your own Telegram bot and fill in the data needed for that. Otherwise, I'm sure it's relatively easy to setup a Discord bot to do something similarly as well.

HOW TO USE:
1. Enter the route in which you will be shiny hunting
2. Take/Gather screenshots of every Pokemon on the route
3. Adjust the code to properly read the png files
4. Position your trainer to be in grass (they will move left and right)
4. Run shinyWildEncounter.py
5. Quickly click or Alt+Tab the Emulator so that it is selected
6. Wait for script to find a Shiny Pokemon
