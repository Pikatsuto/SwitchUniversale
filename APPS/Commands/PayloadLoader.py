import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def PayloadLoader():# Menu [(9) Payload Loader]
    InputPayload = ""
    PayloadFin = False
    while InputPayload != "q":
        Clear()
        print("Insérez tous vos payloads dans le dossier Payload (Pour les tests j'ai mis les payloads de rr ils seront retirés)\n")
        NBPayload = 0
        Payload = os.listdir("Payload")
        ChoisPayload = 30

        for Name in Payload:
            if NBPayload >= 10:
                print(f" ({NBPayload}) {Name}")
            else:
                print(f" ({NBPayload})  {Name}")

            NBPayload += 1
            if NBPayload == 16:
                break

        Ligne = (19 - NBPayload - 2)

        while Ligne != 0:
            print("")
            Ligne -= 1
        
        print(" (Q) Quitter\n")
        InputPayload = input("Que choisissez-vous ?: ")
        InputPayload = InputPayload.lower()
        
        try:
            ChoisPayload = int(InputPayload)
        except ValueError:
            ChoisPayload = 30

        NBPayload = 0
        for Name in Payload:
            UsePayload = Payload[NBPayload]
            if (ChoisPayload) == NBPayload:
                UsePayload = Payload[NBPayload]
                os.system(f"Data\\PayloadLoader\\TegraRcmSmash.exe Payload\\{UsePayload}")
                PayloadFin = True
                break
            NBPayload += 1
        
        if PayloadFin == True:
            InputPayload = "q"
