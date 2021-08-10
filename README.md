# gToWbot
  gToWbot (Grildroid's Tales of Wind bot) - by using this simple python3 script you can automatically collect resources (fish, wood, stone) at your farm. gToWbot using computer vision module OpenCV.

  gToWbot don't collect and don't transfer any of your personal data!  
  
<p align="center">
<a href="/releases"><img src="https://img.shields.io/github/v/release/grildroid/gToWbot?style=flat-square" alt="Github release Badge"/></a>
<a href="/license"><img src="https://img.shields.io/github/license/grildroid/gToWbot?style=flat-square" alt="Github license Badge"/></a>
</p>

  **❤️ Come visit our Telegram channel with news about gToWbot updates, some blog stuff and other @grildroid projects! ❤️**

<p align="center">
<a href="https://t.me/grildroidcave"><img src="https://img.shields.io/badge/-Telegram%20channel-blue?style=for-the-badge&logo=Telegram" alt="Telegram Badge"/></a>
</p>

____
  * Systems: Windows 10  
  * UI: Console-based
  
# License
  gToWbot is a free opensource project!  
  gToWbot Copyright © 2021 grildroid  
  [Licensed under GNU General Public License v3 (GPL-3)](/LICENSE)  

# Important
Currently gToWbot works only with ToW with russian translation!

* Press the "Q" button if you need to stop the bot, or just close the gToWbot console
* When a bot controls a character and collect resources, the bot takes control of the mouse. Do not move the mouse while bot doing its work, otherwise errors may occur
* After all resources is collected - bot stops his work and closing the console
* When bot starts - the ToW game window will be automatically resized to 1360x720 and moving to the main monitor at top left corner. Don't move, hide, resize, obscure the window! Bot uses coordinates system, so mouse clicks will be missed

# Getting Started
1. Run the TalesOfWind game
2. Manually move to the farm and check your instuments in inventory
3. Run the gToWbot.exe
4. Type the number of AutoResources parameter at console window and press enter
5. After 5 seconds the bot will be started and your character will go to collect resources on the farm automatically

Press ESC instead of Q when you choosing the CoordinatesCollector to close the script

# Plans
* Make gToWbot works with other game translations
* Exiting from CoordinatesCollector by pressing Q
* More modules such as AutoResources
* Logging system

# Technologies
* Writed on Python3.9 
* Using external modules: opencv-python, mss, keyboard, pywin32.
  
