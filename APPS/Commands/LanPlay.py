import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def LanPlay():# Menu [(3) LanPlay Loader]
    Clear()
    print(" Connexion au LanPlay\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")

    InstallWinPcap = input(" Voulez-vous installer WinPcap ? [O/Entrer]: ")
    InstallWinPcap = InstallWinPcap.lower()
    if InstallWinPcap == "q":
        return()
    if InstallWinPcap == "o":
        os.system("Data\\LanPlay\\WinPcap_4_1_3.exe")

    LanPlayIP = ""
    while LanPlayIP == "":
        Clear()
        print(" Connexion au LanPlay\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")
        LanPlayIP = input(" Entrez l'adresse IP du server LanPlay: ")
        LanPlayIP = LanPlayIP.lower()
        if LanPlayIP == "q":
            return()

    Clear()
    print(" Connexion au LanPlay\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quiter\n")
    LanPlayPmut = input(" Entrez votre PMTU ou faites entrer pour passer: ")
    LanPlayPmut = LanPlayPmut.lower()
    if LanPlayPmut == "q":
        return()
    if LanPlayPmut == "":
        os.system(f"Data\\LanPlay\\lan-play-win64.exe --relay-server-addr {LanPlayIP} --pmtu 500")
    else:
        os.system(f"Data\\LanPlay\\lan-play-win64.exe --relay-server-addr {LanPlayIP} --pmtu {LanPlayPmut}")
