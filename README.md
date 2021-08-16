# gToWbot
  gToWbot (Grildroid's Tales of Wind bot) - by using this simple python3 script you can automatically collect resources (fish, wood, stone) at your farm. gToWbot using computer vision module OpenCV. gToWbot don't collect and don't transfer any of your personal data!  
  
<a href="#"><img title="gToWbot user interface (version: 1.1)" src="https://user-images.githubusercontent.com/55492813/129568026-ad5e6e0e-2b9a-4421-9f07-73e4fff196b8.png"/></a>

<p align="center">
<a href="https://github.com/grildroid/gToWbot/releases"><img src="https://img.shields.io/github/v/release/grildroid/gToWbot?style=flat-square" alt="Github release Badge"/></a>
<a href="/LICENSE"><img src="https://img.shields.io/github/license/grildroid/gToWbot?style=flat-square" alt="Github license Badge"/></a>
<a href="https://sourceforge.net/projects/gtowbot/files/latest/download"><img alt="Download gToWbot" src="https://img.shields.io/sourceforge/dt/gtowbot.svg" ></a>
</p>

<p align="center">
  <a href="https://sourceforge.net/projects/gtowbot/files/latest/download"><img alt="Download gToWbot" src="https://a.fsdn.com/con/app/sf-download-button" width=276 height=48 srcset="https://a.fsdn.com/con/app/sf-download-button?button_size=2x 2x"></a>
</p>

  

<p align="center">
❤️ <b>Come visit our Telegram channel with news about gToWbot updates, some blog stuff and other @grildroid projects!</b> ❤️
</p>
<p align="center">
  <a href="https://t.me/grildroidcave"><img src="https://img.shields.io/badge/-Telegram%20channel-blue?style=for-the-badge&logo=Telegram" alt="Telegram Badge"/></a>  
</p>

____
  * Systems: Windows 10  
  * User Interface: Console-based
  
# License
  gToWbot is a free opensource project!  
  gToWbot Copyright © 2021 grildroid  
  [Licensed under GNU General Public License v3 (GPL-3)](/LICENSE)  

# Important
* When the bot starts up, the ToW window automatically resizes to 1360x720 and moves to the main monitor (1) in the upper left corner. Don't move the window, resize it, hide or overlap the ToW window with other applications!
* When the bot is running, it controls the character and does its job. At this point, the bot takes control of the mouse cursor. Do not move the mouse cursor while the bot is doing its job, it can lead to errors in the bot!
* The bot uses the coordinate system on which it clicks with the mouse cursor. While the bot is running - any changes in the game window, or movements of the mouse cursor can lead to errors!
* Press the "Q" button if you need to stop the bot.
* After completing its work - the bot stops and closes the console window. After that, you can manually return the ToW window to its original size and position.

# Getting Started
1. Start the game Tales of Wind
2. Run the bot gToWbot.exe
3. Enter the number of the module you need in the opened console window and press ENTER
4. After 5 seconds, the bot starts executing the module you selected 

Press ESC instead of Q when you choosing the CoordinatesCollector to close the script

# Plans
* Exiting from CoordinatesCollector by pressing Q
* More modules
* Web-gui
* Logging system

# Technologies
* Writed on Python3.9 
* Using external modules: opencv-python, mss, keyboard, pywin32.
* Remember to install manually pywin32 for python3.9!
* Builded (as .exe file) for Windows by pytoexe
  
