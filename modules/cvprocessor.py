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

import os, sys, time, threading, numpy

import mss
import cv2.cv2 as cv2

class CvProcessor:
    prefix = 'CvProcessor'

    cv2wintitle = 'cv2 - grildroid towbot'
    current_frame = 0
    cvimg = None
    running = None
    threadOBJ = None

    visualize_process = False # [True/False] Creating cv2 window and visualizing the process of cv2
    screenshot = mss.mss()

    clicks_counter = 0
    last_coordinate = (0, 0)

    def __init__(self):
        if getattr(sys, 'frozen', False): # Code block for --onefile parameter of pytoexe
            templates_folder = os.path.join(sys._MEIPASS, 'data', 'templates')
        else: # Code block for path to project templates folder
            templates_folder = os.path.join(os.getcwd(), 'data', 'templates')

        self.template__use_button = cv2.imread(os.path.join(templates_folder, 'button_use.png'), cv2.IMREAD_GRAYSCALE) # Template image. Button "USE"

        print(f'[INFO] Templates folder path: {templates_folder}')

    def start_main(self):
        self.running = True
        self.threadOBJ = threading.Thread(target=self.__main, daemon=True)
        self.threadOBJ.start() # Start the thread

    def start_cc(self):
        self.running = True
        self.threadOBJ = threading.Thread(target=self.__cordinates_collector, daemon=False)
        self.threadOBJ.start() # Start the thread

    def stop(self):
        self.running = False
        cv2.destroyAllWindows()

        if self.threadOBJ is not None:
            self.threadOBJ.join() # Stop the thread


    def __main(self):
        if self.visualize_process: # If visualize cv2 process is turned on
            cv2.namedWindow(self.cv2wintitle) # Creating cv2 window with title = cv2wintitle

        while self.running or cv2.getWindowProperty(self.cv2wintitle, 0) >= 0:
            self.current_frame += 1  # +1 to the frames counter

            cvimg = numpy.asarray(self.screenshot.grab((0, 0, 1360, 720)))  # Screenshoting ToW window. Converting to numpy arrays format
            self.cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)  # Converting BGR format to GRAY

            if self.visualize_process:
                cv2.putText(img=self.cvimg, text=f'frame:{self.current_frame}', org=(300, 80), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0, 0, 0), thickness=1)  # Rendering frame counter text
                cv2.imshow(self.cv2wintitle, self.cvimg)  # Image rendering to cv2 window

            if cv2.waitKey(500) & 0xFF == 27: # If ESC pressed (code: 27) - stop the script
                self.running = False
                cv2.destroyAllWindows()
                break

        exit()

    def __cordinates_collector(self):
        cv2.namedWindow(self.cv2wintitle)  # Creating cv2 window with title = cv2wintitle
        cv2.setMouseCallback(self.cv2wintitle, self.get_click_pos)

        while self.running:
            self.current_frame += 1 # +1 to the frames counter

            self.cvimg = numpy.asarray(self.screenshot.grab((0, 0, 1360, 720))) # Screenshoting ToW window. Converting to numpy arrays format
            self.cvimg = cv2.cvtColor(self.cvimg, cv2.COLOR_BGR2GRAY) # Converting image to gray (for templates collecting)

            cv2.putText(img=self.cvimg, text=f'frame:{self.current_frame}', org=(80, 600), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0, 0, 0), thickness=1)
            cv2.putText(img=self.cvimg, text=f'time:{time.strftime("%H:%M:%S")}', org=(80, 630), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0, 0, 0), thickness=1)
            cv2.putText(img=self.cvimg, text=f'coord:{self.last_coordinate}', org=(80, 660), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0, 0, 0), thickness=1)

            cv2.imshow(self.cv2wintitle, self.cvimg)  # Image rendering to cv2 window

            if cv2.waitKey(5) & 0xFF == 27: # If ESC pressed (code: 27) - stop the script
                self.running = False
                cv2.destroyAllWindows()
                break

        exit()


    def match(self, gray_template, coeff):
        obj_counter = 0  # Founded objects counter

        w, h = gray_template.shape[::-1]  # Transforming (y, x) coordinates system to (x, y)

        result = cv2.matchTemplate(self.cvimg, gray_template, cv2.TM_CCOEFF_NORMED)  # Finding object by template
        loc = numpy.where(result >= coeff)  # Filtering objects by coefficient

        # Drawing rectangle on the founded object
        for pt in zip(*loc[::-1]):
            cv2.rectangle(self.cvimg, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
            obj_counter += 1

        obj_counter = int(obj_counter / 4)  # Founded object counter on cvimg

        return obj_counter

    def get_click_pos(self, event, x, y, none1, none2):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.clicks_counter += 1
            self.last_coordinate = (x, y)
            cv2.circle(self.cvimg, (x, y), 15, (0, 0, 255), -1)
            print(f'[{self.prefix}] ({time.strftime("%H:%M:%S")}) <{self.clicks_counter}> Clicked position coordinates: {x, y} (x, y)')
            return x, y

class Payload:
    prefix = 'Payload'
    __running = False
    __thread = None

    def __init__(self):
        self.__thread = threading.Thread(target=self.__main, daemon=False)

    def start(self):
        self.__running = True
        print(f'[{self.prefix}] [INFO] Payload thread started')
        self.__thread.run()

    def stop(self):
        if self.__thread is not None:
            self.__running = False
            print(f'[{self.prefix}] [INFO] Payload thread stopped')

    def __main(self):
        while self.__running:
            pass
