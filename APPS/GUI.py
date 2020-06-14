from tkinter import *
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
from Commands.SDBackup import SDBackup
from Commands.SDCorruptionCleaner import SDCoruptionCleaner
from Commands.SDUpdater import SDUpdater
from Commands.SwitchGet import SwitchGet
from Commands.SwitchUniversaleUpdater import SwitchUniversaleUpdater
from Commands.SDCleaner import SDCleaner
import os
Path = os.getcwd()
# Interface

# Toutes les fenetres
GUIMain = Tk()

# Parametre de GUIMain
GUIMain.title("Switch Universale")
GUIMain.geometry("820x480")
GUIMain.minsize(720, 300)
GUIMain.maxsize(920, 580)
GUIMain.iconbitmap("GUI/Logo.ico")
GUIMain.config(background="#363636")

# Ajout de contenu
FrameHeader = Frame(GUIMain, bg="#363636")

ImageHeader = PhotoImage(file="GUI/Pika45.png").zoom(1).subsample(1)
CanvasHeader = Canvas(FrameHeader, width=48, height=48, bg="#363636", bd=0, highlightthickness=0)
CanvasHeader.create_image(25, 25, image=ImageHeader)
CanvasHeader.grid(row=0, column=1, sticky=N)

LabelTitle = Label(FrameHeader, text="Switch Universale", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")
LabelTitle.grid(row=0, column=0, sticky=N)

FrameHeader.pack()

'''
Textes Variables
'''

'''
Fonctions boutons
'''

def ClearGui():
    BoutonNSCBuilder.grid_forget()
    BoutonNSPToNSZConverter.grid_forget()
    BoutonLanplay.grid_forget()
    BoutonSysDvr.grid_forget()
    BoutonSDUpdater.grid_forget()
    BoutonSDCoruptionCleaner.grid_forget()
    BoutonSDBackup.grid_forget()
    BoutonSDFlacher.grid_forget()
    BoutonPayloadLoader.grid_forget()
    BoutonSwitchUniversaleUpdater.grid_forget()
    BoutonIsMySwitchPatched.grid_forget()
    BoutonInstallDriver.grid_forget()
    BoutonSwitchGet.grid_forget()
    BoutonSDCleaner.grid_forget()
#Lanplay
def LanplaySuivant():
    global WinPcapText
    global WinPcapOui
    global WinPcapNon
    global IpEntry
    global IpText
    global IpButton
    WinPcapText.pack_forget()
    WinPcapOui.pack_forget()
    WinPcapNon.pack_forget()
    IpEntry.pack(side="top")
    IpText.pack(side="top")
    IpButton.pack(side="top")

def GetIp():
    global LanPlayIP
    global IpEntry
    global IpText
    global IpButton
    global PmtuEntry
    global PmtuButton
    global PmtuText
    LanPlayIP = IpEntry.get()
    IpEntry.pack_forget()
    IpText.pack_forget()
    IpButton.pack_forget()
    PmtuEntry.pack(side="top")
    PmtuButton.pack(side="top")
    PmtuText.pack(side="top")

    

def LanplayOui():
    LanplaySuivant()
    os.system("Data\\LanPlay\\WinPcap_4_1_3.exe")
def LanplayGui():
    global WinPcapText
    global WinPcapOui
    global WinPcapNon
    ClearGui()
    WinPcapText.pack(side="top")
    WinPcapOui.pack(side="left")
    WinPcapNon.pack(side="right")

def Finish():
    global PmtuEntry
    global PmtuButton
    global PmtuText
    global LanPlayPmtu
    global LanPlayIP
    LanPlayPmtu = PmtuEntry.get()
    PmtuEntry.pack_forget()
    PmtuText.pack_forget()
    PmtuButton.pack_forget()
    Gui()
    if LanPlayPmtu == "":
        os.system(f"Data\\LanPlay\\lan-play-win64.exe --relay-server-addr {LanPlayIP} --pmtu 500")
    else:
        os.system(f"Data\\LanPlay\\lan-play-win64.exe --relay-server-addr {LanPlayIP} --pmtu {LanPlayPmtu}")
'''
Variables fonctions
'''

#Lanplay
LanPlayIP =""
LanPlayPmtu = ""
WinPcapText =Label (text="Voulez vous installez Winpcap ?",font=("Courrier", 14))
WinPcapOui = Button(text="Oui", command=LanplayOui)
WinPcapNon = Button(text="Non", command=LanplaySuivant)
IpEntry = Entry()
IpText =Label (text=" Entrez l'adresse IP du server LanPlay:",font=("Courrier", 14))
IpButton= Button(text="Suivant !", command=GetIp)
PmtuEntry = Entry()
PmtuText =Label (text="Entrez votre PMTU, cliquez sur suivant pour avoir le PMTU de base",font=("Courrier", 14))
PmtuButton = Button(text="Suivant !",command=Finish)
# Ajout d'application
FrameBG = Frame(GUIMain, bg="#363636")

'''
Menu GUI
'''
#NSCBuilder 1
ImgNSCB = PhotoImage(file="GUI/ButtunNSCB.png")
BoutonNSCBuilder = Button(FrameBG, text="NSC Builder", command=NSCBuilder, font=("Courrier", 14))
BoutonNSCBuilder.config(image=ImgNSCB, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#NSZ Converter 2
ImgNSZ = PhotoImage(file="GUI/ButtunNSZ.png")
BoutonNSPToNSZConverter = Button(FrameBG, text="(NSP NSZ XCI XCZ) Converter", command=NSPToNSZConverter, font=("Courrier", 14))
BoutonNSPToNSZConverter.config(image=ImgNSZ, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space2 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#Lanplay 3
ImgLanplay = PhotoImage(file="GUI/ButtunLanPlay.png")
BoutonLanplay = Button(FrameBG, text="LanPlay", command=LanplayGui, font=("Courrier", 14))
BoutonLanplay.config(image=ImgLanplay, height= 40, bg="#363636", bd=0, highlightthickness=0)

Enter = Label(FrameBG, text="        ", font=("Courrier", 12), bg="#363636", fg="#FFFFFF")

#Sysdvr 4
ImgSysDvr = PhotoImage(file="GUI/ButtunSysDVR.png")
BoutonSysDvr = Button(FrameBG, text="SysDVR", command=SysDVR, font=("Courrier", 14))
BoutonSysDvr.config(image=ImgLanplay, height= 40, bg="#363636", bd=0, highlightthickness=0)


Space3 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#SD Updater 5
ImgSDUpdater = PhotoImage(file="GUI/SDUpdater.png")
BoutonSDUpdater = Button(FrameBG, text="SDUpdater", command=SDUpdater, font=("Courrier", 14))
BoutonSDUpdater.config(image=ImgSDUpdater, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space4 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#SDCorruptionCleaner 6
ImgSDCoruptionCleaner = PhotoImage(file="GUI/SDCorruptionCleaner.png")
BoutonSDCoruptionCleaner = Button(FrameBG, text="SDCorruptionCleaner", command=SDCoruptionCleaner, font=("Courrier", 14))
BoutonSDCoruptionCleaner.config(image=ImgLanplay, height= 40, bg="#363636", bd=0, highlightthickness=0)

Enter2 = Label(FrameBG, text="        ", font=("Courrier", 12), bg="#363636", fg="#FFFFFF")

#SDBackup 7
ImgSDBackup = PhotoImage(file="GUI/SDBackup.png")
BoutonSDBackup = Button(FrameBG, text="SDBackup", command=SDBackup, font=("Courrier", 14))
BoutonSDBackup.config(image=ImgSDBackup, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space5 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#(Android / Linux) Flasher 8
ImgSDFlacher = PhotoImage(file="GUI/SDFlasher.png")
BoutonSDFlacher = Button(FrameBG, text="(Android / Linux) Flasher", command=SDFlacher, font=("Courrier", 14))
BoutonSDFlacher.config(image=ImgSDFlacher, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space6 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#Payload Loader 9
ImgPayloadLoader = PhotoImage(file="GUI/PayloadLoader.png")
BoutonPayloadLoader = Button(FrameBG, text="Payload Loader", command=PayloadLoader, font=("Courrier", 14))
BoutonPayloadLoader.config(image=ImgPayloadLoader, height= 40, bg="#363636", bd=0, highlightthickness=0)

Enter3 = Label(FrameBG, text="        ", font=("Courrier", 12), bg="#363636", fg="#FFFFFF")

#SDBackup 10
ImgSwitchUniversaleUpdater = PhotoImage(file="GUI/SwitchUniversaleUpdater.png")
BoutonSwitchUniversaleUpdater = Button(FrameBG, text="Switch Universale Updater", command=SwitchUniversaleUpdater, font=("Courrier", 14))
BoutonSwitchUniversaleUpdater.config(image=ImgSwitchUniversaleUpdater, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space7 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#(Android / Linux) Flasher 11
ImgIsMySwitchPatched = PhotoImage(file="GUI/IsMySwitchPatched.png")
BoutonIsMySwitchPatched = Button(FrameBG, text="Is My Switch Patched", command=IsMySwitchPatched, font=("Courrier", 14))
BoutonIsMySwitchPatched.config(image=ImgIsMySwitchPatched, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space8 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#InstallDriver 12
ImgInstallDriver = PhotoImage(file="GUI/InstallDriver.png")
BoutonInstallDriver = Button(FrameBG, text="Install Driver", command=InstallDriver, font=("Courrier", 14))
BoutonInstallDriver.config(image=ImgInstallDriver, height= 40, bg="#363636", bd=0, highlightthickness=0)

Enter4 = Label(FrameBG, text="        ", font=("Courrier", 12), bg="#363636", fg="#FFFFFF")
 
#SwitchGet 13
ImgSwitchGet = PhotoImage(file="GUI/SwitchGet.png")
BoutonSwitchGet = Button(FrameBG, text="SwitchGet (Gestionnaire / Installer D'Apps Et Theme)", command=SwitchGet, font=("Courrier", 14))
BoutonSwitchGet.config(image=ImgSwitchGet, height= 40, bg="#363636", bd=0, highlightthickness=0)

Space8 = Label(FrameBG, text="        ", font=("Courrier", 25), bg="#363636", fg="#FFFFFF")

#InstallDriver 14 
ImgSDCleaner = PhotoImage(file="GUI/SDCleaner.png")
BoutonSDCleaner = Button(FrameBG, text="SD Cleaner", command=SDCleaner, font=("Courrier", 14))
BoutonSDCleaner.config(image=ImgSDCleaner, height= 40, bg="#363636", bd=0, highlightthickness=0)




def Gui():
    #NSCBuilder 1
    global BoutonNSCBuilder
    BoutonNSCBuilder.grid(row=0, column=0, sticky=N) 

    Space.grid(row=0, column=1, sticky=N)

    #NSZ Converter 2
    global BoutonNSPToNSZConverter
    BoutonNSPToNSZConverter.grid(row=0, column=2, sticky=N)

    Space2.grid(row=0, column=3, sticky=N) 

    #Lanplay 3
    global BoutonLanplay
    BoutonLanplay.grid(row=0, column=4, sticky=N)


    Enter.grid(row=1, column=0, sticky=N)


    #Sysdvr 4
    global BoutonSysDvr
    BoutonSysDvr.grid(row=2, column=0, sticky=N) 

    Space3.grid(row=2, column=1, sticky=N)

    #SD Updater 5
    global BoutonSDUpdater
    BoutonSDUpdater.grid(row=2, column=2, sticky=N)

    Space4.grid(row=2, column=3, sticky=N) 

    #SDCorruptionCleaner 6
    global BoutonSDCoruptionCleaner
    BoutonSDCoruptionCleaner.grid(row=2, column=4, sticky=N)


    Enter2.grid(row=3, column=0, sticky=N)
    

    #SDBackup 7
    global BoutonSDBackup
    BoutonSDBackup.grid(row=4, column=0, sticky=N) 

    Space5.grid(row=4, column=1, sticky=N)

    #(Android / Linux) Flasher 8
    global BoutonSDFlacher
    BoutonSDFlacher.grid(row=4, column=2, sticky=N)


    Space6.grid(row=4, column=3, sticky=N) 

    #Payload Loader 9
    global BoutonPayloadLoader
    BoutonPayloadLoader.grid(row=4, column=4, sticky=N)


    Enter3.grid(row=5, column=0, sticky=N)


    #SDBackup 10
    global BoutonSwitchUniversaleUpdater
    BoutonSwitchUniversaleUpdater.grid(row=6, column=0, sticky=N) 


    Space7.grid(row=6, column=1, sticky=N)

    #(Android / Linux) Flasher 11
    global BoutonIsMySwitchPatched
    BoutonIsMySwitchPatched.grid(row=6, column=2, sticky=N)

    Space8.grid(row=6, column=3, sticky=N) 

    #InstallDriver 12
    global BoutonInstallDriver
    BoutonInstallDriver.grid(row=6, column=4, sticky=N)


    Enter4.grid(row=7, column=0, sticky=N)

    #SwitchGet 13
    global BoutonSwitchGet
    BoutonSwitchGet.grid(row=8, column=0, sticky=N)

    Space8.grid(row=8, column=1, sticky=N) 

    #InstallDriver 14 
    global BoutonSDCleaner
    BoutonSDCleaner.grid(row=8, column=2, sticky=N)
    FrameBG.pack(expand=YES)
Gui()
# Start de toutes les fenetres
'''
Fin du Menu GUI
'''
'''
Début provisoire
'''

# Enlève tous les boutons du menus
GUIMain.mainloop()