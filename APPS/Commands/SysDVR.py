import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def SysDVR():# Menu [(4) SysDVR Loader]
    ChoisSysDVR = 0
    while ChoisSysDVR < 1 or ChoisSysDVR > 2:
        Clear()
        print(" Comment voulez-vous streamer votre Switch ?")
        print(" (1) USB\n (2) WIFI\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")

        ChoisSysDVR = input(" Que choisissez-vous: ")
        ChoisSysDVR = ChoisSysDVR.lower()
        if ChoisSysDVR == "q":
            return()
        if ChoisSysDVR == "":
            ChoisSysDVR = 0
        else:
            ChoisSysDVR = int(ChoisSysDVR)
    Clear()
    print(" Comment voulez-vous streamer votre Switch ?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")
    ChoisNETCore = input(" Voulez-vous installer .NET Core 3.1.4 ? [O/Entrer]: ")
    ChoisNETCore = ChoisNETCore.lower
    if ChoisNETCore == "q":
        return()
    if ChoisNETCore == "o":
        os.system("Data\\SysDVR\\Installer\\Installer.exe")
        return("")
    if ChoisSysDVR == 1:
        os.system("start dotnet SysDVR-Client.dll usb")
        os.system("timeout 2 > NUL && \"Data\\SysDVR\\MVPA\\mpv.com\" rtsp://127.0.0.1:6666/")
    if ChoisSysDVR == 2:
        IPSysDVR = ""
        while IPSysDVR == "":
            Clear()
            print(" Streamer de la Switch\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")
            IPSysDVR = input(" Entrez l'adresse IP de votre Switch: ")
            IPSysDVR = IPSysDVR.lower()
            if IPSysDVR == "q":
                return()
        os.system(f"start dotnet SysDVR-Client.dll bridge {IPSysDVR}")
        os.system("timeout 2 > NUL && \"Data\\SysDVR\\MVPA\\mpv.com\" rtsp://127.0.0.1:6666/")
