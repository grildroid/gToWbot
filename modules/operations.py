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

import pyautogui

class TowOperations:
    prefix = 'TowOperations'
    open__map__coordinates = (1284, 87) # Координаты карты (Кнопки открытия карты) (x, y)
    close__map__coordinates = (1055, 45) # Координаты карты (Кнопки закрытия карты) (x, y)
    use_button__coordinates = (967, 499)  # Координаты кнопки "Использовать" (x, y)


    def click__map_point(self, coordinates):
        pyautogui.click(x=coordinates[0], y=coordinates[1], clicks=1)
        print(f'[{self.prefix}] [DEBUG] Clicked on map point: {coordinates}')

    def open__map(self):
        pyautogui.click(x=self.open__map__coordinates[0], y=self.open__map__coordinates[1], clicks=1)
        print(f'[{self.prefix}] [DEBUG] Opened map')

    def close__map(self):
        pyautogui.click(x=self.close__map__coordinates[0], y=self.close__map__coordinates[1], clicks=1)
        print(f'[{self.prefix}] [DEBUG] Closed map')

    def click__use_button(self):
        pyautogui.click(x=self.use_button__coordinates[0], y=self.use_button__coordinates[1], clicks=1)
        #print(f'[{self.prefix}] [DEBUG] Clicked on use button')
