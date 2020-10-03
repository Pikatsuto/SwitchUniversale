import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def Menu():# Appelle la fonction clear et gère le menu
    Clear()
    print(" Menu (Les menus ne sont pas à leur place définitive)\n")
    print(" [1]  (Fait) NSC Builder                                                               Is My Switch Patched (Fait) [11]")
    print(" [2]  (Fait) [NSP NSZ XCi XCZ] Converter                                                     Install Driver (Fait) [12]\n")
                    
    print(" [3]  (Fait) LanPlay                                           SwitchGet (Gestionnaire D'Apps Et Theme) (En Cours) [13]")
    print(" [4]  (Fait) SysDVR                                                               SD Cleaner / Installer (À Faire) [14]\n")
                
    print(" [5]  (À Faire) SD Updater                                                                   NSP Spliter (A Faire) [15]")
    print(" [6]  (À Faire) SD Corruption Cleaner                                                         NST To XCI (A Faire) [16]")
    print(" [7]  (À Faire) SD Backup\n")
                
    print(" [8]  (Fait) [Android Linux] Flasheur")
    print(" [9]  (Fait) Payload Loader\n")
                
    print(" [10] (À Faire) Update SwitchUniversal\n")
    print("                                                                                                            Quitter [Q]")


#Que fais tu ?