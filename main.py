"""
gToWbot
Copyright (C) 2021  grildroid

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys, time, threading

import keyboard
import win32gui, win32con, win32api

from modules.cvprocessor import CvProcessor, Payload
from modules.operations import TowOperations

__author__ = "grildroid"
__version__ = "1.0"

project_name = "gToWbot"

before_autoresources_start = 7 # [int] Seconds

class TerminateProcessor:
    close_flag = False

    def check_terminate(self):
        if self.close_flag:  # Checking for "Q" (exit) button pressed status
            payloadOBJ.stop()
            sys.exit(1)


class ToWWindow:
    prefix = 'ToWWindow' # class prefix
    hwnd = 0
    window_size = (1360, 720) # Don't change the window size parameter. The cvprocessor may stop working. Coordinate points (1360, 720)
    window_pos = (0, 0) # position of the window

    def check_existance(self):
        self.hwnd = win32gui.FindWindow(None, "Tales of Wind")
        return self.hwnd

    def move_window(self):
        if self.check_existance() != 0:
            win32gui.ShowWindow(self.hwnd, win32con.SW_NORMAL) # making window visible
            win32gui.SetForegroundWindow(self.hwnd) # set window foreground
            win32gui.MoveWindow(self.hwnd, self.window_pos[0], self.window_pos[1], self.window_size[0], self.window_size[1], True) # moving window on the first monitor (main) to the top left corner and setting the window size


class AutoResources:
    prefix = 'AutoResources'

    module_name = 'auto_resources'
    active = False

    resources_data = [
        {'name': 'fish', 'coords': (680, 400)},
        {'name': 'wood', 'coords': (690, 240)},
        {'name': 'stone', 'coords': (750, 160)},
    ]

    def start(self):
        self.active = True
        print(f'[{self.prefix}] [INFO] Started main cycle')
        cvprocessor.start_main()
        self.__main()

    def stop(self):
        self.active = False
        print(f'[{self.prefix}] [INFO] Stopped main cycle')
        cvprocessor.stop()

    def __main(self):
        countdown = 0
        for second in range(1, before_autoresources_start+1):
            terminateprocOBJ.check_terminate() # Checking the close_flag parameter
            countdown += 1
            print(f'[{self.prefix}] [INFO] Seconds before AutoResources starts: {before_autoresources_start - countdown}')
            time.sleep(1)

        for resource in self.resources_data:
            terminateprocOBJ.check_terminate() # Checking the close_flag parameter

            print(f"[INFO] Going to {resource['name']} {resource['coords']}")

            if self.active:
                check_map__counter = 0
                while self.active: # [CYCLE] Searching and clicking on map
                    terminateprocOBJ.check_terminate() # Checking the close_flag parameter

                    operations.open__map() # Opening the farm map
                    time.sleep(2) # Waiting for 2 seconds for map loading

                    if check_map__counter > 3:
                        print(f'[WARNING] Map cant be opened!')
                        terminateprocOBJ.close_flag = True # Setting the terminate option
                        break # Exiting the cycle with terminate command

                    if cvprocessor.check(cvprocessor.template__farm_map) > 0: # Checking for the map opens -> If map opens
                        break # Exiting the done cycle
                    else:
                        check_map__counter += 1

                terminateprocOBJ.check_terminate() # Checking the close_flag parameter

                operations.click__map_point(resource['coords']) # Click on map coordinate. Going to resource

                check_resource_use_button = 0
                while self.active: # [CYCLE] Search 'USE' button
                    terminateprocOBJ.check_terminate() # Checking the close_flag parameter

                    if check_resource_use_button >= 30: # If can't find 'USE' button more than 30 cycles
                        break # Going to the next resource

                    time.sleep(1) # Every 1 second check the button existance

                    if cvprocessor.check(cvprocessor.template__use_button) > 0: # Check 'USE' button existance
                        break # IF button found -> going to clicking block
                    else: # IF button not found
                        check_resource_use_button += 1


                if check_resource_use_button < 30:
                    terminateprocOBJ.check_terminate()  # Checking the close_flag parameter

                    print(f"[INFO] Resource {resource['name']} reached")
                    no_use_button = 0
                    time.sleep(1) # Waiting for 'USE' button appears

                    while self.active: # Цикл ресурса
                        terminateprocOBJ.check_terminate() # Checking the close_flag parameter

                        if cvprocessor.check(cvprocessor.template__use_button) > 0: # Checking the existance of 'USE' button
                            print('[DEBUG] [CHECK] Founded use button')
                            operations.click__use_button() # Clicking on 'USE' button
                            time.sleep(12) # Waiting 12 seconds for resource collecting
                            no_use_button = 0
                        else:
                            no_use_button += 1

                        if no_use_button >= 5: # If 'USE' button can't be found more than 5 times
                            print(f'[INFO] The resource {resource["name"]} is fully сollected')
                            break # Going to the next resource

        self.stop()




class StopButton:
    prefix = 'StopButton'
    thread_run = None
    thread = None

    def start_thread(self):
        self.thread_run = True
        self.thread = threading.Thread(target=self.__main, daemon=True)
        self.thread.start()
        print(f'[{self.prefix}] [i] Started main thread')

    def stop_thread(self):
        self.thread_run = False
        print(f'[{self.prefix}] [i] Stopped main thread')

    def __main(self):
        while self.thread_run:
            time.sleep(0.1)
            if keyboard.is_pressed('q'):
                if auto_resourcesOBJ.active:
                    terminateprocOBJ.close_flag = True # Setting the terminate option
                    print('[INFO] Pressed "Q" button')
                    auto_resourcesOBJ.stop() # if pressed q button - stopping the "auto resources" module

class TUI:
    def main(self):
        print(f'\n=============> {project_name} ({__version__}) <=============')
        print(f'{project_name} Copyright © 2021 grildroid')
        print(f'{project_name} licensed under GNU GPL-3. Read the LICENSE file for more details!\n')
        print('[1] AutoResources')
        print('[9] CoordinatesCollector')
        print('')

        choice = str(input('>>:'))

        if choice == '1':
            auto_resourcesOBJ.start()

        elif choice == '9':
            cvprocessor.start_cc()
            payloadOBJ.start()

        else:
            print(f'Entered wrong value: {choice}')

if __name__ == '__main__':
    win32api.SetConsoleTitle(project_name)

    towwindow = ToWWindow() # ToW window controller
    result = towwindow.check_existance() # Checking ToW window existance (is process running in system)

    if result == 0:
        print('[WARNING] Open the ToW game before starting the bot!')
        input('PRESS ENTER TO CLOSE THIS WINDOW')
        exit()

    else:
        towwindow.move_window() # Resize, move and set foregroud ToW window

        terminateprocOBJ = TerminateProcessor()

        stopbuttonOBJ = StopButton() # Stop button controller object
        stopbuttonOBJ.start_thread()

        cvprocessor = CvProcessor()
        operations = TowOperations()

        payloadOBJ = Payload()
        auto_resourcesOBJ = AutoResources()  # AutoResources module

        tui = TUI()
        tui.main()
