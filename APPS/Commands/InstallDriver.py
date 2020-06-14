import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def InstallDriver():
    ZadigOrTegra = ""
    while ZadigOrTegra != "q":
        Clear()
        print(" Voulez-vous Zadig[Z] ou Tegra[T]\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")
        ZadigOrTegra = input("Que choisissez vous: ")
        ZadigOrTegra = ZadigOrTegra.lower()

        if ZadigOrTegra == "q":
            return()
        elif ZadigOrTegra == "z":
            os.system('"Data\\Zadig\\zadig-2.5.exe"')
            return()
            
        elif ZadigOrTegra == "t":
            os.system('"Data\\PayloadLoader\\apx_driver\\InstallDriver.exe"')
            return()
