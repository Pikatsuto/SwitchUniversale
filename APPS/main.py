from sys import platform as _platform
import os
from Commands.Clear import Clear
from Commands.Credits import Credits
from Commands.InstallDriver import InstallDriver
from Commands.IsMySwitchPatched import IsMySwitchPatched
from Commands.LanPlay import LanPlay
from Commands.Menu import Menu
from Commands.NSCBuilder import NSCBuilder
from Commands.NSPToNSZConverter import NSPToNSZConverter
from Commands.PayloadLoader import PayloadLoader
from Commands.SDFlacher import SDFlacher
from Commands.SysDVR import SysDVR
from Commands.SwitchGet import SwitchGet

os.system("@ECHO off") 

if _platform == 'win32':
    os.system('COLOR 60')

CMD = True

# # Menu [Chois]
if CMD == True:
    PageMenu = 0
    InputMenu = ""
    while InputMenu != "q":
        Menu()
        InputMenu = input("Que choisissez-vous ? ")
        InputMenu = InputMenu.lower()
        print(InputMenu)        

        if InputMenu == "c":
            Credits()

        elif InputMenu == "q":
            os.system("quit")
        else:
            try:
                ChoisMenu = int(InputMenu)
            except ValueError:
                ChoisMenu = 30

            if ChoisMenu == 1:
                NSCBuilder()

            elif ChoisMenu == 2:
                NSPToNSZConverter()

            elif ChoisMenu == 3:
                LanPlay()

            elif ChoisMenu == 4:
                SysDVR()

            elif ChoisMenu == 5:
                Clear()

            elif ChoisMenu == 6:
                Clear()

            elif ChoisMenu == 7:
                Clear()

            elif ChoisMenu == 8:
                SDFlacher()

            elif ChoisMenu == 9:
                PayloadLoader()

            elif ChoisMenu == 10:
                Clear()

            elif ChoisMenu == 11:
                IsMySwitchPatched()

            elif ChoisMenu == 12:
                InstallDriver()
                
            elif ChoisMenu == 13:
                Clear()
                SwitchGet()
                
            elif ChoisMenu == 14:
                Clear()

    Clear()